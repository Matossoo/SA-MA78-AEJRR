from database import conectar

def listar_enderecos():
    # abrir conexão
    conexao = conectar()

    # criar cursor
    cursor = conexao.cursor()

    # sql da consulta
    sql = """
    SELECT
        id_endereco,
        rua,
        numero,
        bairro,
        cidade,
        estado,
        cep
    FROM Endereco
    """

    # executa sql
    cursor.execute(sql)

    # recuperar dados
    dados = cursor.fetchall()

    # exibir dados
    for endereco in dados:
        print(endereco)

    # fechar conexão
    cursor.close()
    conexao.close()


def cadastrar_endereco(rua, numero, bairro, cidade, estado, cep):

    # abrir conexão
    conexao = conectar()

    # criar cursor
    cursor = conexao.cursor()

    # sql de inserção
    sql = """
    INSERT INTO Endereco
    (rua, numero, bairro, cidade, estado, cep)
    VALUES
    (%s, %s, %s, %s, %s, %s)
    """

    valores = (
        rua,
        numero,
        bairro,
        cidade,
        estado,
        cep
    )

    # executa sql
    cursor.execute(sql, valores)
    conexao.commit()

    print("Endereço cadastrado com sucesso!")

    # fechar conexão
    cursor.close()
    conexao.close()


def atualizar_endereco(id_endereco, rua, numero, bairro, cidade, estado, cep):

    # abrir conexão
    conexao = conectar()

    # criar cursor
    cursor = conexao.cursor()

    # sql atualização
    sql = """
    UPDATE Endereco
    SET
        rua = %s,
        numero = %s,
        bairro = %s,
        cidade = %s,
        estado = %s,
        cep = %s
    WHERE id_endereco = %s
    """

    valores = (
        rua,
        numero,
        bairro,
        cidade,
        estado,
        cep,
        id_endereco
    )

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Endereço {id_endereco} atualizado com sucesso!")

    # fechar conexão
    cursor.close()
    conexao.close()


def deletar_endereco(id_endereco):

    # abrir conexão
    conexao = conectar()

    # criar cursor
    cursor = conexao.cursor()

    # sql exclusão
    sql = """
    DELETE FROM Endereco
    WHERE id_endereco = %s
    """

    valores = (id_endereco,)

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Endereço {id_endereco} deletado com sucesso!")

    # fechar conexão
    cursor.close()
    conexao.close()