import mysql.connector
from mysql.connector import Error

try:
    # Tentativa de conexão com o banco de dados MySQL
    connection = mysql.connector.connect(
        host='localhost',
        database='dbescola',
        user='tiao',
        password='123456'
    )

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print(f"Conectado ao servidor MySQL versão {db_Info}")
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print(f"Conectado ao banco de dados: {record}")

except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")
    connection = None

finally:

    if connection and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão com o MySQL encerrada")
