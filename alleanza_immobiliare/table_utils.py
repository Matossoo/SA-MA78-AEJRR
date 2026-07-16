"""
Utilitário compartilhado para exibir resultados de consultas em forma de
tabela bonita e organizada no terminal (em vez de tuplas cruas soltas na
tela). Usa a biblioteca `tabulate`.
"""

from datetime import date, datetime
from decimal import Decimal

from tabulate import tabulate


def _formatar_valor(valor):
    """Formata cada valor individualmente para ficar mais legível."""
    if valor is None:
        return "-"
    if isinstance(valor, Decimal):
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    if isinstance(valor, datetime):
        return valor.strftime("%d/%m/%Y %H:%M")
    if isinstance(valor, date):
        return valor.strftime("%d/%m/%Y")
    if isinstance(valor, bool):
        return "Sim" if valor else "Não"
    return valor


def _formatar_cabecalho(nome_coluna):
    """Transforma nomes de coluna do banco (snake_case) em títulos legíveis."""
    apelidos = {
        "id": "ID",
        "cpf": "CPF",
        "cnpj": "CNPJ",
        "cpf_cnpj": "CPF/CNPJ",
        "creci": "CRECI",
        "url": "URL",
        "imovel": "Imóvel",
        "imoveis": "Imóveis",
    }
    partes = nome_coluna.split("_")
    partes = [apelidos.get(p.lower(), p.capitalize()) for p in partes]
    return " ".join(partes)


def imprimir_tabela(cursor, titulo=None, campos_moeda=None):
    """
    Recebe um cursor já executado (cursor.execute(sql) já foi chamado),
    busca as linhas e imprime tudo formatado em tabela.

    - titulo: cabeçalho opcional exibido acima da tabela.
    - campos_moeda: lista de nomes de coluna (como vieram do SELECT) que
      devem ser formatados como valor monetário mesmo que o driver não
      retorne Decimal (ex.: quando vem de pandas/float).
    """
    colunas = [desc[0] for desc in cursor.description]
    linhas = cursor.fetchall()

    if titulo:
        print(f"\n{'═' * (len(titulo) + 4)}")
        print(f"  {titulo}")
        print(f"{'═' * (len(titulo) + 4)}")

    if not linhas:
        print("\n(nenhum registro encontrado)\n")
        return

    campos_moeda = set(campos_moeda or [])
    linhas_formatadas = []
    for linha in linhas:
        linha_fmt = []
        for nome_col, valor in zip(colunas, linha):
            if nome_col in campos_moeda and valor is not None and not isinstance(valor, Decimal):
                valor = Decimal(str(valor))
            linha_fmt.append(_formatar_valor(valor))
        linhas_formatadas.append(linha_fmt)

    cabecalhos = [_formatar_cabecalho(c) for c in colunas]

    print()
    print(tabulate(linhas_formatadas, headers=cabecalhos, tablefmt="fancy_grid", stralign="left", numalign="right"))
    print(f"\nTotal: {len(linhas)} registro(s)\n")
