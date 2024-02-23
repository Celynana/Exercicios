import sqlite3

conexao = sqlite3.connect('alunos')
cursor = conexao.cursor()

# 1. CRIAR UMA TABELA chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).

cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Celyna", 33, "Ciencias da Computacao")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Amora", 17, "Medicina")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Sherry", 25, "Direito")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Bruno", 30, "Administracao")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Savio", 18, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(6, "Kayo", 27, "Economia")')

# 3. CONSULTAS SQL
# A) SELECIONAR TODOS OS REGISTROS DA TABELA "ALUNO".

cursor.execute('SELECT * FROM alunos')
dados = cursor.execute('SELECT * FROM alunos')
for alunos in dados:
    print(alunos)

# B) SELECIONAR O NOME E A IDADE DOS ALUNOS COM MAIS DE 20 ANOS.

cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
for alunos in dados:
    print(alunos)

# C) SELECIONAR OS ALUNOS DO CURSO DE "ENGENHARIA" EM ORDEM ALFABETICA.

cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
for alunos in dados:
    #print(alunos)

# D) CONTAR O  NUMERO TOTAL DE ALUNOS NA TABELA.

 cursor.execute('SELECT COUNT(*) AS total_alunos FROM alunos')
total_alunos = cursor.execute('SELECT COUNT(*) AS C FROM alunos')
for alunos in total_alunos:
    print ("total_alunos", alunos)
    
# 4. ATUALIZAÇAO E REMOÇAO
# A) ATUALIZE A IDADE DE UM ALUNO ESPECIFICO NA TABELA.

cursor.execute('UPDATE alunos SET idade = 22 WHERE nome = "Amora" ')

# B) REMOVA UM ALUNO PELO SEU ID.

cursor.execute('DELETE FROM alunos WHERE id= 4')

# 5. CRIAR UMA TABELA E INSERIR DADOS.
# CRIE UMA TABELA CHAMADA "CLIENTES" COM OS CAMPOS: id (chave primária), nome (texto), idade (inteiro) e saldo (float). INSIRA ALGUNS REGISTRO DE CLIENTES NA TABELA.

cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')

cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "Marisa", 33, 950.50)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, "Carlos", 28, 1000)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "Carlos", 20, 1750.30)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "vania", 40, 2500.75)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, "Alfredo", 65, 3000.54)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(6, "Francisca", 50, 6000.99)')

# 6. CONSULTAS E FUNÇÕES AGREGADAS.
# ESCREVA CONSULTA SQL PARA REALIZAR AS SEGUINTES TAREFAS:

# A) SELECIONE O NOME E A IDADE DOS CLIENTES COM IDADE SUPERIOR A 30 ANOS. 

cursor.execute('SELECT nome, idade FROM clientes where idade >30')
dados = cursor.execute('SELECT nome, idade FROM clientes where idade >30')
for clientes in dados:
    print(clientes)

# B) CALCULE O SALDO MEDIO DOS CLIENTES. 

cursor.execute('SELECT AVG (saldo) AS saldo_medio FROM clientes')
saldo_medio = cursor.execute('SELECT AVG (saldo) AS saldo_medio FROM clientes')
for clientes in saldo_medio:
    print( "saldo_medio",clientes)

# c) ENCONTRE O CLIENTE COM O SALDO MAXIMO.

cursor.execute('SELECT nome, saldo FROM CLIENTES WHERE saldo = (SELECT MAX(saldo) FROM CLIENTES)')
saldo_maximo = cursor.execute('SELECT nome, saldo FROM CLIENTES WHERE saldo = (SELECT MAX(saldo) FROM CLIENTES)')
for clientes in saldo_maximo:
    print("saldo_maximo",clientes)


# D) CONTE QUANTOS CLIENTES TEM O SALDO ACIMA DE 1000.

cursor.execute('SELECT COUNT (*) AS clientes_saldo_acima_1000 FROM clientes WHERE saldo >1000')
clientes_saldo_acima_1000 = cursor.execute('SELECT COUNT (*) AS clientes_saldo_acima_1000 FROM clientes WHERE saldo >1000')
for clientes in clientes_saldo_acima_1000:
    print("clientes_saldo_acima_1000",clientes)

# 7. ATUALIZAÇÃO E REMOÇÃO COM CONDIÇÕES.
# A) ATUALIZE O SALDO DE UM CLIENTE ESPECIFICO.

cursor.execute('UPDATE clientes SET saldo = 10000 WHERE nome = "Alfredo" ')

# B) REMOVA UM CLIENTE PELO SEU ID. 

cursor.execute('DELETE FROM clientes WHERE id=2')


# 8. JUNÇÃO DE TABELAS.
# CRIE UMA SEGUNDA TABELA CHAMADA "COMPRAS" COM OS CAMPOS: id(CHAVE PRIMARIA), cliente_id(CHAVE ESTRANGEIRA REDERENCIANDO O id DA TABELA "CLIENTES"), produto (TEXTO) e valor (REAL).

cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT, produto TEXT, valor REAL, FOREIGN KEY (cliente_id) REFERENCES CLIENTES(id))')

#INSIRA ALGUMAS COMPRAS ASSOCIADAS A CLIENTES EXISTENTES NA TABELA "CLIENTES".
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1, 1, "casa", 100)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(2, 2, "Carro", 32000)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(3, 3, "apartamento", 150000)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(4, 4, "Lancha", 80000)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(5, 5, "Aviao", 100000)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(6, 1, "Moto", 30000)')

#ESCREVA UMA CONSULTA PARA EXIBIR O NOME DO CLIENTE, O PRODUTO E O VALOR DE CADA COMPRA.

cursor.execute('SELECT clientes.nome AS nome_clientes, compras.produto, compras.valor FROM compras INNER JOIN clientes ON compras.cliente_id = clientes.id')
compra = cursor.execute('SELECT clientes.nome AS nome_clientes, compras.produto, compras.valor FROM compras INNER JOIN clientes ON compras.cliente_id = clientes.id')
for clientes in compra:
    print("Nome_cliente, Produto, valor",clientes)

conexao.commit()
conexao.close