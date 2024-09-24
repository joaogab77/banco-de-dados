import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error


# Função para conectar ao banco de dados
def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host='localhost',  # Endereço do servidor MySQL
            user='tiao',  # Nome de usuário do MySQL
            password='123456',  # Senha do MySQL
            database='DBescola'  # Nome do banco de dados
        )
        return conexao
    except Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None


# Função para validar o login
def validar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if not usuario or not senha:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
        return

    conexao = conectar_banco()
    if conexao is None:
        messagebox.showerror("Erro", "Erro de conexão com o banco de dados.")
        return

    try:
        cursor = conexao.cursor()
        query = "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s"
        cursor.execute(query, (usuario, senha))
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            # Aqui você pode chamar outra janela ou interface, como o dashboard
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    except Error as erro:
        messagebox.showerror("Erro", f"Erro ao validar o login: {erro}")

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()


# Função para criar a interface gráfica de login
def criar_interface_login():
    global entry_usuario, entry_senha

    # Janela principal
    janela = tk.Tk()
    janela.title("Login")
    janela.geometry("300x200")

    # Label e Entry para o usuário
    label_usuario = tk.Label(janela, text="Usuário")
    label_usuario.pack(pady=10)
    entry_usuario = tk.Entry(janela)
    entry_usuario.pack(pady=5)

    # Label e Entry para a senha
    label_senha = tk.Label(janela, text="Senha")
    label_senha.pack(pady=10)
    entry_senha = tk.Entry(janela, show="*")
    entry_senha.pack(pady=5)

    # Botão para login
    botao_login = tk.Button(janela, text="Login", command=validar_login)
    botao_login.pack(pady=20)

    janela.mainloop()


# Executar a interface de login
criar_interface_login()
