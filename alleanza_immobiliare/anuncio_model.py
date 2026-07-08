from database import conectar

def listar_anuncios():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        id_anuncio,
        id_imovel,
        titulo,
        descricao,
        data_publicacao
    FROM Anuncio
    """

    cursor.execute(sql)

    dados = cursor.fetchall()

    for anuncio in dados:
        print(anuncio)

    cursor.close()
    conexao.close()


def cadastrar_anuncio(id_imovel,titulo,descricao,data_publicacao):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO Anuncio
    (id_imovel,titulo,descricao,data_publicacao)
    VALUES
    (%s,%s,%s,%s)
    """

    cursor.execute(sql,(id_imovel,titulo,descricao,data_publicacao))
    conexao.commit()

    print("Anúncio cadastrado!")

    cursor.close()
    conexao.close()


def atualizar_anuncio(id_anuncio,id_imovel,titulo,descricao,data_publicacao):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE Anuncio
    SET
        id_imovel=%s,
        titulo=%s,
        descricao=%s,
        data_publicacao=%s
    WHERE id_anuncio=%s
    """

    cursor.execute(sql,(id_imovel,titulo,descricao,data_publicacao,id_anuncio))
    conexao.commit()

    print("Anúncio atualizado!")

    cursor.close()
    conexao.close()


def deletar_anuncio(id_anuncio):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    DELETE FROM Anuncio
    WHERE id_anuncio=%s
    """

    cursor.execute(sql,(id_anuncio,))
    conexao.commit()

    print("Anúncio removido!")

    cursor.close()
    conexao.close()