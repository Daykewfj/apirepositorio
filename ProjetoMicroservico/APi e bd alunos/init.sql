CREATE TABLE alunos (
    aluno_id character varying(5) NOT NULL,
    nome character varying(40) NOT NULL,
    endereco character varying(60),
    cidade character varying(15),
    estado character varying(15),
    cep character varying(10),
    pais character varying(15),
    telefone character varying(24)
);

INSERT INTO alunos VALUES
('A001', 'João Silva', 'Rua 1', 'São Paulo', 'SP', '01000-000', 'Brasil', '11999999999'),
('A002', 'Maria Oliveira', 'Rua 2', 'Rio de Janeiro', 'RJ', '20000-000', 'Brasil', '21999999999'),
('A003', 'Carlos Santos', 'Rua 3', 'Belo Horizonte', 'MG', '30000-000', 'Brasil', '31999999999'),
-- (adicione mais 7 ou mais registros para atingir 10 alunos).
