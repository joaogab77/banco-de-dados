import tkinter as tk
from tkinter import messagebox, PhotoImage, Frame
import principal

def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "admin" and senha == "1234":
        root.destroy()
        principal.abrir_pagina_principal()
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")

class Imagem():
    def __init__(self, master):
        # Cria um Frame para organizar os widgets
        self.wdgt3 = tk.Frame(master)
        self.wdgt3["padx"] = 20
        self.wdgt3["pady"] = 5
        self.wdgt3.pack()

        # Carrega e exibe a imagem

        self.img = PhotoImage(file="imagem/image.png")
        self.lblimg = tk.Label(self.janela, image=self.img)
        self.lblimg.pack()


# Criar a janela principal
root = tk.Tk()
root.title("Tela de Login")

# Adicionar um frame para organizar os widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20, expand=True)



# Adicionar rótulo e campos de entrada ao frame
label_usuario = tk.Label(frame, text="Usuário:")
label_usuario.pack(pady=(10, 0))  # Adiciona um pouco de padding acima

entry_usuario = tk.Entry(frame)
entry_usuario.pack(pady=(5, 10))  # Adiciona um pouco de padding abaixo

label_senha = tk.Label(frame, text="Senha:")
label_senha.pack(pady=(10, 0))  # Adiciona um pouco de padding acima

entry_senha = tk.Entry(frame, show="*")
entry_senha.pack(pady=(5, 10))  # Adiciona um pouco de padding abaixo

btn_login = tk.Button(frame, text="Login", command=verificar_login)
btn_login.pack(pady=20)  # Adiciona padding para separar o botão dos campos

# Configurar o tamanho da janela
root.geometry("300x300")  # Tamanho adequado para a tela de login

# Executar o loop principal
root.mainloop()
