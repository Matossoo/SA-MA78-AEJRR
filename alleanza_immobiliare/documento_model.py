from database import conectar

def listar_documentos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        id_documento,
        nome_documento,
        tipo
    FROM Documento
    """

    cursor.execute(sql)
    dados = cursor.fetchall()

    for documento in dados:
        print(documento)

    cursor.close()
    conexao.close()


def cadastrar_documento(nome_documento, tipo):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO Documento
    (nome_documento, tipo)
    VALUES
    (%s, %s)
    """

    valores = (
        nome_documento,
        tipo
    )

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Documento {nome_documento} cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def atualizar_documento(id_documento, nome_documento, tipo):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE Documento
    SET
        nome_documento = %s,
        tipo = %s
    WHERE id_documento = %s
    """

    valores = (
        nome_documento,
        tipo,
        id_documento
    )

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Documento {id_documento} atualizado com sucesso!")

    cursor.close()
    conexao.close()


def deletar_documento(id_documento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    DELETE FROM Documento
    WHERE id_documento = %s
    """

    cursor.execute(sql, (id_documento,))
    conexao.commit()

    print(f"Documento {id_documento} deletado com sucesso!")

    cursor.close()
    conexao.close()