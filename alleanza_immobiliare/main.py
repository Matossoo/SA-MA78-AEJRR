from endereco_model import *
from proprietario_model import *
from cliente_model import *
from corretor_model import *
from tipo_imovel_model import *
from documento_model import *
from imovel_model import *
from visita_model import *
from venda_model import *
from aluguel_model import *
from contrato_model import *
from pagamento_model import *
from imovel_documento_model import *
from anuncio_model import *
from foto_imovel_model import *

while True:

    print("\n========================================")
    print("      ALLEANZA IMMOBILIARE")
    print("========================================")
    print("1  - Endereço")
    print("2  - Proprietário")
    print("3  - Cliente")
    print("4  - Corretor")
    print("5  - Tipo de Imóvel")
    print("6  - Documento")
    print("7  - Imóvel")
    print("8  - Visita")
    print("9  - Venda")
    print("10 - Aluguel")
    print("11 - Contrato")
    print("12 - Pagamento")
    print("13 - Imóvel Documento")
    print("14 - Anúncio")
    print("15 - Foto Imóvel")
    print("0  - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "0":
        print("Sistema encerrado.")
        break

#==================================================
# ENDEREÇO
#==================================================

    elif opcao == "1":

        while True:

            print("\n===== ENDEREÇO =====")
            print("1 - Listar")
            print("2 - Cadastrar")
            print("3 - Atualizar")
            print("4 - Deletar")
            print("0 - Voltar")

            escolha = input("Escolha: ")

            if escolha == "1":
                listar_enderecos()

            elif escolha == "2":

                rua = input("Rua: ")
                numero = input("Número: ")
                bairro = input("Bairro: ")
                cidade = input("Cidade: ")
                estado = input("Estado: ")
                cep = input("CEP: ")

                cadastrar_endereco(
                    rua,
                    numero,
                    bairro,
                    cidade,
                    estado,
                    cep
                )

            elif escolha == "3":

                id_endereco = int(input("ID: "))
                rua = input("Rua: ")
                numero = input("Número: ")
                bairro = input("Bairro: ")
                cidade = input("Cidade: ")
                estado = input("Estado: ")
                cep = input("CEP: ")

                atualizar_endereco(
                    id_endereco,
                    rua,
                    numero,
                    bairro,
                    cidade,
                    estado,
                    cep
                )

            elif escolha == "4":

                id_endereco = int(input("ID: "))

                deletar_endereco(id_endereco)

            elif escolha == "0":
                break

#==================================================
# PROPRIETÁRIO
#==================================================

    elif opcao == "2":

        while True:

            print("\n===== PROPRIETÁRIO =====")
            print("1 - Listar")
            print("2 - Cadastrar")
            print("3 - Atualizar")
            print("4 - Deletar")
            print("0 - Voltar")

            escolha = input("Escolha: ")

            if escolha == "1":
                listar_proprietarios()

            elif escolha == "2":

                nome = input("Nome: ")
                cpf = input("CPF/CNPJ: ")
                telefone = input("Telefone: ")
                email = input("Email: ")

                cadastrar_proprietario(
                    nome,
                    cpf,
                    telefone,
                    email
                )

            elif escolha == "3":

                id_proprietario = int(input("ID: "))
                nome = input("Nome: ")
                cpf = input("CPF/CNPJ: ")
                telefone = input("Telefone: ")
                email = input("Email: ")

                atualizar_proprietario(
                    id_proprietario,
                    nome,
                    cpf,
                    telefone,
                    email
                )

            elif escolha == "4":

                id_proprietario = int(input("ID: "))

                deletar_proprietario(id_proprietario)

            elif escolha == "0":
                break

#==================================================
# CLIENTE
#==================================================

    elif opcao == "3":

        while True:

            print("\n===== CLIENTE =====")
            print("1 - Listar")
            print("2 - Cadastrar")
            print("3 - Atualizar")
            print("4 - Deletar")
            print("0 - Voltar")

            escolha = input("Escolha: ")

            if escolha == "1":
                listar_clientes()

            elif escolha == "2":

                nome = input("Nome: ")
                cpf = input("CPF: ")
                telefone = input("Telefone: ")
                email = input("Email: ")

                cadastrar_cliente(
                    nome,
                    cpf,
                    telefone,
                    email
                )

            elif escolha == "3":

                id_cliente = int(input("ID: "))
                nome = input("Nome: ")
                cpf = input("CPF: ")
                telefone = input("Telefone: ")
                email = input("Email: ")

                atualizar_cliente(
                    id_cliente,
                    nome,
                    cpf,
                    telefone,
                    email
                )

            elif escolha == "4":

                id_cliente = int(input("ID: "))

                deletar_cliente(id_cliente)

            elif escolha == "0":
                break
            #==================================================
# CORRETOR
#==================================================

    elif opcao == "4":

        while True:

            print("\n===== CORRETOR =====")
            print("1 - Listar")
            print("2 - Cadastrar")
            print("3 - Atualizar")
            print("4 - Deletar")
            print("0 - Voltar")

            escolha = input("Escolha: ")

            if escolha == "1":
                listar_corretores()

            elif escolha == "2":

                nome = input("Nome: ")
                creci = input("CRECI: ")
                telefone = input("Telefone: ")
                email = input("Email: ")

                cadastrar_corretor(
                    nome,
                    creci,
                    telefone,
                    email
                )

            elif escolha == "3":

                id_corretor = int(input("ID: "))
                nome = input("Nome: ")
                creci = input("CRECI: ")
                telefone = input("Telefone: ")
                email = input("Email: ")

                atualizar_corretor(
                    id_corretor,
                    nome,
                    creci,
                    telefone,
                    email
                )

            elif escolha == "4":

                id_corretor = int(input("ID: "))
                deletar_corretor(id_corretor)

            elif escolha == "0":
                break

#==================================================
# TIPO DE IMÓVEL
#==================================================

    elif opcao == "5":

        while True:

            print("\n===== TIPO DE IMÓVEL =====")
            print("1 - Listar")
            print("2 - Cadastrar")
            print("3 - Atualizar")
            print("4 - Deletar")
            print("0 - Voltar")

            escolha = input("Escolha: ")

            if escolha == "1":
                listar_tipos_imovel()

            elif escolha == "2":

                descricao = input("Descrição: ")

                cadastrar_tipo_imovel(descricao)

            elif escolha == "3":

                id_tipo = int(input("ID: "))
                descricao = input("Descrição: ")

                atualizar_tipo_imovel(
                    id_tipo,
                    descricao
                )

            elif escolha == "4":

                id_tipo = int(input("ID: "))
                deletar_tipo_imovel(id_tipo)

            elif escolha == "0":
                break

#==================================================
# DOCUMENTO
#==================================================

    elif opcao == "6":

        while True:

            print("\n===== DOCUMENTO =====")
            print("1 - Listar")
            print("2 - Cadastrar")
            print("3 - Atualizar")
            print("4 - Deletar")
            print("0 - Voltar")

            escolha = input("Escolha: ")

            if escolha == "1":
                listar_documentos()

            elif escolha == "2":

                nome = input("Nome do documento: ")
                tipo = input("Tipo: ")

                cadastrar_documento(
                    nome,
                    tipo
                )

            elif escolha == "3":

                id_documento = int(input("ID: "))
                nome = input("Nome do documento: ")
                tipo = input("Tipo: ")

                atualizar_documento(
                    id_documento,
                    nome,
                    tipo
                )

            elif escolha == "4":

                id_documento = int(input("ID: "))
                deletar_documento(id_documento)

            elif escolha == "0":
                break

#==================================================
# IMÓVEL
#==================================================

    elif opcao == "7":

        while True:

            print("\n===== IMÓVEL =====")
            print("1 - Listar")
            print("2 - Cadastrar")
            print("3 - Atualizar")
            print("4 - Deletar")
            print("0 - Voltar")

            escolha = input("Escolha: ")

            if escolha == "1":
                listar_imoveis()

            elif escolha == "2":

                id_proprietario = int(input("ID Proprietário: "))
                id_tipo = int(input("ID Tipo Imóvel: "))
                id_endereco = int(input("ID Endereço: "))
                valor = float(input("Valor sugerido: "))
                status = input("Status: ")

                cadastrar_imovel(
                    id_proprietario,
                    id_tipo,
                    id_endereco,
                    valor,
                    status
                )

            elif escolha == "3":

                id_imovel = int(input("ID Imóvel: "))
                id_proprietario = int(input("ID Proprietário: "))
                id_tipo = int(input("ID Tipo Imóvel: "))
                id_endereco = int(input("ID Endereço: "))
                valor = float(input("Valor sugerido: "))
                status = input("Status: ")

                atualizar_imovel(
                    id_imovel,
                    id_proprietario,
                    id_tipo,
                    id_endereco,
                    valor,
                    status
                )

            elif escolha == "4":

                id_imovel = int(input("ID Imóvel: "))
                deletar_imovel(id_imovel)

            elif escolha == "0":
                break
            #==================================================
# VISITA
#==================================================

    elif opcao == "8":

        while True:

            print("\n===== VISITA =====")
            print("1 - Listar")
            print("2 - Cadastrar")
            print("3 - Atualizar")
            print("4 - Deletar")
            print("0 - Voltar")

            escolha = input("Escolha: ")

            if escolha == "1":
                listar_visitas()

            elif escolha == "2":

                id_cliente = int(input("ID Cliente: "))
                id_corretor = int(input("ID Corretor: "))
                id_imovel = int(input("ID Imóvel: "))
                data = input("Data e Hora (AAAA-MM-DD HH:MM:SS): ")
                observacoes = input("Observações: ")

                cadastrar_visita(
                    id_cliente,
                    id_corretor,
                    id_imovel,
                    data,
                    observacoes
                )

            elif escolha == "3":

                id_visita = int(input("ID Visita: "))
                id_cliente = int(input("ID Cliente: "))
                id_corretor = int(input("ID Corretor: "))
                id_imovel = int(input("ID Imóvel: "))
                data = input("Data e Hora: ")
                observacoes = input("Observações: ")

                atualizar_visita(
                    id_visita,
                    id_cliente,
                    id_corretor,
                    id_imovel,
                    data,
                    observacoes
                )

            elif escolha == "4":

                id_visita = int(input("ID Visita: "))
                deletar_visita(id_visita)

            elif escolha == "0":
                break

#==================================================
# VENDA
#==================================================

    elif opcao == "9":

        while True:

            print("\n===== VENDA =====")
            print("1 - Listar")
            print("2 - Cadastrar")
            print("3 - Atualizar")
            print("4 - Deletar")
            print("0 - Voltar")

            escolha = input("Escolha: ")

            if escolha == "1":
                listar_vendas()

            elif escolha == "2":

                id_cliente = int(input("ID Cliente: "))
                id_corretor = int(input("ID Corretor: "))
                id_imovel = int(input("ID Imóvel: "))
                data = input("Data da Venda (AAAA-MM-DD): ")
                valor = float(input("Valor da Venda: "))

                cadastrar_venda(
                    id_cliente,
                    id_corretor,
                    id_imovel,
                    data,
                    valor
                )

            elif escolha == "3":

                id_venda = int(input("ID Venda: "))
                id_cliente = int(input("ID Cliente: "))
                id_corretor = int(input("ID Corretor: "))
                id_imovel = int(input("ID Imóvel: "))
                data = input("Data da Venda: ")
                valor = float(input("Valor da Venda: "))

                atualizar_venda(
                    id_venda,
                    id_cliente,
                    id_corretor,
                    id_imovel,
                    data,
                    valor
                )

            elif escolha == "4":

                id_venda = int(input("ID Venda: "))
                deletar_venda(id_venda)

            elif escolha == "0":
                break

#==================================================
# ALUGUEL
#==================================================

    elif opcao == "10":

        while True:

            print("\n===== ALUGUEL =====")
            print("1 - Listar")
            print("2 - Cadastrar")
            print("3 - Atualizar")
            print("4 - Deletar")
            print("0 - Voltar")

            escolha = input("Escolha: ")

            if escolha == "1":
                listar_alugueis()

            elif escolha == "2":

                id_cliente = int(input("ID Cliente: "))
                id_corretor = int(input("ID Corretor: "))
                id_imovel = int(input("ID Imóvel: "))
                data = input("Data de Início (AAAA-MM-DD): ")
                valor = float(input("Valor do Aluguel: "))

                cadastrar_aluguel(
                    id_cliente,
                    id_corretor,
                    id_imovel,
                    data,
                    valor
                )

            elif escolha == "3":

                id_aluguel = int(input("ID Aluguel: "))
                id_cliente = int(input("ID Cliente: "))
                id_corretor = int(input("ID Corretor: "))
                id_imovel = int(input("ID Imóvel: "))
                data = input("Data de Início: ")
                valor = float(input("Valor do Aluguel: "))

                atualizar_aluguel(
                    id_aluguel,
                    id_cliente,
                    id_corretor,
                    id_imovel,
                    data,
                    valor
                )

            elif escolha == "4":

                id_aluguel = int(input("ID Aluguel: "))
                deletar_aluguel(id_aluguel)

            elif escolha == "0":
                break
            #==================================================
# CONTRATO
#==================================================

    elif opcao == "11":

        while True:

            print("\n===== CONTRATO =====")
            print("1 - Listar")
            print("2 - Cadastrar")
            print("3 - Atualizar")
            print("4 - Deletar")
            print("0 - Voltar")

            escolha = input("Escolha: ")

            if escolha == "1":
                listar_contratos()

            elif escolha == "2":

                id_cliente = int(input("ID Cliente: "))
                id_imovel = int(input("ID Imóvel: "))
                tipo = input("Tipo contrato: ")
                data = input("Data (AAAA-MM-DD): ")

                cadastrar_contrato(
                    id_cliente,
                    id_imovel,
                    tipo,
                    data
                )

            elif escolha == "3":

                id_contrato = int(input("ID Contrato: "))
                id_cliente = int(input("ID Cliente: "))
                id_imovel = int(input("ID Imóvel: "))
                tipo = input("Tipo contrato: ")
                data = input("Data: ")

                atualizar_contrato(
                    id_contrato,
                    id_cliente,
                    id_imovel,
                    tipo,
                    data
                )

            elif escolha == "4":

                id_contrato = int(input("ID Contrato: "))
                deletar_contrato(id_contrato)

            elif escolha == "0":
                break


#==================================================
# PAGAMENTO
#==================================================

    elif opcao == "12":

        while True:

            print("\n===== PAGAMENTO =====")
            print("1 - Listar")
            print("2 - Cadastrar")
            print("3 - Atualizar")
            print("4 - Deletar")
            print("0 - Voltar")

            escolha = input("Escolha: ")

            if escolha == "1":
                listar_pagamentos()

            elif escolha == "2":

                id_contrato = int(input("ID Contrato: "))
                valor = float(input("Valor: "))
                data = input("Data pagamento: ")
                metodo = input("Método pagamento: ")

                cadastrar_pagamento(
                    id_contrato,
                    valor,
                    data,
                    metodo
                )

            elif escolha == "3":

                id_pagamento = int(input("ID Pagamento: "))
                id_contrato = int(input("ID Contrato: "))
                valor = float(input("Valor: "))
                data = input("Data: ")
                metodo = input("Método: ")

                atualizar_pagamento(
                    id_pagamento,
                    id_contrato,
                    valor,
                    data,
                    metodo
                )

            elif escolha == "4":

                id_pagamento = int(input("ID Pagamento: "))
                deletar_pagamento(id_pagamento)

            elif escolha == "0":
                break



#==================================================
# IMÓVEL DOCUMENTO
#==================================================

    elif opcao == "13":

        while True:

            print("\n===== IMÓVEL DOCUMENTO =====")
            print("1 - Listar")
            print("2 - Cadastrar")
            print("3 - Deletar")
            print("0 - Voltar")

            escolha = input("Escolha: ")


            if escolha == "1":
                listar_imovel_documentos()


            elif escolha == "2":

                id_imovel = int(input("ID Imóvel: "))
                id_documento = int(input("ID Documento: "))

                cadastrar_imovel_documento(
                    id_imovel,
                    id_documento
                )


            elif escolha == "3":

                id = int(input("ID: "))

                deletar_imovel_documento(id)


            elif escolha == "0":
                break



#==================================================
# ANÚNCIO
#==================================================

    elif opcao == "14":

        while True:

            print("\n===== ANÚNCIO =====")
            print("1 - Listar")
            print("2 - Cadastrar")
            print("3 - Atualizar")
            print("4 - Deletar")
            print("0 - Voltar")

            escolha = input("Escolha: ")


            if escolha == "1":
                listar_anuncios()


            elif escolha == "2":

                id_imovel = int(input("ID Imóvel: "))
                descricao = input("Descrição: ")
                data = input("Data anúncio: ")

                cadastrar_anuncio(
                    id_imovel,
                    descricao,
                    data
                )


            elif escolha == "3":

                id_anuncio = int(input("ID Anúncio: "))
                descricao = input("Descrição: ")
                data = input("Data: ")

                atualizar_anuncio(
                    id_anuncio,
                    descricao,
                    data
                )


            elif escolha == "4":

                id_anuncio = int(input("ID Anúncio: "))

                deletar_anuncio(id_anuncio)


            elif escolha == "0":
                break



#==================================================
# FOTO IMÓVEL
#==================================================

    elif opcao == "15":

        while True:

            print("\n===== FOTO IMÓVEL =====")
            print("1 - Listar")
            print("2 - Cadastrar")
            print("3 - Deletar")
            print("0 - Voltar")


            escolha = input("Escolha: ")


            if escolha == "1":

                listar_fotos()


            elif escolha == "2":

                id_imovel = int(input("ID Imóvel: "))
                caminho = input("Caminho da foto: ")

                cadastrar_foto(
                    id_imovel,
                    caminho
                )


            elif escolha == "3":

                id_foto = int(input("ID Foto: "))

                deletar_foto(id_foto)


            elif escolha == "0":
                break