import mysql.connector

conexao = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'senha',
    database= 'nome do bd'
)

cursor = conexao.cursor()

#CREATE
def inserir_candidato(nome, email, cpf, linkedin, github):
    query = 'INSERT INTO candidatos (nome, email, cpf, linkedin, github) VALUES (%s,%s,%s,%s,%s)'
    values = (nome, email, cpf, linkedin, github)
    cursor.execute(query,values)
    conexao.commit() # Quando edita o banco de dadoS
    cursor.close()
    conexao.close()

def inserir_formacao(id_candidato, nome_candidato, instituicao, curso, duracao_em_meses):
    query = 'INSERT INTO formacao (id_candidato, nome_candidato, instituicao, curso, duracao_em_meses) VALUES (%s,%s,%s,%s,%s)'
    values = (id_candidato, nome_candidato, instituicao, curso, duracao_em_meses)
    cursor.execute(query,values)
    conexao.commit() # Quando edita o banco de dadoS
    cursor.close()
    conexao.close()

def inserir_experiencia_profissional(nome_candidato, empresa, cargo, tempo_em_meses):
    query = 'INSERT INTO experiencia_profissional (id_candidato, nome_candidato, empresa, cargo, tempo_em_meses) VALUES (NULL,%s,%s,%s,%s)'
    values = (nome_candidato, empresa, cargo, tempo_em_meses)
    cursor.execute(query,values)
    conexao.commit() # Quando edita o banco de dadoS
    cursor.close()
    conexao.close()    



#READ
def ler_candidatos():
    cursor.execute('SELECT * FROM candidatos')
    candidatos = cursor.fetchall() # quando le o banco de dados
    print(candidatos)
    cursor.close()
    conexao.close()    



def ler_formacao():
    cursor.execute('SELECT * FROM formacao')
    formacao = cursor.fetchall() # quando le o banco de dados
    print(formacao)
    cursor.close()
    conexao.close()    


def ler_experiencia_profissional():
    cursor.execute('SELECT * FROM formacao')
    formacao = cursor.fetchall() # quando le o banco de dados
    print(formacao)
    cursor.close()
    conexao.close()    
    



#UPDATE
def atualizar_candidato(nome, email, cpf, linkedin, github, id_candidato):
    query= 'UPDATE candidatos SET nome = %s, email = %s, cpf = %s, linkedin = %s, github = %s WHERE id_candidato = %s'
    values = (nome, email, cpf, linkedin, github, id_candidato) 
    cursor.execute(query,values)



def atualizar_formacao(nome_candidato, instituicao, curso, duracao_em_meses, id_candidato):
    query = 'UPDATE formacao SET nome_candidato = %s, instituicao = %s, curso = %s, duracao_em_meses = %s WHERE id_candidato = %s'
    values = (nome_candidato, instituicao, curso, duracao_em_meses, id_candidato)
    cursor.execute(query, values)
    conexao.commit()
    print("Formação atualizada com sucesso!")

    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()




#DELETE

def delete_formacao (id_candidato):
    query = f'DELETE FROM formacao WHERE id_candidato = {id_candidato}'
    values = (id_candidato)
    cursor.execute(query,values)
    conexao.commit() # Quando edita o banco de dados"""
    cursor.close()
    conexao.close()    


def delete_candidato (id_candidato):
    query = f'DELETE FROM candidatos WHERE id_candidato = "{id_candidato}"'
    cursor.execute(query)
    conexao.commit() # Quando edita o banco de dados"""    
    cursor.close()
    conexao.close()    




# Exemplo de uso:

delete_candidato(1)



#inserir_formacao('1', 'Thiago', 'UNIP', 'ADS', '4')

#inserir_candidato('Robin', 'robin@senai', '32145696354', 'robin.linkedin', 'robin.github')






