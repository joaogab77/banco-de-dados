CREATE DATABASE DBescola;
use DBescola


CREATE TABLE tbl_cidades (
    cid_codigo INT AUTO_INCREMENT PRIMARY KEY,
    cid_nome VARCHAR(100) NOT NULL,
    cid_UF VARCHAR(100) NOT NULL
);


CREATE TABLE tbl_cursos (
    cur_codigo INT AUTO_INCREMENT PRIMARY KEY,
    cur_nome VARCHAR(100) NOT NULL,
    cur_valor VARCHAR(100)
);


CREATE TABLE tbl_professores (
    prof_codigo INT AUTO_INCREMENT PRIMARY KEY,
    prof_nome VARCHAR(100) NOT NULL,
    prof_endereco VARCHAR(100),
    prof_email VARCHAR(100),
    prof_telefone VARCHAR(100),
    prof_CPF VARCHAR(100),
    prof_idade VARCHAR(100),
    tbl_cidades_cid_codigo INT,
    tbl_aulas_aul_codigo INT,
    FOREIGN KEY (tbl_cidades_cid_codigo) REFERENCES tbl_cidades(cid_codigo)
);


CREATE TABLE tbl_alunos (
    alu_codigo INT AUTO_INCREMENT PRIMARY KEY,
    alu_nome VARCHAR(45) NOT NULL,
    alu_endereco VARCHAR(45),
    alu_email VARCHAR(45),
    alu_telefone VARCHAR(45),
    alu_idade VARCHAR(45),
    tbl_cidades_cid_codigo INT,
    tbl_cursos_cur_codigo INT,
    FOREIGN KEY (tbl_cidades_cid_codigo) REFERENCES tbl_cidades(cid_codigo),
    FOREIGN KEY (tbl_cursos_cur_codigo) REFERENCES tbl_cursos(cur_codigo)
);


CREATE TABLE tbl_aulas (
    aul_codigo INT AUTO_INCREMENT PRIMARY KEY,
    aul_materia VARCHAR(45) NOT NULL,
    aul_horario VARCHAR(45),
    tbl_cursos_cur_codigo INT,
    tbl_alunos_alu_codigo INT,
    FOREIGN KEY (tbl_cursos_cur_codigo) REFERENCES tbl_cursos(cur_codigo),
    FOREIGN KEY (tbl_alunos_alu_codigo) REFERENCES tbl_alunos(alu_codigo)
);


CREATE TABLE tbl_usuarios (
    usu_codigo INT AUTO_INCREMENT PRIMARY KEY,
    usu_nome VARCHAR(45) NOT NULL,
    usu_username VARCHAR(45) UNIQUE NOT NULL,
    usu_senha VARCHAR(45) NOT NULL
);


INSERT INTO tbl_cidades (cid_nome, cid_UF) VALUES
('São Paulo', 'SP'),
('Rio de Janeiro', 'RJ'),
('Belo Horizonte', 'MG');


INSERT INTO tbl_cursos (cur_nome, cur_valor) VALUES
('Matemática', 'R$ 500,00'),
('Física', 'R$ 600,00'),
('Química', 'R$ 700,00');


INSERT INTO tbl_professores (prof_nome, prof_endereco, prof_email, prof_telefone, prof_CPF, prof_idade, tbl_cidades_cid_codigo) VALUES
('João da Silva', 'Rua A, 123', 'joao@escola.com', '123456789', '111.222.333-44', '40', 1),
('Maria Oliveira', 'Rua B, 456', 'maria@escola.com', '987654321', '555.666.777-88', '35', 2);


INSERT INTO tbl_alunos (alu_nome, alu_endereco, alu_email, alu_telefone, alu_idade, tbl_cidades_cid_codigo, tbl_cursos_cur_codigo) VALUES
('Carlos Mendes', 'Rua C, 789', 'carlos@exemplo.com', '998877665', '20', 1, 1),
('Ana Souza', 'Rua D, 101', 'ana@exemplo.com', '112233445', '22', 3, 2);


INSERT INTO tbl_aulas (aul_materia, aul_horario, tbl_cursos_cur_codigo, tbl_alunos_alu_codigo) VALUES
('Matemática', '08:00 - 10:00', 1, 1),
('Física', '10:00 - 12:00', 2, 2);


INSERT INTO tbl_usuarios (usu_nome, usu_username, usu_senha) VALUES
('Admin', 'admin', 'admin123'),
('Professor', 'prof1', 'prof123');







