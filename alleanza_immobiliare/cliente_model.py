from database import conectar

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        id_cliente,
        nome,
        cpf,
        telefone,
        email
    FROM Cliente
    """

    cursor.execute(sql)
    dados = cursor.fetchall()

    for cliente in dados:
        print(cliente)

    cursor.close()
    conexao.close()


def cadastrar_cliente(nome, cpf, telefone, email):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO Cliente
    (nome, cpf, telefone, email)
    VALUES
    (%s, %s, %s, %s)
    """

    valores = (nome, cpf, telefone, email)

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Cliente {nome} cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def atualizar_cliente(id_cliente, nome, cpf, telefone, email):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE Cliente
    SET
        nome = %s,
        cpf = %s,
        telefone = %s,
        email = %s
    WHERE id_cliente = %s
    """

    valores = (
        nome,
        cpf,
        telefone,
        email,
        id_cliente
    )

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Cliente {id_cliente} atualizado com sucesso!")

    cursor.close()
    conexao.close()


def deletar_cliente(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    DELETE FROM Cliente
    WHERE id_cliente = %s
    """

    cursor.execute(sql, (id_cliente,))
    conexao.commit()

    print(f"Cliente {id_cliente} deletado com sucesso!")

    cursor.close()
    conexao.close()