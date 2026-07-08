from database import conectar

def listar_contratos():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        id_contrato,
        id_venda,
        id_aluguel,
        data_assinatura,
        clausulas
    FROM Contrato
    """

    cursor.execute(sql)
    dados = cursor.fetchall()

    for contrato in dados:
        print(contrato)

    cursor.close()
    conexao.close()


def cadastrar_contrato(id_venda, id_aluguel, data_assinatura, clausulas):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO Contrato
    (id_venda,id_aluguel,data_assinatura,clausulas)
    VALUES
    (%s,%s,%s,%s)
    """

    valores = (
        id_venda,
        id_aluguel,
        data_assinatura,
        clausulas
    )

    cursor.execute(sql, valores)
    conexao.commit()

    print("Contrato cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def atualizar_contrato(id_contrato,id_venda,id_aluguel,data_assinatura,clausulas):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE Contrato
    SET
        id_venda=%s,
        id_aluguel=%s,
        data_assinatura=%s,
        clausulas=%s
    WHERE id_contrato=%s
    """

    valores = (
        id_venda,
        id_aluguel,
        data_assinatura,
        clausulas,
        id_contrato
    )

    cursor.execute(sql,valores)
    conexao.commit()

    print("Contrato atualizado com sucesso!")

    cursor.close()
    conexao.close()


def deletar_contrato(id_contrato):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    DELETE FROM Contrato
    WHERE id_contrato=%s
    """

    cursor.execute(sql,(id_contrato,))
    conexao.commit()

    print("Contrato removido com sucesso!")

    cursor.close()
    conexao.close()