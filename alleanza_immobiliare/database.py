import os
import mysql.connector
from dotenv import load_dotenv


load_dotenv()

def conectar():
    
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")
    port = os.getenv("DB_PORT")

    conn_kwargs = dict(
        host=host,
        user=user,
        password=password,
        database=database,
    )

    if port:
        try:
            conn_kwargs["port"] = int(port)
        except ValueError:
            raise ValueError("DB_PORT deve ser um número inteiro")

    ssl_ca = os.getenv("DB_SSL_CA")
    if ssl_ca:
        conn_kwargs["ssl_ca"] = ssl_ca

    try:
        conexao = mysql.connector.connect(**conn_kwargs)
    except mysql.connector.Error as err:
        raise Exception(f"Erro ao conectar ao banco de dados: {err}")

    return conexao