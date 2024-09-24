import tkinter as tk
from tkinter import *
import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import tempfile


# Classe de conexão com o banco de dados
class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.create_table()

    def create_table(self):
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS tbl_usuarios (
            idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            email TEXT,
            usuario TEXT,
            senha TEXT,
            cidade TEXT
        )""")
        self.conexao.commit()
        c.close()

    def get_connection(self):
        return self.conexao


class Usuarios:
    def __init__(self):
        self.banco = Banco()

    def selectUser(self, idusuario):
        conexao = self.banco.get_connection()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tbl_usuarios WHERE idusuario = ?", (idusuario,))
        usuario = cursor.fetchone()
        conexao.close()
        if usuario:
            self.idusuario, self.nome, self.telefone, self.email, self.usuario, self.senha, self.cidade = usuario
            return True
        return False

    def insertUser(self, nome, telefone, email, usuario, senha, cidade):
        conexao = self.banco.get_connection()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO tbl_usuarios (nome, telefone, email, usuario, senha, cidade) VALUES (?, ?, ?, ?, ?, ?)",
            (nome, telefone, email, usuario, senha, cidade))
        conexao.commit()
        conexao.close()

    def updateUser(self, idusuario, nome, telefone, email, usuario, senha, cidade):
        conexao = self.banco.get_connection()
        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE tbl_usuarios SET nome = ?, telefone = ?, email = ?, usuario = ?, senha = ?, cidade = ? WHERE idusuario = ?",
            (nome, telefone, email, usuario, senha, cidade, idusuario))
        conexao.commit()
        conexao.close()

    def deleteUser(self, idusuario):
        conexao = self.banco.get_connection()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM tbl_usuarios WHERE idusuario = ?", (idusuario,))
        conexao.commit()
        conexao.close()

    def getAllUsers(self):
        conexao = self.banco.get_connection()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tbl_usuarios")
        usuarios = cursor.fetchall()
        conexao.close()
        return usuarios


class SistemaGestao:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.janela.pack(fill=BOTH, expand=True)

        self.titulo = Label(self.janela, text="Gerenciamento de Usuários", font=("Arial", 20, "bold"))
        self.titulo.pack(pady=20)

        self.frame_campos = Frame(self.janela)
        self.frame_campos.pack(pady=10)

        self.idUsuarioLabel = Label(self.frame_campos, text="ID Usuário:")
        self.idUsuarioLabel.grid(row=0, column=0, padx=5, pady=5, sticky=E)
        self.idUsuario = Entry(self.frame_campos)
        self.idUsuario.grid(row=0, column=1, padx=5, pady=5)

        self.btn_buscar = Button(self.frame_campos, text="Buscar", command=self.buscarUsuario)
        self.btn_buscar.grid(row=0, column=2, padx=5, pady=5)

        self.nomeLabel = Label(self.frame_campos, text="Nome:")
        self.nomeLabel.grid(row=1, column=0, padx=5, pady=5, sticky=E)
        self.nome = Entry(self.frame_campos)
        self.nome.grid(row=1, column=1, padx=5, pady=5)

        self.telefoneLabel = Label(self.frame_campos, text="Telefone:")
        self.telefoneLabel.grid(row=2, column=0, padx=5, pady=5, sticky=E)
        self.telefone = Entry(self.frame_campos)
        self.telefone.grid(row=2, column=1, padx=5, pady=5)

        self.emailLabel = Label(self.frame_campos, text="Email:")
        self.emailLabel.grid(row=3, column=0, padx=5, pady=5, sticky=E)
        self.email = Entry(self.frame_campos)
        self.email.grid(row=3, column=1, padx=5, pady=5)

        self.usuarioLabel = Label(self.frame_campos, text="Usuário:")
        self.usuarioLabel.grid(row=4, column=0, padx=5, pady=5, sticky=E)
        self.usuario = Entry(self.frame_campos)
        self.usuario.grid(row=4, column=1, padx=5, pady=5)

        self.senhaLabel = Label(self.frame_campos, text="Senha:")
        self.senhaLabel.grid(row=5, column=0, padx=5, pady=5, sticky=E)
        self.senha = Entry(self.frame_campos, show="*")
        self.senha.grid(row=5, column=1, padx=5, pady=5)

        self.cidadeLabel = Label(self.frame_campos, text="Cidade:")
        self.cidadeLabel.grid(row=6, column=0, padx=5, pady=5, sticky=E)
        self.cidade = Entry(self.frame_campos)
        self.cidade.grid(row=6, column=1, padx=5, pady=5)

        self.janela_botoes = Frame(self.janela)
        self.janela_botoes.pack(pady=20)

        self.btn_inserir = Button(self.janela_botoes, text="Inserir", command=self.inserirUsuario)
        self.btn_inserir.grid(row=0, column=0, padx=5)

        self.btn_alterar = Button(self.janela_botoes, text="Alterar", command=self.alterarUsuario)
        self.btn_alterar.grid(row=0, column=1, padx=5)

        self.btn_excluir = Button(self.janela_botoes, text="Excluir", command=self.excluirUsuario)
        self.btn_excluir.grid(row=0, column=2, padx=5)

        self.btn_visualizar_pdf = Button(self.janela_botoes, text="Visualizar PDF", command=self.visualizarPdf)
        self.btn_visualizar_pdf.grid(row=0, column=3, padx=5)

        self.btn_sair = Button(self.janela_botoes, text="Sair", command=self.sairAplicativo)
        self.btn_sair.grid(row=0, column=4, padx=5)

        self.lblmsg = Label(self.janela, text="")
        self.lblmsg.pack()

        self.frame_lista = Frame(self.janela)
        self.frame_lista.pack(pady=20, fill=BOTH, expand=True)

        self.lista_usuarios = Listbox(self.frame_lista, width=80, height=20, selectmode=SINGLE)
        self.lista_usuarios.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar_vertical = Scrollbar(self.frame_lista, orient=VERTICAL, command=self.lista_usuarios.yview)
        self.scrollbar_vertical.pack(side=RIGHT, fill=Y)

        self.lista_usuarios.config(yscrollcommand=self.scrollbar_vertical.set)

        self.atualizarListaUsuarios()

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.idUsuario.get()
        if user.selectUser(idusuario):
            self.nome.delete(0, END)
            self.nome.insert(INSERT, user.nome)
            self.telefone.delete(0, END)
            self.telefone.insert(INSERT, user.telefone)
            self.email.delete(0, END)
            self.email.insert(INSERT, user.email)
            self.usuario.delete(0, END)
            self.usuario.insert(INSERT, user.usuario)
            self.senha.delete(0, END)
            self.senha.insert(INSERT, user.senha)
            self.cidade.delete(0, END)
            self.cidade.insert(INSERT, user.cidade)
            self.lblmsg["text"] = "Usuário encontrado!"
        else:
            self.limparCampos()
            self.lblmsg["text"] = "Usuário não encontrado."

    def inserirUsuario(self):
        user = Usuarios()
        user.insertUser(self.nome.get(), self.telefone.get(), self.email.get(),
                        self.usuario.get(), self.senha.get(), self.cidade.get())
        self.lblmsg["text"] = "Usuário inserido com sucesso!"
        self.limparCampos()
        self.atualizarListaUsuarios()

    def alterarUsuario(self):
        user = Usuarios()
        user.updateUser(self.idUsuario.get(), self.nome.get(), self.telefone.get(),
                        self.email.get(), self.usuario.get(), self.senha.get(), self.cidade.get())
        self.lblmsg["text"] = "Usuário atualizado com sucesso!"
        self.limparCampos()
        self.atualizarListaUsuarios()

    def excluirUsuario(self):
        user = Usuarios()
        user.delete
        user.deleteUser(self.idUsuario.get())
        self.lblmsg["text"] = "Usuário excluído com sucesso!"
        self.limparCampos()
        self.atualizarListaUsuarios()

    def limparCampos(self):
        self.idUsuario.delete(0, END)
        self.nome.delete(0, END)
        self.telefone.delete(0, END)
        self.email.delete(0, END)
        self.usuario.delete(0, END)
        self.senha.delete(0, END)
        self.cidade.delete(0, END)

    def atualizarListaUsuarios(self):
        self.lista_usuarios.delete(0, END)
        user = Usuarios()
        usuarios = user.getAllUsers()
        for u in usuarios:
            self.lista_usuarios.insert(END,
                                       f"ID: {u[0]} | Nome: {u[1]} | Telefone: {u[2]} | Email: {u[3]} | Usuário: {u[4]} | Cidade: {u[6]}")

    def visualizarPdf(self):
        user = Usuarios()
        usuarios = user.getAllUsers()

        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
            pdf_path = temp_pdf.name

        c = canvas.Canvas(pdf_path, pagesize=letter)
        width, height = letter
        c.drawString(100, height - 100, "Relatório de Usuários")
        y = height - 140
        for u in usuarios:
            c.drawString(100, y,
                         f"ID: {u[0]} | Nome: {u[1]} | Telefone: {u[2]} | Email: {u[3]} | Usuário: {u[4]} | Cidade: {u[6]}")
            y -= 20
            if y < 100:
                c.showPage()
                y = height - 100
        c.save()

        try:
            if os.name == 'nt':
                os.startfile(pdf_path)
            elif os.name == 'posix':
                os.system(f'open "{pdf_path}"' if os.uname().sysname == 'Darwin' else f'xdg-open "{pdf_path}"')
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o PDF: {e}")

    def sairAplicativo(self):
        self.janela.master.destroy()


def abrir_pagina_principal():
    root = Tk()
    root.title("Sistema de Gestão")
    root.geometry("800x600")
    SistemaGestao(root)
    root.mainloop()


# Não executar automaticamente ao ser importado
if __name__ == "__main__":
    abrir_pagina_principal()
