from database import conectar

def listar_proprietarios():
    # abrir conexão
    conexao = conectar()

    # criar cursor
    cursor = conexao.cursor()

    # sql da consulta
    sql = """
    SELECT
        id_proprietario,
        nome,
        cpf_cnpj,
        telefone,
        email
    FROM Proprietario
    """

    # executa sql
    cursor.execute(sql)

    # recuperar dados
    dados = cursor.fetchall()

    # exibir dados
    for proprietario in dados:
        print(proprietario)

    # fechar conexão
    cursor.close()
    conexao.close()


def cadastrar_proprietario(nome, cpf_cnpj, telefone, email):
    # abrir conexão
    conexao = conectar()

    # criar cursor
    cursor = conexao.cursor()

    # sql de inserção
    sql = """
    INSERT INTO Proprietario
    (nome, cpf_cnpj, telefone, email)
    VALUES
    (%s, %s, %s, %s)
    """

    valores = (
        nome,
        cpf_cnpj,
        telefone,
        email
    )

    # executa sql
    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Proprietário {nome} cadastrado com sucesso!")

    # fechar conexão
    cursor.close()
    conexao.close()


def atualizar_proprietario(id_proprietario, nome, cpf_cnpj, telefone, email):
    # abrir conexão
    conexao = conectar()

    # criar cursor
    cursor = conexao.cursor()

    # sql de atualização
    sql = """
    UPDATE Proprietario
    SET
        nome = %s,
        cpf_cnpj = %s,
        telefone = %s,
        email = %s
    WHERE id_proprietario = %s
    """

    valores = (
        nome,
        cpf_cnpj,
        telefone,
        email,
        id_proprietario
    )

    # executa sql
    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Proprietário {id_proprietario} atualizado com sucesso!")

    # fechar conexão
    cursor.close()
    conexao.close()


def deletar_proprietario(id_proprietario):
    # abrir conexão
    conexao = conectar()

    # criar cursor
    cursor = conexao.cursor()

    # sql de exclusão
    sql = """
    DELETE FROM Proprietario
    WHERE id_proprietario = %s
    """

    valores = (id_proprietario,)

    # executa sql
    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Proprietário {id_proprietario} deletado com sucesso!")

    # fechar conexão
    cursor.close()
    conexao.close()