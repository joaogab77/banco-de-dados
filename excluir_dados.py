import tkinter as tk
from tkinter import messagebox, Entry, Listbox, Button, Frame
import sqlite3


class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.create_table()

    def create_table(self):
        c = self.conexao.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS tbl_usuarios (
            idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            usuario TEXT,
            senha TEXT
        )
        """)
        self.conexao.commit()
        c.close()

    def delete_user(self, user_id):
        c = self.conexao.cursor()
        c.execute("DELETE FROM tbl_usuarios WHERE idusuario=?", (user_id,))
        self.conexao.commit()
        c.close()

    def get_all_users(self):
        c = self.conexao.cursor()
        c.execute("SELECT * FROM tbl_usuarios")
        users = c.fetchall()
        c.close()
        return users


class SistemaGestao:
    def __init__(self, master):
        self.master = master
        self.banco = Banco()

        self.frame = Frame(master)
        self.frame.pack(pady=20)

        self.user_list = Listbox(self.frame)
        self.user_list.pack()

        self.btn_excluir = Button(self.frame, text="Excluir", command=self.excluir_usuario)
        self.btn_excluir.pack(pady=10)

        self.atualizar_lista()

    def atualizar_lista(self):
        self.user_list.delete(0, tk.END)
        users = self.banco.get_all_users()
        for user in users:
            self.user_list.insert(tk.END, f"ID: {user[0]} | Nome: {user[1]}")

    def excluir_usuario(self):
        try:
            selected = self.user_list.curselection()
            if not selected:
                messagebox.showwarning("Aviso", "Selecione um usuário para excluir.")
                return

            user_id = self.user_list.get(selected[0]).split('|')[0].split(':')[1].strip()
            self.banco.delete_user(user_id)
            messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
            self.atualizar_lista()
        except Exception as e:
            messagebox.showerror("Erro", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Gestão")
    SistemaGestao(root)
    root.mainloop()