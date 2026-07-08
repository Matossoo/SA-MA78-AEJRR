-- ============================================
-- CONSULTAS SQL - SISTEMA IMOBILIÁRIA
-- ============================================

-- 1. Listar todos os clientes
SELECT * FROM Cliente;

-- 2. Listar todos os corretores
SELECT * FROM Corretor;

-- 3. Listar todos os proprietários
SELECT * FROM Proprietario;

-- 4. Listar todos os imóveis disponíveis
SELECT *
FROM Imovel
WHERE status = 'Disponível';

-- 5. Listar imóveis do mais caro para o mais barato
SELECT *
FROM Imovel
ORDER BY valor_sugerido DESC;

-- 6. Mostrar imóvel com seu proprietário
SELECT
    i.id_imovel,
    p.nome AS proprietario,
    i.valor_sugerido,
    i.status
FROM Imovel i
JOIN Proprietario p
ON i.id_proprietario = p.id_proprietario;

-- 7. Mostrar imóvel com seu endereço
SELECT
    i.id_imovel,
    e.rua,
    e.numero,
    e.bairro,
    e.cidade,
    e.estado
FROM Imovel i
JOIN Endereco e
ON i.id_endereco = e.id_endereco;

-- 8. Mostrar tipo de cada imóvel
SELECT
    i.id_imovel,
    t.descricao AS tipo_imovel,
    i.valor_sugerido
FROM Imovel i
JOIN TipoImovel t
ON i.id_tipo_imovel = t.id_tipo_imovel;

-- 9. Listar visitas realizadas
SELECT
    c.nome AS cliente,
    co.nome AS corretor,
    v.data_visita
FROM Visita v
JOIN Cliente c
ON v.id_cliente = c.id_cliente
JOIN Corretor co
ON v.id_corretor = co.id_corretor;

-- 10. Mostrar visitas com imóvel
SELECT
    c.nome AS cliente,
    i.id_imovel,
    v.data_visita
FROM Visita v
JOIN Cliente c
ON v.id_cliente = c.id_cliente
JOIN Imovel i
ON v.id_imovel = i.id_imovel;

-- 11. Listar vendas realizadas
SELECT
    c.nome AS cliente,
    co.nome AS corretor,
    v.valor_venda,
    v.data_venda
FROM Venda v
JOIN Cliente c
ON v.id_cliente = c.id_cliente
JOIN Corretor co
ON v.id_corretor = co.id_corretor;

-- 12. Listar aluguéis
SELECT
    c.nome AS cliente,
    co.nome AS corretor,
    a.valor_aluguel,
    a.data_inicio
FROM Aluguel a
JOIN Cliente c
ON a.id_cliente = c.id_cliente
JOIN Corretor co
ON a.id_corretor = co.id_corretor;

-- 13. Mostrar contratos
SELECT *
FROM Contrato;

-- 14. Mostrar pagamentos
SELECT *
FROM Pagamento;

-- 15. Mostrar anúncios com seus imóveis
SELECT
    a.titulo,
    i.id_imovel,
    a.data_publicacao
FROM Anuncio a
JOIN Imovel i
ON a.id_imovel = i.id_imovel;

-- 16. Contar quantidade de imóveis
SELECT COUNT(*) AS total_imoveis
FROM Imovel;

-- 17. Contar quantidade de clientes
SELECT COUNT(*) AS total_clientes
FROM Cliente;

-- 18. Valor médio dos imóveis
SELECT AVG(valor_sugerido) AS media_valor
FROM Imovel;

-- 19. Valor total dos imóveis cadastrados
SELECT SUM(valor_sugerido) AS patrimonio
FROM Imovel;

-- 20. Quantidade de imóveis por tipo
SELECT
    t.descricao,
    COUNT(*) AS quantidade
FROM Imovel i
JOIN TipoImovel t
ON i.id_tipo_imovel = t.id_tipo_imovel
GROUP BY t.descricao;

-- 21. Quantidade de imóveis por proprietário
SELECT
    p.nome,
    COUNT(*) AS quantidade
FROM Imovel i
JOIN Proprietario p
ON i.id_proprietario = p.id_proprietario
GROUP BY p.nome;

-- 22. Clientes cujo nome começa com A
SELECT *
FROM Cliente
WHERE nome LIKE 'A%';

-- 23. Corretores em ordem alfabética
SELECT *
FROM Corretor
ORDER BY nome;

-- 24. Imóveis acima de R$ 400.000
SELECT *
FROM Imovel
WHERE valor_sugerido > 400000;

-- 25. Proprietários que possuem mais de um imóvel
SELECT
    p.nome,
    COUNT(i.id_imovel) AS quantidade
FROM Proprietario p
JOIN Imovel i
ON p.id_proprietario = i.id_proprietario
GROUP BY p.nome
HAVING COUNT(i.id_imovel) > 1;

--1. Busca de imóveis disponíveis filtrando por tipo e faixa de preço (Filtro do Site)

SELECT i.id_imovel, t.descricao AS tipo, i.valor_sugerido, e.bairro, e.cidade 
FROM Imovel i
JOIN TipoImovel t ON i.id_tipo_imovel = t.id_tipo_imovel
JOIN Endereco e ON i.id_endereco = e.id_endereco
WHERE i.status = 'Disponível' 
  AND t.descricao = 'Apartamento' 
  AND i.valor_sugerido BETWEEN 300000 AND 600000;

--2. Anúncios críticos que não possuem nenhuma foto cadastrada (Controle de Qualidade)

SELECT a.id_anuncio, a.titulo, a.data_publicacao, i.id_imovel
FROM Anuncio a
JOIN Imovel i ON a.id_imovel = i.id_imovel
LEFT JOIN FotoImovel f ON a.id_anuncio = f.id_anuncio
WHERE f.id_foto IS NULL;

--3. Grandes Investidores: Proprietários que possuem mais de 3 imóveis cadastrados

SELECT p.id_proprietario, p.nome, p.telefone, COUNT(i.id_imovel) AS total_imoveis
FROM Proprietario p
JOIN Imovel i ON p.id_proprietario = i.id_proprietario
GROUP BY p.id_proprietario, p.nome, p.telefone
HAVING COUNT(i.id_imovel) > 3
ORDER BY total_imoveis DESC;

--4. Leads Frios: Clientes que visitaram imóveis mas nunca fecharam compra ou aluguel

SELECT DISTINCT c.id_cliente, c.nome, c.email, c.telefone
FROM Cliente c
JOIN Visita v ON c.id_cliente = v.id_cliente
WHERE c.id_cliente NOT IN (SELECT id_cliente FROM Venda)
  AND c.id_cliente NOT IN (SELECT id_cliente FROM Aluguel);

--5. Faturamento total com Vendas agrupado por Mês e Ano (Relatório Comercial)

SELECT YEAR(v.data_venda) AS ano, MONTH(v.data_venda) AS mes, COUNT(v.id_venda) AS qtd_vendas, SUM(v.valor_venda) AS total_faturado
FROM Venda v
GROUP BY YEAR(v.data_venda), MONTH(v.data_venda)
ORDER BY ano DESC, mes DESC;

--6. Receita recorrente prevista: Faturamento mensal total de Aluguéis ativos

SELECT SUM(a.valor_aluguel) AS receita_mensal_total, COUNT(a.id_aluguel) AS contratos_ativos
FROM Aluguel a
JOIN Imovel i ON a.id_imovel = i.id_imovel
WHERE i.status = 'Alugado';

--7. Extrato de Contratos de Aluguel com a última data de pagamento efetuada

SELECT con.id_contrato, cli.nome AS inquilino, alu.valor_aluguel, MAX(pag.data_pagamento) AS ultimo_pagamento
FROM Contrato con
JOIN Aluguel alu ON con.id_aluguel = alu.id_aluguel
JOIN Cliente cli ON alu.id_cliente = cli.id_cliente
LEFT JOIN Pagamento pag ON con.id_contrato = pag.id_contrato
GROUP BY con.id_contrato, cli.nome, alu.valor_aluguel;

--8. Inteligência de Mercado: Top 5 bairros mais caros baseado no valor sugerido de venda

SELECT e.bairro, e.cidade, ROUND(AVG(i.valor_sugerido), 2) AS media_preco_imovel
FROM Endereco e
JOIN Imovel i ON e.id_endereco = i.id_endereco
JOIN TipoImovel t ON i.id_tipo_imovel = t.id_tipo_imovel
WHERE t.descricao = 'Casa'
GROUP BY e.bairro, e.cidade
ORDER BY media_preco_imovel DESC
LIMIT 5;

--9. Corretores Ociosos: Quem não realizou nenhuma visita nos últimos 30 dias

SELECT corr.id_corretor, corr.nome, corr.creci, corr.telefone
FROM Corretor corr
WHERE corr.id_corretor NOT IN (
    SELECT id_corretor 
    FROM Visita 
    WHERE data_visita >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
);

--10. Auditoria de Status: Imóveis marcados como "Vendido" ou "Alugado" sem contrato assinado

SELECT i.id_imovel, i.status, i.valor_sugerido, p.nome AS proprietario
FROM Imovel i
JOIN Proprietario p ON i.id_proprietario = p.id_proprietario
WHERE i.status IN ('Vendido', 'Alugado')
  AND i.id_imovel NOT IN (SELECT id_imovel FROM Venda)
  AND i.id_imovel NOT IN (SELECT id_imovel FROM Aluguel);

--11. Eficiência de Anúncio: Tempo médio (em dias) que um anúncio leva para virar uma venda

SELECT ROUND(AVG(DATEDIFF(v.data_venda, a.data_publicacao)), 0) AS media_dias_para_venda
FROM Anuncio a
JOIN Venda v ON a.id_imovel = v.id_imovel;

--12. Agenda Operacional: Listagem de visitas agendadas para o dia de hoje

SELECT v.data_visita, c.nome AS cliente, c.telefone AS tel_cliente, corr.nome AS corretor, i.id_imovel, e.rua, e.numero
FROM Visita v
JOIN Cliente c ON v.id_cliente = c.id_cliente
JOIN Corretor corr ON v.id_corretor = corr.id_corretor
JOIN Imovel i ON v.id_imovel = i.id_imovel
JOIN Endereco e ON i.id_endereco = e.id_endereco
WHERE DATE(v.data_visita) = CURDATE()
ORDER BY v.data_visita ASC;

--13. Análise Financeira: Formas de pagamento mais utilizadas pelos clientes

SELECT forma_pagamento, COUNT(id_pagamento) AS volume_transacoes, SUM(valor_pago) AS total_recebido
FROM Pagamento
GROUP BY forma_pagamento
ORDER BY volume_transacoes DESC;

--14. Imóveis Populares: Top 5 imóveis com mais registros de visitas cadastrados

SELECT i.id_imovel, t.descricao AS tipo, e.bairro, COUNT(v.id_visita) AS total_visitas
FROM Imovel i
JOIN TipoImovel t ON i.id_tipo_imovel = t.id_tipo_imovel
JOIN Endereco e ON i.id_endereco = e.id_endereco
JOIN Visita v ON i.id_imovel = v.id_imovel
GROUP BY i.id_imovel, t.descricao, e.bairro
ORDER BY total_visitas DESC
LIMIT 5;

--15. Disparo de Marketing: Selecionar e-mails de clientes interessados em imóveis de uma cidade específica

SELECT DISTINCT c.nome, c.email, e.cidade
FROM Cliente c
JOIN Visita v ON c.id_cliente = v.id_cliente
JOIN Imovel i ON v.id_imovel = i.id_imovel
JOIN Endereco e ON i.id_endereco = e.id_endereco
WHERE e.cidade = 'São Paulo';

--16. Auditoria de Documentos: Imóveis sem nenhuma Certidão ou Escritura arquivada

SELECT i.id_imovel, i.status, p.nome AS proprietario, p.telefone
FROM Imovel i
JOIN Proprietario p ON i.id_proprietario = p.id_proprietario
LEFT JOIN ImovelDocumento idoc ON i.id_imovel = idoc.id_imovel
WHERE idoc.id_imovel_documento IS NULL;

--17. Cálculo de Comissão: Total gerado por corretor baseado em uma taxa fixa de 5% sobre as vendas

SELECT c.id_corretor, c.nome, COUNT(v.id_venda) AS total_vendas, SUM(v.valor_venda) AS valor_total_vendido, ROUND(SUM(v.valor_venda) * 0.05, 2) AS comissao_imobiliaria
FROM Corretor c
JOIN Venda v ON c.id_corretor = v.id_corretor
GROUP BY c.id_corretor, c.nome
ORDER BY comissao_imobiliaria DESC;

--18. Dashboard Inventory: Quantidade de imóveis cadastrados segmentados por Tipo

SELECT t.descricao AS tipo_imovel, COUNT(i.id_imovel) AS quantidade_em_estoque
FROM TipoImovel t
LEFT JOIN Imovel i ON t.id_tipo_imovel = i.id_tipo_imovel
GROUP BY t.id_tipo_imovel, t.descricao
ORDER BY quantidade_em_estoque DESC;

--19. Campanhas de Pós-Venda/Boas-vindas: Contratos de aluguel iniciados nos últimos 7 dias

SELECT alu.id_aluguel, cli.nome AS inquilino, cli.email, alu.data_inicio, e.rua, e.bairro
FROM Aluguel alu
JOIN Cliente cli ON alu.id_cliente = cli.id_cliente
JOIN Imovel i ON alu.id_imovel = i.id_imovel
JOIN Endereco e ON i.id_endereco = e.id_endereco
WHERE alu.data_inicio BETWEEN DATE_SUB(CURDATE(), INTERVAL 7 DAY) AND CURDATE();

--20. Detalhes Completos da Ficha do Anúncio (Para o Painel Interno)

SELECT 
    a.id_anuncio, a.titulo, i.valor_sugerido, i.status,
    CONCAT(e.rua, ', ', e.numero, ' - ', e.bairro, ' (', e.cidade, '/', e.estado, ')') AS endereco_completo,
    p.nome AS proprietario, p.telefone AS telefone_proprietario,
    (SELECT url_foto FROM FotoImovel WHERE id_anuncio = a.id_anuncio AND principal = TRUE LIMIT 1) AS foto_capa
FROM Anuncio a
JOIN Imovel i ON a.id_imovel = i.id_imovel
JOIN Endereco e ON i.id_endereco = e.id_endereco
JOIN Proprietario p ON i.id_proprietario = p.id_proprietario
WHERE a.id_anuncio = 123; -- Substitua pelo ID do anúncio desejado