import mysql.connector

# Conectar ao banco de dados

conn = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'senai',
    database= 'banco_de_talentos')

cursor = conn.cursor()

# Script para criar uma tabela chamada cliente_vip

cursor.execute('''
    CREATE TABLE IF NOT EXISTS banco_de_talentos (
                nome VARCHAR (45) NOT NULL,
                email VARCHAR NOT NULL ,
                cpf INT NOT NULL,
                linkedin VARCHAR,
                github VARCHAR

               
    )''')

# Função para inserir candidato na tabela cadidato

def inserir_candidato(nome, email, cpf, linkedin, github):
    query = 'INSERT INTO cliente_vip (nome, email, cpf, linkedin, github) VALUES (%s,%s,%s,%s,%s)'
    values = (nome, email, cpf, linkedin, github)
    cursor.execute(query,values)
    conn.commit()

# Função para listar todos os clientes

'''def listar_clientes():
    cursor.execute('SELECT * FROM cliente_vip')
    cliente = cursor.fetchall()
    for clientes in cliente:
        print(clientes)

# Função para atualizar a tabela cliente_vip

def atualizar_cliente_vip(idcliente, nome, endereco, telefone,email,cpf):
    query= 'UPDATE cliente_vip SET nome = %s, endereco = %s, telefone = %s, email = %s, cpf = %s WHERE idcliente = %s'
    values = (nome, endereco, telefone, email, cpf, idcliente) 
    cursor.execute(query,values)

# Função para deletar um cliente

def delete_cliente(idcliente):
    query= 'DELETE FROM cliente_vip WHERE idcliente = %s'
    values = (idcliente)
    cursor.execute(query,values)'''

# Exemplo de uso:


inserir_candidato('Thiago', 'thiago@senai', '53698542366', 'thiago.linkedin', 'thiago.github')   