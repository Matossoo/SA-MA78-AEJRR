-- 21. Mostrar o valor total vendido por cada corretor

SELECT c.nome,
       COUNT(v.id_venda) AS total_vendas,
       SUM(v.valor_venda) AS valor_total_vendido
FROM Corretor c
JOIN Venda v
ON c.id_corretor = v.id_corretor
GROUP BY c.nome
ORDER BY valor_total_vendido DESC;


-- 22. Calcular a receita mensal prevista dos contratos de aluguel ativos

SELECT SUM(a.valor_aluguel) AS receita_mensal_total,
       COUNT(a.id_aluguel) AS contratos_ativos
FROM Aluguel a
JOIN Imovel i
ON a.id_imovel = i.id_imovel
WHERE i.status = 'Alugado';


-- 23. Mostrar as formas de pagamento mais utilizadas pelos clientes

SELECT forma_pagamento,
       COUNT(id_pagamento) AS quantidade_pagamentos,
       SUM(valor_pago) AS total_recebido
FROM Pagamento
GROUP BY forma_pagamento
ORDER BY quantidade_pagamentos DESC;


-- 24. Mostrar a quantidade de imóveis cadastrados por tipo

SELECT t.descricao AS tipo_imovel,
       COUNT(i.id_imovel) AS quantidade
FROM TipoImovel t
LEFT JOIN Imovel i
ON t.id_tipo_imovel = i.id_tipo_imovel
GROUP BY t.descricao
ORDER BY quantidade DESC;


-- 25. Mostrar os contratos de aluguel com a última data de pagamento

SELECT con.id_contrato,
       cli.nome AS inquilino,
       alu.valor_aluguel,
       MAX(pag.data_pagamento) AS ultimo_pagamento
FROM Contrato con
JOIN Aluguel alu
ON con.id_aluguel = alu.id_aluguel
JOIN Cliente cli
ON alu.id_cliente = cli.id_cliente
JOIN Pagamento pag
ON con.id_contrato = pag.id_contrato
GROUP BY con.id_contrato,
         cli.nome,
         alu.valor_aluguel;


-- 26. Mostrar os cinco imóveis com maior número de visitas

SELECT i.id_imovel,
       t.descricao AS tipo,
       e.bairro,
       COUNT(v.id_visita) AS total_visitas
FROM Imovel i
JOIN TipoImovel t
ON i.id_tipo_imovel = t.id_tipo_imovel
JOIN Endereco e
ON i.id_endereco = e.id_endereco
JOIN Visita v
ON i.id_imovel = v.id_imovel
GROUP BY i.id_imovel,
         t.descricao,
         e.bairro
ORDER BY total_visitas DESC
LIMIT 5;


-- 27. Selecionar clientes interessados em imóveis de uma cidade

SELECT DISTINCT c.nome,
                c.email,
                e.cidade
FROM Cliente c
JOIN Visita v
ON c.id_cliente = v.id_cliente
JOIN Imovel i
ON v.id_imovel = i.id_imovel
JOIN Endereco e
ON i.id_endereco = e.id_endereco
WHERE e.cidade = 'São Paulo';


-- 28. Listar imóveis que não possuem documentos cadastrados

SELECT i.id_imovel,
       i.status,
       p.nome AS proprietario,
       p.telefone
FROM Imovel i
JOIN Proprietario p
ON i.id_proprietario = p.id_proprietario
LEFT JOIN ImovelDocumento idoc
ON i.id_imovel = idoc.id_imovel
WHERE idoc.id_imovel_documento IS NULL;


-- 29. Mostrar os cinco bairros com maior média de valor dos imóveis

SELECT e.bairro,
       e.cidade,
       ROUND(AVG(i.valor_sugerido),2) AS media_preco
FROM Endereco e
JOIN Imovel i
ON e.id_endereco = i.id_endereco
GROUP BY e.bairro,
         e.cidade
ORDER BY media_preco DESC
LIMIT 5;


-- 30. Calcular o tempo médio entre a publicação do anúncio e a venda do imóvel

SELECT ROUND(AVG(DATEDIFF(v.data_venda, a.data_publicacao)),0)
AS media_dias_para_venda
FROM Anuncio a
JOIN Venda v
ON a.id_imovel = v.id_imovel;


-- 31. Auditar imóveis vendidos ou alugados sem registro correspondente

SELECT i.id_imovel,
       i.status,
       p.nome AS proprietario
FROM Imovel i
JOIN Proprietario p
ON i.id_proprietario = p.id_proprietario
WHERE i.status IN ('Vendido','Alugado')
AND i.id_imovel NOT IN
(
    SELECT id_imovel
    FROM Venda
)
AND i.id_imovel NOT IN
(
    SELECT id_imovel
    FROM Aluguel
);


-- 32. Calcular a comissão dos corretores (5% sobre as vendas)

SELECT c.id_corretor,
       c.nome,
       COUNT(v.id_venda) AS total_vendas,
       SUM(v.valor_venda) AS valor_total_vendido,
       ROUND(SUM(v.valor_venda) * 0.05,2) AS comissao
FROM Corretor c
JOIN Venda v
ON c.id_corretor = v.id_corretor
GROUP BY c.id_corretor,
         c.nome
ORDER BY comissao DESC;