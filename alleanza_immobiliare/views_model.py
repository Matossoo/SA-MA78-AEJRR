"""
Consulta das VIEWS do banco (criadas em BancoDeDados/05_Views.sql).

Cada view já resolve os JOINs necessários direto no banco; aqui a gente só
lista as opções disponíveis, deixa o usuário escolher qual quer consultar
e mostra o resultado formatado em tabela.
"""

import mysql.connector

from database import conectar
from table_utils import imprimir_tabela

# nome exibido no menu -> (nome da view no banco, título da tabela, colunas monetárias)
VIEWS_DISPONIVEIS = {
    "1": ("vw_imoveis_disponiveis", "IMÓVEIS DISPONÍVEIS", ["valor_sugerido"]),
    "2": ("vw_agenda_visitas", "AGENDA DE VISITAS", []),
    "3": ("vw_historico_vendas", "HISTÓRICO DE VENDAS", ["valor_venda"]),
    "4": ("vw_historico_alugueis", "HISTÓRICO DE ALUGUÉIS", ["valor_aluguel"]),
    "5": ("vw_pagamentos", "PAGAMENTOS REALIZADOS", ["valor_pago"]),
}


def consultar_view(nome_view, titulo, campos_moeda=None):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM {nome_view}")
        imprimir_tabela(cursor, titulo=titulo, campos_moeda=campos_moeda)
    except mysql.connector.Error as err:
        print(f"\n❌ Erro ao consultar a view '{nome_view}': {err}")
        print("   Verifique se o script BancoDeDados/05_Views.sql já foi executado no banco.")
    finally:
        cursor.close()
        conexao.close()


def menu_views():
    while True:
        print("\n===== CONSULTAR VIEWS 👁 =====")
        for chave, (_, titulo, _) in VIEWS_DISPONIVEIS.items():
            print(f"{chave} - {titulo.title()}")
        print("0 - Voltar ao Menu Principal")

        escolha = input("\nEscolha uma view: ")

        if escolha == "0":
            break
        elif escolha in VIEWS_DISPONIVEIS:
            nome_view, titulo, campos_moeda = VIEWS_DISPONIVEIS[escolha]
            consultar_view(nome_view, titulo, campos_moeda)
        else:
            print("\n❌ Opção inválida.")
