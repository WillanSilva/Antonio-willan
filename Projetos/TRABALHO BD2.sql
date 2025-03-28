DROP TABLE IF EXISTS solicita;
DROP TABLE IF EXISTS vende_produto;
DROP TABLE IF EXISTS loja;
DROP TABLE IF EXISTS produto_meio_empacotamento;
DROP TABLE IF EXISTS produto_tamanho;
DROP TABLE IF EXISTS produto_categoria;
DROP TABLE IF EXISTS cesta_compras;
DROP TABLE IF EXISTS vende_atacado;
DROP TABLE IF EXISTS providencia;
DROP TABLE IF EXISTS fornece;
DROP TABLE IF EXISTS registra;
DROP TABLE IF EXISTS pedido;
DROP TABLE IF EXISTS marca;
DROP TABLE IF EXISTS dependentes;
DROP TABLE IF EXISTS cliente;
DROP TABLE IF EXISTS fornecedor;
DROP TABLE IF EXISTS inventario;
DROP TABLE IF EXISTS produto;
DROP VIEW IF EXISTS clientes CASCADE;
DROP VIEW IF EXISTS vendidos CASCADE;



CREATE TABLE produto
(
  id_produto VARCHAR(20) NOT NULL,
  lote VARCHAR(20),
  nome VARCHAR(50) NOT NULL,
  codigo VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_produto),
  UNIQUE (lote)
);

CREATE TABLE inventario
(
  id_inventario VARCHAR(20) NOT NULL,
  estoque_normal_unidades INT NOT NULL,
  PRIMARY KEY (id_inventario)
);

CREATE TABLE fornecedor
(
  id_fornecedor VARCHAR(20) NOT NULL,
  nome VARCHAR(50) NOT NULL,
  endereco VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_fornecedor)
);

CREATE TABLE cliente
(
  id_cliente VARCHAR(20) NOT NULL,
  nome VARCHAR(50),
  celular VARCHAR(20),
  cpf VARCHAR(11),
  tipo_cliente VARCHAR(20) NOT NULL,
  pontos INT,
  endereco VARCHAR(50),
  PRIMARY KEY (id_cliente)
);

CREATE TABLE dependentes
(
  id_dependente VARCHAR(20) NOT NULL,
  parentesco VARCHAR(50) NOT NULL,
  nome VARCHAR(50) NOT NULL,
  id_cliente VARCHAR(20),
  PRIMARY KEY (id_dependente, id_cliente),
  FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

CREATE TABLE marca
(
  id_marca VARCHAR(20) NOT NULL,
  nome VARCHAR(50) NOT NULL,
  id_produto VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_marca),
  FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
);

CREATE TABLE pedido
(
  id_pedido VARCHAR(20) NOT NULL,
  data VARCHAR(20),
  tipo_pedido VARCHAR(20) NOT NULL,
  id_cliente VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_pedido),
  FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

CREATE TABLE registra
(
  valor_unidade INT NOT NULL,
  id_produto VARCHAR(20) NOT NULL,
  id_inventario VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_produto, id_inventario),
  FOREIGN KEY (id_produto) REFERENCES produto(id_produto),
  FOREIGN KEY (id_inventario) REFERENCES inventario(id_inventario)
);

CREATE TABLE fornece
(
  tipo_entrega VARCHAR(20) NOT NULL,
  id_fornecedor VARCHAR(20) NOT NULL,
  id_produto VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_fornecedor, id_produto),
  FOREIGN KEY (id_fornecedor) REFERENCES fornecedor(id_fornecedor),
  FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
);

CREATE TABLE providencia
(
  custo_produto INT NOT NULL,
  id_fornecedor VARCHAR(20) NOT NULL,
  id_inventario VARCHAR(20) NOT NULL,
  PRIMARY KEY (custo_produto),
  FOREIGN KEY (id_fornecedor) REFERENCES fornecedor(id_fornecedor),
  FOREIGN KEY (id_inventario) REFERENCES inventario(id_inventario),
  UNIQUE (id_fornecedor, id_inventario)
);

CREATE TABLE vende_atacado
(
  id_fornecedor VARCHAR(20) NOT NULL,
  id_marca VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_fornecedor, id_marca),
  FOREIGN KEY (id_fornecedor) REFERENCES fornecedor(id_fornecedor),
  FOREIGN KEY (id_marca) REFERENCES marca(id_marca)
);

CREATE TABLE cesta_compras
(
  id_cesta_compras VARCHAR(20) NOT NULL,
  numero_items INT NOT NULL,
  id_pedido VARCHAR(20) NOT NULL,
  id_produto VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_cesta_compras),
  FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido),
  FOREIGN KEY (id_produto) REFERENCES produto(id_produto),
  UNIQUE (id_pedido, id_produto)
);

CREATE TABLE produto_categoria
(
  categoria VARCHAR(20) NOT NULL,
  id_produto VARCHAR(20) NOT NULL,
  PRIMARY KEY (categoria, id_produto),
  FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
);

CREATE TABLE produto_tamanho
(
  tamanho VARCHAR(20) NOT NULL,
  id_produto VARCHAR(20) NOT NULL,
  PRIMARY KEY (tamanho, id_produto),
  FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
);

CREATE TABLE produto_meio_empacotamento
(
  meio_empacotamento VARCHAR(50) NOT NULL,
  id_produto VARCHAR(20) NOT NULL,
  PRIMARY KEY (meio_empacotamento, id_produto),
  FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
);

CREATE TABLE loja
(
  nome VARCHAR(50),
  endereco VARCHAR(50),
  id_loja VARCHAR(20) NOT NULL,
  horario_atendimento VARCHAR(20),
  id_inventario VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_loja),
  FOREIGN KEY (id_inventario) REFERENCES inventario(id_inventario)
);

CREATE TABLE vende_produto
(
  preco INT NOT NULL,
  id_loja VARCHAR(20) NOT NULL,
  id_produto VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_loja, id_produto),
  FOREIGN KEY (id_loja) REFERENCES loja(id_loja),
  FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
);

CREATE TABLE solicita
(
  id_solicita VARCHAR(20) NOT NULL,
  id_pedido VARCHAR(20) NOT NULL,
  id_loja VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_solicita),
  FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido),
  FOREIGN KEY (id_loja) REFERENCES loja(id_loja),
  UNIQUE (id_pedido, id_loja)
);

delete from inventario;
insert into inventario(id_inventario, estoque_normal_unidades) values ('INV1001', 1000);
insert into inventario(id_inventario, estoque_normal_unidades) values ('INV1002', 500);
insert into inventario(id_inventario, estoque_normal_unidades) values ('INV1003', 1000);
insert into inventario(id_inventario, estoque_normal_unidades) values ('INV1004', 600);
insert into inventario(id_inventario, estoque_normal_unidades) values ('INV1005', 1000);
insert into inventario(id_inventario, estoque_normal_unidades) values ('INV1006', 700);


delete from produto;
insert into produto(id_produto, codigo, lote, nome) values('PROD1001', 'CODPROD1001', 'LOTE1001', 'refrigerante coca cola');
insert into produto(id_produto, codigo, lote, nome) values('PROD1002', 'CODPROD1002', 'LOTE1002', 'refrigerante pepsi');
insert into produto(id_produto, codigo, lote, nome) values('PROD1003', 'CODPROD1003', 'LOTE1003', 'cerveja antartica');
insert into produto(id_produto, codigo, lote, nome) values('PROD1004', 'CODPROD1004', 'LOTE1004', 'cerveja brahma');
insert into produto(id_produto, codigo, lote, nome) values('PROD1005', 'CODPROD1005', 'LOTE1005', 'cerveja skol');
insert into produto(id_produto, codigo, lote, nome) values('PROD1006', 'CODPROD1006', 'LOTE1006', 'cerveja heineken');


delete from cliente;
insert into cliente(id_cliente, nome, celular, cpf, tipo_cliente, endereco) values('CLI1001', 'Miguel', '(21)1234-1000', '12345671000', 'frequente', 'Rua santa luzia, 343');
insert into cliente(id_cliente, nome, celular, cpf, tipo_cliente, endereco) values('CLI1002', 'Helena', '(21)1234-1001', '12345671001', 'frequente', 'Rua sao jorge, 341');
insert into cliente(id_cliente, nome, celular, cpf, tipo_cliente, endereco) values('CLI1003', 'Arthur', '(21)1234-1002', '12345671002', 'frequente', 'Rua dezenove, 333');
insert into cliente(id_cliente, nome, celular, cpf, tipo_cliente, endereco) values('CLI1004', 'Alice', '(21)1234-1003', '12345671003', 'frequente', 'Rua castro alves, 331');
insert into cliente(id_cliente, nome, celular, cpf, tipo_cliente, endereco) values('CLI1005', 'Heitor', '(21)1234-1004', '12345671004', 'frequente', 'Rua duque de caxias, 329');
insert into cliente(id_cliente, nome, celular, cpf, tipo_cliente, endereco) values('CLI1006', 'Laura', '(21)1234-1005', '12345671005', 'frequente', 'Rua rui barbosa,320');


delete from loja;
insert into loja(id_loja, nome, endereco, horario_atendimento, id_inventario) values ('LOJA1001', 'Loja Centro 1', 'Rua Presidente Vargas 100', '8.00am-10.00pm', 'INV1001');
insert into loja(id_loja, nome, endereco, horario_atendimento, id_inventario) values ('LOJA1002', 'Loja Centro 2', 'Rua Rio Branco 100', '8.00am-10.00pm', 'INV1002');
insert into loja(id_loja, nome, endereco, horario_atendimento, id_inventario) values ('LOJA1003', 'Loja Zona Sul 1', 'Avenida Atlantica 100', '8.00am-10.00pm', 'INV1003');
insert into loja(id_loja, nome, endereco, horario_atendimento, id_inventario) values ('LOJA1004', 'Loja Zona Sul 2', 'Avenida Nossa Senhora de Copacabana 100', '8.00am-10.00pm', 'INV1004');
insert into loja(id_loja, nome, endereco, horario_atendimento, id_inventario) values ('LOJA1005', 'Loja Zona Norte 1', 'Avenida Brasil 100', '8.00am-10.00pm', 'INV1005');
insert into loja(id_loja, nome, endereco, horario_atendimento, id_inventario) values ('LOJA1006', 'Loja Zona Norte 2', 'Estrada do Galeao 100', '8.00am-10.00pm', 'INV1006');


delete from fornecedor;
insert into fornecedor(id_fornecedor, nome, endereco) values ('FORNE1001', 'Empresa de Atacado MG', 'Rua Minas Gerais 100');
insert into fornecedor(id_fornecedor, nome, endereco) values ('FORNE1002', 'Empresa de Atacado ES', 'Rua Espirito Santo 200');
insert into fornecedor(id_fornecedor, nome, endereco) values ('FORNE1003', 'Empresa de Atacado TM', 'Rua Treze de Maio 300');
insert into fornecedor(id_fornecedor, nome, endereco) values ('FORNE1004', 'Empresa de Atacado FL', 'Rua das Flores 400');
insert into fornecedor(id_fornecedor, nome, endereco) values ('FORNE1005', 'Empresa de Atacado SM', 'Rua Santa Maria 500');
insert into fornecedor(id_fornecedor, nome, endereco) values ('FORNE1006', 'Empresa de Atacado BV', 'Rua Boa Vista 600');


delete from providencia;
insert into providencia(id_fornecedor, id_inventario, custo_produto) values ('FORNE1001', 'INV1001', 300);
insert into providencia(id_fornecedor, id_inventario, custo_produto) values ('FORNE1002', 'INV1002', 260);
insert into providencia(id_fornecedor, id_inventario, custo_produto) values ('FORNE1003', 'INV1003', 149);
insert into providencia(id_fornecedor, id_inventario, custo_produto) values ('FORNE1004', 'INV1004', 160);
insert into providencia(id_fornecedor, id_inventario, custo_produto) values ('FORNE1005', 'INV1005', 180);
insert into providencia(id_fornecedor, id_inventario, custo_produto) values ('FORNE1006', 'INV1006', 250);


delete from marca;
insert into marca(id_marca, nome, id_produto) values ('MARCA1001', 'Coca Cola', 'PROD1001');
insert into marca(id_marca, nome, id_produto) values ('MARCA1002', 'Pepsi', 'PROD1002');
insert into marca(id_marca, nome, id_produto) values ('MARCA1003', 'Antartica', 'PROD1003');
insert into marca(id_marca, nome, id_produto) values ('MARCA1004', 'Brahma', 'PROD1004');
insert into marca(id_marca, nome, id_produto) values ('MARCA1005', 'Skol', 'PROD1005');
insert into marca(id_marca, nome, id_produto) values ('MARCA1006', 'Heineken', 'PROD1006');


delete from dependentes;
insert into dependentes(id_dependente, parentesco, nome, id_cliente) values ('DEPEN1001', 'esposa', 'Manuela', 'CLI1001');
insert into dependentes(id_dependente, parentesco, nome, id_cliente) values ('DEPEN1002', 'esposo', 'Bernardo', 'CLI1002');
insert into dependentes(id_dependente, parentesco, nome, id_cliente) values ('DEPEN1003', 'esposa', 'Valentina', 'CLI1003');
insert into dependentes(id_dependente, parentesco, nome, id_cliente) values ('DEPEN1004', 'esposo', 'Davi', 'CLI1004');


delete from registra;
insert into registra(id_produto, id_inventario, valor_unidade) values ('PROD1001', 'INV1001', 350);
insert into registra(id_produto, id_inventario, valor_unidade) values ('PROD1002', 'INV1002', 310);
insert into registra(id_produto, id_inventario, valor_unidade) values ('PROD1003', 'INV1003', 199);
insert into registra(id_produto, id_inventario, valor_unidade) values ('PROD1004', 'INV1004', 210);
insert into registra(id_produto, id_inventario, valor_unidade) values ('PROD1005', 'INV1005', 230);
insert into registra(id_produto, id_inventario, valor_unidade) values ('PROD1006', 'INV1006', 300);


delete from fornece;
insert into fornece(id_fornecedor, id_produto, tipo_entrega) values ('FORNE1001', 'PROD1001', 'rapida');
insert into fornece(id_fornecedor, id_produto, tipo_entrega) values ('FORNE1002', 'PROD1002', 'normal');
insert into fornece(id_fornecedor, id_produto, tipo_entrega) values ('FORNE1003', 'PROD1003', 'rapida');
insert into fornece(id_fornecedor, id_produto, tipo_entrega) values ('FORNE1004', 'PROD1004', 'normal');
insert into fornece(id_fornecedor, id_produto, tipo_entrega) values ('FORNE1005', 'PROD1005', 'rapida');
insert into fornece(id_fornecedor, id_produto, tipo_entrega) values ('FORNE1006', 'PROD1006', 'normal');


delete from pedido;
insert into pedido(id_pedido, data, tipo_pedido, id_cliente) values ('PEDIDO1001', '18/06/2021', 'fisica', 'CLI1001');
insert into pedido(id_pedido, data, tipo_pedido, id_cliente) values ('PEDIDO1002', '18/06/2021', 'fisica', 'CLI1002');
insert into pedido(id_pedido, data, tipo_pedido, id_cliente) values ('PEDIDO1003', '18/06/2021', 'fisica', 'CLI1003');
insert into pedido(id_pedido, data, tipo_pedido, id_cliente) values ('PEDIDO1004', '18/06/2021', 'virtual', 'CLI1004');
insert into pedido(id_pedido, data, tipo_pedido, id_cliente) values ('PEDIDO1005', '18/06/2021', 'virtual', 'CLI1005');
insert into pedido(id_pedido, data, tipo_pedido, id_cliente) values ('PEDIDO1006', '18/06/2021', 'virtual', 'CLI1006');


delete from cesta_compras;
insert into cesta_compras(id_cesta_compras, numero_items, id_pedido, id_produto) values ('CESTA1001', 1, 'PEDIDO1001', 'PROD1001');
insert into cesta_compras(id_cesta_compras, numero_items, id_pedido, id_produto) values ('CESTA1002', 1, 'PEDIDO1002', 'PROD1002');
insert into cesta_compras(id_cesta_compras, numero_items, id_pedido, id_produto) values ('CESTA1003', 1, 'PEDIDO1003', 'PROD1003');
insert into cesta_compras(id_cesta_compras, numero_items, id_pedido, id_produto) values ('CESTA1004', 2, 'PEDIDO1004', 'PROD1004');
insert into cesta_compras(id_cesta_compras, numero_items, id_pedido, id_produto) values ('CESTA1005', 2, 'PEDIDO1005', 'PROD1005');
insert into cesta_compras(id_cesta_compras, numero_items, id_pedido, id_produto) values ('CESTA1006', 2, 'PEDIDO1006', 'PROD1006');


delete from vende_produto;
insert into vende_produto(id_loja, id_produto, preco) values ('LOJA1001', 'PROD1001', 450);
insert into vende_produto(id_loja, id_produto, preco) values ('LOJA1001', 'PROD1002', 410);
insert into vende_produto(id_loja, id_produto, preco) values ('LOJA1001', 'PROD1003', 299);
insert into vende_produto(id_loja, id_produto, preco) values ('LOJA1002', 'PROD1004', 310);
insert into vende_produto(id_loja, id_produto, preco) values ('LOJA1002', 'PROD1005', 330);
insert into vende_produto(id_loja, id_produto, preco) values ('LOJA1002', 'PROD1006', 400);


delete from vende_atacado;
insert into vende_atacado(id_fornecedor, id_marca) values ('FORNE1001', 'MARCA1001');
insert into vende_atacado(id_fornecedor, id_marca) values ('FORNE1002', 'MARCA1002');
insert into vende_atacado(id_fornecedor, id_marca) values ('FORNE1003', 'MARCA1003');
insert into vende_atacado(id_fornecedor, id_marca) values ('FORNE1004', 'MARCA1004');
insert into vende_atacado(id_fornecedor, id_marca) values ('FORNE1005', 'MARCA1005');
insert into vende_atacado(id_fornecedor, id_marca) values ('FORNE1006', 'MARCA1006');


delete from solicita;
insert into solicita(id_solicita, id_pedido, id_loja) values ('SOL1001', 'PEDIDO1001', 'LOJA1001');
insert into solicita(id_solicita, id_pedido, id_loja) values ('SOL1002', 'PEDIDO1002', 'LOJA1001');
insert into solicita(id_solicita, id_pedido, id_loja) values ('SOL1003', 'PEDIDO1003', 'LOJA1001');
insert into solicita(id_solicita, id_pedido, id_loja) values ('SOL1004', 'PEDIDO1004', 'LOJA1002');
insert into solicita(id_solicita, id_pedido, id_loja) values ('SOL1005', 'PEDIDO1005', 'LOJA1002');
insert into solicita(id_solicita, id_pedido, id_loja) values ('SOL1006', 'PEDIDO1006', 'LOJA1002');


delete from produto_tamanho;
insert into produto_tamanho(tamanho, id_produto) values('500ml', 'PROD1001');
insert into produto_tamanho(tamanho, id_produto) values('500ml', 'PROD1002');
insert into produto_tamanho(tamanho, id_produto) values('350ml', 'PROD1003');
insert into produto_tamanho(tamanho, id_produto) values('350ml', 'PROD1004');
insert into produto_tamanho(tamanho, id_produto) values('350ml', 'PROD1005');
insert into produto_tamanho(tamanho, id_produto) values('350ml', 'PROD1006');


delete from produto_categoria;
insert into produto_categoria(categoria, id_produto) values('refrigerantes', 'PROD1001');
insert into produto_categoria(categoria, id_produto) values('refrigerantes', 'PROD1002');
insert into produto_categoria(categoria, id_produto) values('cerveja', 'PROD1003');
insert into produto_categoria(categoria, id_produto) values('cerveja', 'PROD1004');
insert into produto_categoria(categoria, id_produto) values('cerveja', 'PROD1005');
insert into produto_categoria(categoria, id_produto) values('cerveja', 'PROD1006');


delete from produto_meio_empacotamento;
insert into produto_meio_empacotamento(meio_empacotamento, id_produto) values('garrafa plastico', 'PROD1001');
insert into produto_meio_empacotamento(meio_empacotamento, id_produto) values('garrafa lata', 'PROD1001');
insert into produto_meio_empacotamento(meio_empacotamento, id_produto) values('garrafa plastico', 'PROD1002');
insert into produto_meio_empacotamento(meio_empacotamento, id_produto) values('garrafa lata', 'PROD1002');
insert into produto_meio_empacotamento(meio_empacotamento, id_produto) values('garrafa plastico', 'PROD1003');
insert into produto_meio_empacotamento(meio_empacotamento, id_produto) values('garrafa lata', 'PROD1003');


CREATE VIEW clientes AS
    SELECT *
    FROM produto
    WHERE produto.nome = 'refrigerante'
    WITH LOCAL CHECK OPTION;

CREATE VIEW vendidos AS
    SELECT *
    FROM vende_produto
    WHERE vende_produto.preco = 300
    WITH CASCADED CHECK OPTION;

