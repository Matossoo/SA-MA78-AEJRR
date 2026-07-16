import mysql.connector

from database import conectar
from table_utils import imprimir_tabela

def listar_pagamentos():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        p.id_pagamento,
        p.id_contrato,
        p.valor_pago,
        p.data_pagamento,
        p.forma_pagamento,
        p.status_pagamento,
        p.data_vencimento
    FROM Pagamento p
    """

    cursor.execute(sql)
    imprimir_tabela(cursor, titulo="PAGAMENTOS", campos_moeda=["valor_pago"])

    cursor.close()
    conexao.close()


STATUS_PAGAMENTO_VALIDOS = ('Pago', 'Pendente', 'Atrasado', 'Cancelado')


def cadastrar_pagamento(id_contrato, valor_pago, data_pagamento, forma_pagamento, status_pagamento, data_vencimento):

    if status_pagamento not in STATUS_PAGAMENTO_VALIDOS:
        print(f"\n❌ Status inválido! Use um dos valores: {', '.join(STATUS_PAGAMENTO_VALIDOS)}")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO Pagamento
    (id_contrato,valor_pago,data_pagamento,forma_pagamento,status_pagamento,data_vencimento)
    VALUES
    (%s,%s,%s,%s,%s,%s)
    """

    valores = (
        id_contrato,
        valor_pago,
        data_pagamento,
        forma_pagamento,
        status_pagamento,
        data_vencimento
    )

    cursor.execute(sql,valores)
    conexao.commit()

    print("Pagamento cadastrado!")

    cursor.close()
    conexao.close()


def atualizar_pagamento(id_pagamento, id_contrato, valor_pago, data_pagamento, forma_pagamento, status_pagamento, data_vencimento):
    if status_pagamento not in STATUS_PAGAMENTO_VALIDOS:
        print(f"\n❌ Status inválido! Use um dos valores: {', '.join(STATUS_PAGAMENTO_VALIDOS)}")
        return
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """UPDATE Pagamento 
                 SET id_contrato=%s, valor_pago=%s, data_pagamento=%s, forma_pagamento=%s, status_pagamento=%s, data_vencimento=%s 
                 WHERE id_pagamento=%s"""
        cursor.execute(sql, (id_contrato, valor_pago, data_pagamento, forma_pagamento, status_pagamento, data_vencimento, id_pagamento))
        conexao.commit()
        print("\n✅ Pagamento atualizado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Erro: O ID de contrato especificado não existe!")
    finally:
        cursor.close()
        conexao.close()


def deletar_pagamento(id_pagamento):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "DELETE FROM Pagamento WHERE id_pagamento = %s"
        cursor.execute(sql, (id_pagamento,))
        conexao.commit()
        print("\n✅ Registro de pagamento deletado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Erro ao deletar pagamento devido a uma restrição de integridade.")
    finally:
        cursor.close()
        conexao.close()