from database import conectar

def listar_corretores():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        id_corretor,
        nome,
        creci,
        telefone,
        email
    FROM Corretor
    """

    cursor.execute(sql)
    dados = cursor.fetchall()

    for corretor in dados:
        print(corretor)

    cursor.close()
    conexao.close()


def cadastrar_corretor(nome, creci, telefone, email):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO Corretor
    (nome, creci, telefone, email)
    VALUES
    (%s, %s, %s, %s)
    """

    valores = (
        nome,
        creci,
        telefone,
        email
    )

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Corretor {nome} cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def atualizar_corretor(id_corretor, nome, creci, telefone, email):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE Corretor
    SET
        nome = %s,
        creci = %s,
        telefone = %s,
        email = %s
    WHERE id_corretor = %s
    """

    valores = (
        nome,
        creci,
        telefone,
        email,
        id_corretor
    )

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Corretor {id_corretor} atualizado com sucesso!")

    cursor.close()
    conexao.close()


def deletar_corretor(id_corretor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    DELETE FROM Corretor
    WHERE id_corretor = %s
    """

    cursor.execute(sql, (id_corretor,))
    conexao.commit()

    print(f"Corretor {id_corretor} deletado com sucesso!")

    cursor.close()
    conexao.close()