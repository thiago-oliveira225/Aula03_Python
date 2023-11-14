import mysql.connector

conexao = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'admin',
    database= 'teste',
)

cursor = conexao.cursor()

#CREATE
nome = "chocolate"
valor = 15
valor
valor
valor
comando = f'INSERT INTO vendas (nome, email, cpf, linkedin, github) VALUES ("{nome}", {email}, {cpf}, {linkedin}, {github})'
cursor.execute(comando)
conexao.commit() # Quando edita o banco de dadoS
#resultado = cursor.fetchall() # quando le o banco de dados


#READ
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
#conexao.commit() # Quando edita o banco de dados
resultado = cursor.fetchall() # quando le o banco de dados
print(resultado)


#UPDATE
valor = 6
nome_produto = "todynho"
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # Quando edita o banco de dados


#DELETE
nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # Quando edita o banco de dados"""



cursor.close()
conexao.close()






