-- ENDERECO
INSERT INTO Endereco (rua, numero, bairro, cidade, estado, cep) VALUES
('Rua das Palmeiras', '120', 'Centro', 'Florianópolis', 'SC', '88000-001'),
('Av. Beira Mar', '500', 'Agronômica', 'Florianópolis', 'SC', '88015-200'),
('Rua do Comércio', '45', 'Estreito', 'Florianópolis', 'SC', '88070-100');

-- PROPRIETARIO
INSERT INTO Proprietario (nome, cpf_cnpj, telefone, email) VALUES
('João Pereira', '12345678901', '48999990001', '[joao@email.com](mailto:joao@email.com)'),
('Maria Oliveira', '23456789012', '48999990002', '[maria@email.com](mailto:maria@email.com)'),
('Carlos Mendes', '34567890123', '48999990003', '[carlos@email.com](mailto:carlos@email.com)');

-- CLIENTE
INSERT INTO Cliente (nome, cpf, telefone, email) VALUES
('Ana Souza', '11111111111', '48988880001', '[ana@email.com](mailto:ana@email.com)'),
('Pedro Santos', '22222222222', '48988880002', '[pedro@email.com](mailto:pedro@email.com)'),
('Juliana Costa', '33333333333', '48988880003', '[juliana@email.com](mailto:juliana@email.com)');

-- CORRETOR
INSERT INTO Corretor (nome, creci, telefone, email) VALUES
('Lucas Martins', 'CRECI12345', '48977770001', '[lucas@imobisys.com](mailto:lucas@imobisys.com)'),
('Fernanda Rocha', 'CRECI12346', '48977770002', '[fernanda@imobisys.com](mailto:fernanda@imobisys.com)'),
('Ricardo Alves', 'CRECI12347', '48977770003', '[ricardo@imobisys.com](mailto:ricardo@imobisys.com)');

-- TIPOIMOVEL
INSERT INTO TipoImovel (descricao) VALUES
('Casa'),
('Apartamento'),
('Terreno');

-- DOCUMENTO
INSERT INTO Documento (nome_documento, tipo) VALUES
('Escritura Pública', 'Escritura'),
('Certidão Negativa', 'Certidão'),
('Matrícula do Imóvel', 'Registro');

-- IMOVEL
INSERT INTO Imovel (id_proprietario, id_tipo_imovel, id_endereco, valor_sugerido, status) VALUES
(1, 1, 1, 450000.00, 'Disponível'),
(2, 2, 2, 650000.00, 'Disponível'),
(3, 3, 3, 300000.00, 'Disponível');

-- VISITA
INSERT INTO Visita (id_cliente, id_corretor, id_imovel, data_visita, observacoes) VALUES
(1, 1, 1, '2026-06-10 14:00:00', 'Cliente gostou do imóvel'),
(2, 2, 2, '2026-06-11 10:00:00', 'Solicitou nova visita'),
(3, 3, 3, '2026-06-12 16:00:00', 'Interessado para investimento');

-- VENDA
INSERT INTO Venda (id_cliente, id_corretor, id_imovel, data_venda, valor_venda) VALUES
(1, 1, 1, '2026-06-15', 440000.00);

-- ALUGUEL
INSERT INTO Aluguel (id_cliente, id_corretor, id_imovel, data_inicio, valor_aluguel) VALUES
(2, 2, 2, '2026-06-20', 2800.00);

-- CONTRATO
INSERT INTO Contrato (id_venda, id_aluguel, data_assinatura, clausulas) VALUES
(1, NULL, '2026-06-15', 'Contrato de compra e venda do imóvel.'),
(NULL, 1, '2026-06-20', 'Contrato de locação residencial.');

-- PAGAMENTO
INSERT INTO Pagamento (id_contrato, valor_pago, data_pagamento, forma_pagamento) VALUES
(1, 440000.00, '2026-06-15', 'Transferência Bancária'),
(2, 2800.00, '2026-06-20', 'PIX');

-- IMOVELDOCUMENTO
INSERT INTO ImovelDocumento (id_imovel, id_documento, data_arquivamento) VALUES
(1, 1, '2026-05-01'),
(1, 3, '2026-05-01'),
(2, 2, '2026-05-02');

-- ANUNCIO
INSERT INTO Anuncio (id_imovel, titulo, descricao, data_publicacao) VALUES
(1, 'Casa ampla no Centro', 'Casa com 3 quartos e garagem.', '2026-06-01'),
(2, 'Apartamento vista mar', 'Apartamento com 2 suítes.', '2026-06-02'),
(3, 'Terreno comercial', 'Ótima localização para comércio.', '2026-06-03');

-- FOTOIMOVEL
INSERT INTO FotoImovel (id_anuncio, url_foto, principal) VALUES
(1, 'https://imobisys.com/fotos/casa1.jpg', TRUE),
(1, 'https://imobisys.com/fotos/casa2.jpg', FALSE),
(2, 'https://imobisys.com/fotos/apto1.jpg', TRUE),
(3, 'https://imobisys.com/fotos/terreno1.jpg', TRUE);
