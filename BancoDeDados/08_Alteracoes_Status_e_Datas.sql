-- ============================================
-- 08_Alteracoes_Status_e_Datas.sql
-- Adiciona status padronizados (ENUM) e datas de controle.
--
-- Correções feitas em relação ao script original enviado:
--   1) "Cliete" -> "Cliente" (nome da tabela estava com erro de digitação)
--   2) A tabela Imovel já possuia uma coluna "status" (texto livre) usada
--      em todo o sistema. Em vez de criar "status_imovel" duplicada, os
--      dados são migrados para o novo ENUM e a coluna antiga é removida.
--   3) Colunas NOT NULL não podem ser adicionadas "a seco" em tabelas que
--      já têm linhas (o MySQL recusa, pois não haveria valor para as
--      linhas existentes). Por isso cada coluna é: criada como NULL ->
--      preenchida (backfill) com um valor padrão coerente -> só então
--      marcada como NOT NULL.
--
-- Este script é seguro para rodar em um banco que já tem os dados de
-- 03_Inserts.sql. Rode-o uma única vez, na ordem em que está.
-- ============================================


-- ============================================
-- IMOVEL
-- ============================================
ALTER TABLE Imovel
    ADD COLUMN status_imovel ENUM ('Disponível','Reservado','Vendido','Alugado','Em negociação','Indisponível') NULL AFTER status,
    ADD COLUMN data_cadastro DATE NULL AFTER status_imovel;

-- migra o valor da coluna antiga (texto livre) para o novo ENUM
UPDATE Imovel SET status_imovel = status WHERE status_imovel IS NULL;

-- não existia data de cadastro antes: usamos a data de hoje como padrão
-- para os imóveis já cadastrados (ajuste manualmente depois se souber a
-- data real de cada um)
UPDATE Imovel SET data_cadastro = CURDATE() WHERE data_cadastro IS NULL;

ALTER TABLE Imovel
    MODIFY COLUMN status_imovel ENUM ('Disponível','Reservado','Vendido','Alugado','Em negociação','Indisponível') NOT NULL DEFAULT 'Disponível',
    MODIFY COLUMN data_cadastro DATE NOT NULL DEFAULT (CURRENT_DATE);

-- remove a coluna antiga, já substituída pelo ENUM
ALTER TABLE Imovel DROP COLUMN status;


-- ============================================
-- VISITA
-- ============================================
ALTER TABLE Visita
    ADD COLUMN status_visita ENUM ('Agendada','Confirmada','Realizada','Cancelada','Cliente faltou')
        NOT NULL DEFAULT 'Agendada' AFTER data_visita;

-- opcional: marcar como "Realizada" as visitas cujo horário já passou
-- UPDATE Visita SET status_visita = 'Realizada' WHERE data_visita < NOW();


-- ============================================
-- PAGAMENTO
-- ============================================
ALTER TABLE Pagamento
    ADD COLUMN status_pagamento ENUM ('Pago','Pendente','Atrasado','Cancelado') NULL AFTER forma_pagamento,
    ADD COLUMN data_vencimento DATE NULL AFTER status_pagamento;

-- todo pagamento já cadastrado tem "data_pagamento" preenchida, ou seja,
-- já foi quitado: marcamos como 'Pago' e usamos a própria data do
-- pagamento como vencimento (ajuste manualmente se souber a data real)
UPDATE Pagamento
SET status_pagamento = 'Pago',
    data_vencimento = data_pagamento
WHERE status_pagamento IS NULL;

ALTER TABLE Pagamento
    MODIFY COLUMN status_pagamento ENUM ('Pago','Pendente','Atrasado','Cancelado') NOT NULL DEFAULT 'Pendente',
    MODIFY COLUMN data_vencimento DATE NOT NULL;


-- ============================================
-- CLIENTE  (corrigido: "Cliete" -> "Cliente")
-- ============================================
ALTER TABLE Cliente
    ADD COLUMN data_cadastro DATE NULL AFTER email;

UPDATE Cliente SET data_cadastro = CURDATE() WHERE data_cadastro IS NULL;

ALTER TABLE Cliente
    MODIFY COLUMN data_cadastro DATE NOT NULL DEFAULT (CURRENT_DATE);


-- ============================================
-- CONTRATO
-- ============================================
ALTER TABLE Contrato
    ADD COLUMN data_inicio DATE NULL AFTER data_assinatura,
    ADD COLUMN data_fim DATE NULL AFTER data_inicio;

-- contratos de aluguel: usa a data de início real do aluguel vinculado
UPDATE Contrato c
JOIN Aluguel a ON c.id_aluguel = a.id_aluguel
SET c.data_inicio = a.data_inicio
WHERE c.data_inicio IS NULL;

-- contratos de venda não têm "início de locação": usamos a própria
-- data de assinatura
UPDATE Contrato
SET data_inicio = data_assinatura
WHERE data_inicio IS NULL;

-- o modelo original não guardava prazo de contrato. Como padrão de
-- migração: aluguéis recebem 12 meses de vigência a partir do início, e
-- vendas recebem data_fim igual à data_inicio (evento único). Ajuste os
-- prazos reais manualmente depois, se necessário.
UPDATE Contrato c
JOIN Aluguel a ON c.id_aluguel = a.id_aluguel
SET c.data_fim = DATE_ADD(c.data_inicio, INTERVAL 12 MONTH)
WHERE c.data_fim IS NULL;

UPDATE Contrato
SET data_fim = data_inicio
WHERE data_fim IS NULL;

ALTER TABLE Contrato
    MODIFY COLUMN data_inicio DATE NOT NULL,
    MODIFY COLUMN data_fim DATE NOT NULL;
