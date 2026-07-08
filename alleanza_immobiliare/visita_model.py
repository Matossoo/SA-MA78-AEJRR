from database import conectar

def listar_visitas():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        v.id_visita,
        c.nome AS cliente,
        co.nome AS corretor,
        i.id_imovel,
        v.data_visita,
        v.observacoes
    FROM Visita v
    JOIN Cliente c ON v.id_cliente = c.id_cliente
    JOIN Corretor co ON v.id_corretor = co.id_corretor
    JOIN Imovel i ON v.id_imovel = i.id_imovel
    """

    cursor.execute(sql)
    dados = cursor.fetchall()

    for visita in dados:
        print(visita)

    cursor.close()
    conexao.close()


def cadastrar_visita(id_cliente, id_corretor, id_imovel, data_visita, observacoes):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO Visita
    (id_cliente,id_corretor,id_imovel,data_visita,observacoes)
    VALUES
    (%s,%s,%s,%s,%s)
    """

    valores = (
        id_cliente,
        id_corretor,
        id_imovel,
        data_visita,
        observacoes
    )

    cursor.execute(sql, valores)
    conexao.commit()

    print("Visita cadastrada com sucesso!")

    cursor.close()
    conexao.close()


def atualizar_visita(id_visita,id_cliente,id_corretor,id_imovel,data_visita,observacoes):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE Visita
    SET
        id_cliente=%s,
        id_corretor=%s,
        id_imovel=%s,
        data_visita=%s,
        observacoes=%s
    WHERE id_visita=%s
    """

    valores = (
        id_cliente,
        id_corretor,
        id_imovel,
        data_visita,
        observacoes,
        id_visita
    )

    cursor.execute(sql,valores)
    conexao.commit()

    print(f"Visita {id_visita} atualizada!")

    cursor.close()
    conexao.close()


def deletar_visita(id_visita):

    conexao=conectar()
    cursor=conexao.cursor()

    sql="""
    DELETE FROM Visita
    WHERE id_visita=%s
    """

    cursor.execute(sql,(id_visita,))
    conexao.commit()

    print(f"Visita {id_visita} deletada!")

    cursor.close()
    conexao.close()