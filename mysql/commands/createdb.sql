USE teste

CREATE TABLE pessoa(
	cpf VARCHAR(18) NOT NULL PRIMARY KEY,
	nome VARCHAR(30) NOT NULL,
	saldo DECIMAL(9, 2)
);

INSERT INTO pessoa (cpf, nome, saldo) VALUES ('100.500.311-31', 'AlguemAi', 18600.10);

