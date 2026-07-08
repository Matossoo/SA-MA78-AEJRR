from database import conectar

def listar_imovel_documentos():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        id_imovel_documento,
        id_imovel,
        id_documento,
        data_arquivamento
    FROM ImovelDocumento
    """

    cursor.execute(sql)

    dados = cursor.fetchall()

    for documento in dados:
        print(documento)

    cursor.close()
    conexao.close()


def cadastrar_imovel_documento(id_imovel,id_documento,data_arquivamento):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO ImovelDocumento
    (id_imovel,id_documento,data_arquivamento)
    VALUES
    (%s,%s,%s)
    """

    cursor.execute(sql,(id_imovel,id_documento,data_arquivamento))
    conexao.commit()

    print("Documento vinculado ao imóvel!")

    cursor.close()
    conexao.close()


def atualizar_imovel_documento(id_imovel_documento,id_imovel,id_documento,data_arquivamento):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE ImovelDocumento
    SET
        id_imovel=%s,
        id_documento=%s,
        data_arquivamento=%s
    WHERE id_imovel_documento=%s
    """

    cursor.execute(sql,(id_imovel,id_documento,data_arquivamento,id_imovel_documento))
    conexao.commit()

    print("Registro atualizado!")

    cursor.close()
    conexao.close()


def deletar_imovel_documento(id_imovel_documento):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    DELETE FROM ImovelDocumento
    WHERE id_imovel_documento=%s
    """

    cursor.execute(sql,(id_imovel_documento,))
    conexao.commit()

    print("Registro removido!")

    cursor.close()
    conexao.close()