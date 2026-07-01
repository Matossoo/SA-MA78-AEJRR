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