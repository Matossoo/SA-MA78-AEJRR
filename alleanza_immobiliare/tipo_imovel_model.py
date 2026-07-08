from database import conectar

def listar_tipos_imovel():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        id_tipo_imovel,
        descricao
    FROM TipoImovel
    """

    cursor.execute(sql)
    dados = cursor.fetchall()

    for tipo in dados:
        print(tipo)

    cursor.close()
    conexao.close()


def cadastrar_tipo_imovel(descricao):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO TipoImovel
    (descricao)
    VALUES
    (%s)
    """

    cursor.execute(sql, (descricao,))
    conexao.commit()

    print("Tipo de imóvel cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def atualizar_tipo_imovel(id_tipo_imovel, descricao):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE TipoImovel
    SET
        descricao = %s
    WHERE id_tipo_imovel = %s
    """

    cursor.execute(sql, (descricao, id_tipo_imovel))
    conexao.commit()

    print(f"Tipo de imóvel {id_tipo_imovel} atualizado com sucesso!")

    cursor.close()
    conexao.close()


def deletar_tipo_imovel(id_tipo_imovel):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    DELETE FROM TipoImovel
    WHERE id_tipo_imovel = %s
    """

    cursor.execute(sql, (id_tipo_imovel,))
    conexao.commit()

    print(f"Tipo de imóvel {id_tipo_imovel} deletado com sucesso!")

    cursor.close()
    conexao.close()