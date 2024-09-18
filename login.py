import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error



def validar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    try:
        # Conexão com o banco de dados MySQL
        connection = mysql.connector.connect(
            host='localhost',  # Substitua pelo host do servidor MySQL
            database='dbescola',  # Substitua pelo nome do banco de dados
            user='tiao',  # Substitua pelo seu usuário MySQL
            password='123456'  # Substitua pela senha do MySQL
        )

        if connection.is_connected():
            cursor = connection.cursor()

            query = "SELECT * FROM usuarios WHERE nome_usuario = %s AND senha = %s"
            cursor.execute(query, (usuario, senha))
            resultado = cursor.fetchone()

            if resultado:
                messagebox.showinfo("Login bem-sucedido", "Bem-vindo!")
            else:
                messagebox.showwarning("Falha no login", "Usuário ou senha incorretos")

    except Error as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()



root = tk.Tk()
root.title("Login")


label_usuario = tk.Label(root, text="Usuário")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(root)
entry_usuario.pack(pady=5)

label_senha = tk.Label(root, text="Senha")
label_senha.pack(pady=5)
entry_senha = tk.Entry(root, show="*")
entry_senha.pack(pady=5)


botao_login = tk.Button(root, text="Login", command=validar_login)
botao_login.pack(pady=20)


root.mainloop()
