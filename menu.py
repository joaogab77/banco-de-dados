import tkinter as tk
from tkinter import messagebox, simpledialog
import mysql.connector
from mysql.connector import Error


# Função para conectar ao banco de dados
def conectar():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='dbescola',
            user='tiao',
            password='123456'
        )
        return connection
    except Error as e:
        messagebox.showerror("Erro de Conexão", f"Erro ao conectar ao MySQL: {e}")
        return None


# Funções para cada menu
def gerenciar_cidades():
    def adicionar_cidade():
        nome = simpledialog.askstring("Entrada", "Nome da Cidade:")
        uf = simpledialog.askstring("Entrada", "UF da Cidade:")
        if nome and uf:
            connection = conectar()
            if connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO tbl_cidades (cid_nome, cid_UF) VALUES (%s, %s)", (nome, uf))
                    connection.commit()
                    messagebox.showinfo("Sucesso", "Cidade adicionada com sucesso!")
                except Error as e:
                    messagebox.showerror("Erro", f"Erro ao adicionar cidade: {e}")
                finally:
                    cursor.close()
                    connection.close()

    def visualizar_cidades():
        connection = conectar()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM tbl_cidades")
                result = cursor.fetchall()
                if result:
                    texto = "\n".join([f"ID: {row[0]}, Nome: {row[1]}, UF: {row[2]}" for row in result])
                    messagebox.showinfo("Cidades", texto)
                else:
                    messagebox.showinfo("Cidades", "Nenhuma cidade encontrada.")
            except Error as e:
                messagebox.showerror("Erro", f"Erro ao visualizar cidades: {e}")
            finally:
                cursor.close()
                connection.close()

    # Criar a janela para gerenciamento de cidades
    janela_cidades = tk.Toplevel(root)
    janela_cidades.title("Gerenciar Cidades")
    janela_cidades.geometry("1000x500")

    btn_adicionar = tk.Button(janela_cidades, text="Adicionar Cidade", command=adicionar_cidade)
    btn_adicionar.pack(pady=10)

    btn_visualizar = tk.Button(janela_cidades, text="Visualizar Cidades", command=visualizar_cidades)
    btn_visualizar.pack(pady=10)


def gerenciar_cursos():
    def adicionar_curso():
        nome = simpledialog.askstring("Entrada", "Nome do Curso:")
        valor = simpledialog.askstring("Entrada", "Valor do Curso:")
        if nome and valor:
            connection = conectar()
            if connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO tbl_cursos (cur_nome, cur_valor) VALUES (%s, %s)", (nome, valor))
                    connection.commit()
                    messagebox.showinfo("Sucesso", "Curso adicionado com sucesso!")
                except Error as e:
                    messagebox.showerror("Erro", f"Erro ao adicionar curso: {e}")
                finally:
                    cursor.close()
                    connection.close()

    def visualizar_cursos():
        connection = conectar()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM tbl_cursos")
                result = cursor.fetchall()
                if result:
                    texto = "\n".join([f"ID: {row[0]}, Nome: {row[1]}, Valor: {row[2]}" for row in result])
                    messagebox.showinfo("Cursos", texto)
                else:
                    messagebox.showinfo("Cursos", "Nenhum curso encontrado.")
            except Error as e:
                messagebox.showerror("Erro", f"Erro ao visualizar cursos: {e}")
            finally:
                cursor.close()
                connection.close()

    # Criar a janela para gerenciamento de cursos
    janela_cursos = tk.Toplevel(root)
    janela_cursos.title("Gerenciar Cursos")
    janela_cursos.geometry("1000x500")

    btn_adicionar = tk.Button(janela_cursos, text="Adicionar Curso", command=adicionar_curso)
    btn_adicionar.pack(pady=10)

    btn_visualizar = tk.Button(janela_cursos, text="Visualizar Cursos", command=visualizar_cursos)
    btn_visualizar.pack(pady=10)


def gerenciar_professores():
    def adicionar_professor():
        nome = simpledialog.askstring("Entrada", "Nome do Professor:")
        endereco = simpledialog.askstring("Entrada", "Endereço do Professor:")
        email = simpledialog.askstring("Entrada", "Email do Professor:")
        telefone = simpledialog.askstring("Entrada", "Telefone do Professor:")
        cpf = simpledialog.askstring("Entrada", "CPF do Professor:")
        idade = simpledialog.askstring("Entrada", "Idade do Professor:")
        cidade = simpledialog.askinteger("Entrada", "Código da Cidade (cid_codigo):")
        aula = simpledialog.askinteger("Entrada", "Código da Aula (aul_codigo):")

        if nome and endereco and email and telefone and cpf and idade:
            connection = conectar()
            if connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute("""
                        INSERT INTO tbl_professores (prof_nome, prof_endereco, prof_email, prof_telefone, prof_CPF, prof_idade, tbl_cidades_cid_codigo, tbl_aulas_aul_codigo)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """, (nome, endereco, email, telefone, cpf, idade, cidade, aula))
                    connection.commit()
                    messagebox.showinfo("Sucesso", "Professor adicionado com sucesso!")
                except Error as e:
                    messagebox.showerror("Erro", f"Erro ao adicionar professor: {e}")
                finally:
                    cursor.close()
                    connection.close()

    def visualizar_professores():
        connection = conectar()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM tbl_professores")
                result = cursor.fetchall()
                if result:
                    texto = "\n".join([
                                          f"ID: {row[0]}, Nome: {row[1]}, Endereço: {row[2]}, Email: {row[3]}, Telefone: {row[4]}, CPF: {row[5]}, Idade: {row[6]}, Cidade: {row[7]}, Aula: {row[8]}"
                                          for row in result])
                    messagebox.showinfo("Professores", texto)
                else:
                    messagebox.showinfo("Professores", "Nenhum professor encontrado.")
            except Error as e:
                messagebox.showerror("Erro", f"Erro ao visualizar professores: {e}")
            finally:
                cursor.close()
                connection.close()

    # Criar a janela para gerenciamento de professores
    janela_professores = tk.Toplevel(root)
    janela_professores.title("Gerenciar Professores")
    janela_professores.geometry("1000x500")

    btn_adicionar = tk.Button(janela_professores, text="Adicionar Professor", command=adicionar_professor)
    btn_adicionar.pack(pady=10)

    btn_visualizar = tk.Button(janela_professores, text="Visualizar Professores", command=visualizar_professores)
    btn_visualizar.pack(pady=10)


def gerenciar_alunos():
    def adicionar_aluno():
        nome = simpledialog.askstring("Entrada", "Nome do Aluno:")
        endereco = simpledialog.askstring("Entrada", "Endereço do Aluno:")
        email = simpledialog.askstring("Entrada", "Email do Aluno:")
        telefone = simpledialog.askstring("Entrada", "Telefone do Aluno:")
        idade = simpledialog.askstring("Entrada", "Idade do Aluno:")
        cidade = simpledialog.askinteger("Entrada", "Código da Cidade (cid_codigo):")
        curso = simpledialog.askinteger("Entrada", "Código do Curso (cur_codigo):")

        if nome and endereco and email and telefone and idade:
            connection = conectar()
            if connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute("""
                        INSERT INTO tbl_alunos (alu_nome, alu_endereco, alu_email, alu_telefone, alu_idade, tbl_cidades_cid_codigo, tbl_cursos_cur_codigo)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (nome, endereco, email, telefone, idade, cidade, curso))
                    connection.commit()
                    messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")
                except Error as e:
                    messagebox.showerror("Erro", f"Erro ao adicionar aluno: {e}")
                finally:
                    cursor.close()
                    connection.close()

    def visualizar_alunos():
        connection = conectar()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM tbl_alunos")
                result = cursor.fetchall()
                if result:
                    texto = "\n".join([
                                          f"ID: {row[0]}, Nome: {row[1]}, Endereço: {row[2]}, Email: {row[3]}, Telefone: {row[4]}, Idade: {row[5]}, Cidade: {row[6]}, Curso: {row[7]}"
                                          for row in result])
                    messagebox.showinfo("Alunos", texto)
                else:
                    messagebox.showinfo("Alunos", "Nenhum aluno encontrado.")
            except Error as e:
                messagebox.showerror("Erro", f"Erro ao visualizar alunos: {e}")
            finally:
                cursor.close()
                connection.close()

    # Criar a janela para gerenciamento de alunos
    janela_alunos = tk.Toplevel(root)
    janela_alunos.title("Gerenciar Alunos")
    janela_alunos.geometry("1000x500")

    btn_adicionar = tk.Button(janela_alunos, text="Adicionar Aluno", command=adicionar_aluno)
    btn_adicionar.pack(pady=10)

    btn_visualizar = tk.Button(janela_alunos, text="Visualizar Alunos", command=visualizar_alunos)
    btn_visualizar.pack(pady=10)


def gerenciar_aulas():
    def adicionar_aula():
        materia = simpledialog.askstring("Entrada", "Matéria da Aula:")
        horario = simpledialog.askstring("Entrada", "Horário da Aula:")
        curso = simpledialog.askinteger("Entrada", "Código do Curso (cur_codigo):")
        aluno = simpledialog.askinteger("Entrada", "Código do Aluno (alu_codigo):")

        if materia and horario:
            connection = conectar()
            if connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute("""
                        INSERT INTO tbl_aulas (aul_materia, aul_horario, tbl_cursos_cur_codigo, tbl_alunos_alu_codigo)
                        VALUES (%s, %s, %s, %s)
                    """, (materia, horario, curso, aluno))
                    connection.commit()
                    messagebox.showinfo("Sucesso", "Aula adicionada com sucesso!")
                except Error as e:
                    messagebox.showerror("Erro", f"Erro ao adicionar aula: {e}")
                finally:
                    cursor.close()
                    connection.close()

    def visualizar_aulas():
        connection = conectar()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM tbl_aulas")
                result = cursor.fetchall()
                if result:
                    texto = "\n".join(
                        [f"ID: {row[0]}, Matéria: {row[1]}, Horário: {row[2]}, Curso: {row[3]}, Aluno: {row[4]}" for row
                         in result])
                    messagebox.showinfo("Aulas", texto)
                else:
                    messagebox.showinfo("Aulas", "Nenhuma aula encontrada.")
            except Error as e:
                messagebox.showerror("Erro", f"Erro ao visualizar aulas: {e}")
            finally:
                cursor.close()
                connection.close()

    # Criar a janela para gerenciamento de aulas
    janela_aulas = tk.Toplevel(root)
    janela_aulas.title("Gerenciar Aulas")
    janela_aulas.geometry("1000x300")

    btn_adicionar = tk.Button(janela_aulas, text="Adicionar Aula", command=adicionar_aula)
    btn_adicionar.pack(pady=10)

    btn_visualizar = tk.Button(janela_aulas, text="Visualizar Aulas", command=visualizar_aulas)
    btn_visualizar.pack(pady=10)


def gerenciar_usuarios():
    def adicionar_usuario():
        nome = simpledialog.askstring("Entrada", "Nome do Usuário:")
        username = simpledialog.askstring("Entrada", "Username do Usuário:")
        senha = simpledialog.askstring("Entrada", "Senha do Usuário:")

        if nome and username and senha:
            connection = conectar()
            if connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute("""
                        INSERT INTO tbl_usuarios (usu_nome, usu_username, usu_senha)
                        VALUES (%s, %s, %s)
                    """, (nome, username, senha))
                    connection.commit()
                    messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
                except Error as e:
                    messagebox.showerror("Erro", f"Erro ao adicionar usuário: {e}")
                finally:
                    cursor.close()
                    connection.close()

    def visualizar_usuarios():
        connection = conectar()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM tbl_usuarios")
                result = cursor.fetchall()
                if result:
                    texto = "\n".join([f"Nome: {row[0]}, Username: {row[1]}" for row in result])
                    messagebox.showinfo("Usuários", texto)
                else:
                    messagebox.showinfo("Usuários", "Nenhum usuário encontrado.")
            except Error as e:
                messagebox.showerror("Erro", f"Erro ao visualizar usuários: {e}")
            finally:
                cursor.close()
                connection.close()

    # Criar a janela para gerenciamento de usuários
    janela_usuarios = tk.Toplevel(root)
    janela_usuarios.title("Gerenciar Usuários")
    janela_usuarios.geometry("1000x500")

    btn_adicionar = tk.Button(janela_usuarios, text="Adicionar Usuário", command=adicionar_usuario)
    btn_adicionar.pack(pady=10)

    btn_visualizar = tk.Button(janela_usuarios, text="Visualizar Usuários", command=visualizar_usuarios)
    btn_visualizar.pack(pady=10)


# Criação da janela principal
root = tk.Tk()
root.title("Sistema de Gerenciamento")
root.geometry("1000x600")

# Criação do menu
menu_bar = tk.Menu(root)

# Menu "Cidades"
menu_cidades = tk.Menu(menu_bar, tearoff=0)
menu_cidades.add_command(label="Gerenciar Cidades", command=gerenciar_cidades)
menu_bar.add_cascade(label="Cidades", menu=menu_cidades)

# Menu "Cursos"
menu_cursos = tk.Menu(menu_bar, tearoff=0)
menu_cursos.add_command(label="Gerenciar Cursos", command=gerenciar_cursos)
menu_bar.add_cascade(label="Cursos", menu=menu_cursos)

# Menu "Professores"
menu_professores = tk.Menu(menu_bar, tearoff=0)
menu_professores.add_command(label="Gerenciar Professores", command=gerenciar_professores)
menu_bar.add_cascade(label="Professores", menu=menu_professores)

# Menu "Alunos"
menu_alunos = tk.Menu(menu_bar, tearoff=0)
menu_alunos.add_command(label="Gerenciar Alunos", command=gerenciar_alunos)
menu_bar.add_cascade(label="Alunos", menu=menu_alunos)

# Menu "Aulas"
menu_aulas = tk.Menu(menu_bar, tearoff=0)
menu_aulas.add_command(label="Gerenciar Aulas", command=gerenciar_aulas)
menu_bar.add_cascade(label="Aulas", menu=menu_aulas)

# Menu "Usuário"
menu_usuario = tk.Menu(menu_bar, tearoff=0)
menu_usuario.add_command(label="Gerenciar Usuários", command=gerenciar_usuarios)
menu_bar.add_cascade(label="Usuário", menu=menu_usuario)

# Menu "Arquivo" para sair
menu_arquivo = tk.Menu(menu_bar, tearoff=0)
menu_arquivo.add_command(label="Sair", command=root.quit)
menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)

# Configurar a barra de menus
root.config(menu=menu_bar)

# Rodar a janela principal
root.mainloop()
