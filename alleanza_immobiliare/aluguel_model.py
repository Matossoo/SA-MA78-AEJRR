from database import conectar

def listar_alugueis():

    conexao=conectar()
    cursor=conexao.cursor()

    sql="""
    SELECT
        a.id_aluguel,
        c.nome,
        co.nome,
        i.id_imovel,
        a.data_inicio,
        a.valor_aluguel
    FROM Aluguel a
    JOIN Cliente c ON a.id_cliente=c.id_cliente
    JOIN Corretor co ON a.id_corretor=co.id_corretor
    JOIN Imovel i ON a.id_imovel=i.id_imovel
    """

    cursor.execute(sql)
    dados=cursor.fetchall()

    for aluguel in dados:
        print(aluguel)

    cursor.close()
    conexao.close()


def cadastrar_aluguel(id_cliente,id_corretor,id_imovel,data_inicio,valor_aluguel):

    conexao=conectar()
    cursor=conexao.cursor()

    sql="""
    INSERT INTO Aluguel
    (id_cliente,id_corretor,id_imovel,data_inicio,valor_aluguel)
    VALUES
    (%s,%s,%s,%s,%s)
    """

    valores=(
        id_cliente,
        id_corretor,
        id_imovel,
        data_inicio,
        valor_aluguel
    )

    cursor.execute(sql,valores)
    conexao.commit()

    print("Aluguel cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def atualizar_aluguel(id_aluguel,id_cliente,id_corretor,id_imovel,data_inicio,valor_aluguel):

    conexao=conectar()
    cursor=conexao.cursor()

    sql="""
    UPDATE Aluguel
    SET
        id_cliente=%s,
        id_corretor=%s,
        id_imovel=%s,
        data_inicio=%s,
        valor_aluguel=%s
    WHERE id_aluguel=%s
    """

    valores=(
        id_cliente,
        id_corretor,
        id_imovel,
        data_inicio,
        valor_aluguel,
        id_aluguel
    )

    cursor.execute(sql,valores)
    conexao.commit()

    print(f"Aluguel {id_aluguel} atualizado!")

    cursor.close()
    conexao.close()


def deletar_aluguel(id_aluguel):

    conexao=conectar()
    cursor=conexao.cursor()

    sql="""
    DELETE FROM Aluguel
    WHERE id_aluguel=%s
    """

    cursor.execute(sql,(id_aluguel,))
    conexao.commit()

    print(f"Aluguel {id_aluguel} deletado!")

    cursor.close()
    conexao.close()