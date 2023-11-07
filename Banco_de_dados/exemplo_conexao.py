import mysql.connector

# Configurações da conexão com o banco de dados
config = {
    'user': 'se_usuário',
    'password': 'sua_senha',
    'host': 'localhost',
    'database': 'nome_do_banco_de_dados'
}

# Estabelecer a conexão com o banco de dados
conexao = mysql.connector.connect(**config)

# Criar um cursor para executar consultas SQL
cursor = conexao.cursor()

# Exemplo de consulta SQL
selecionarDB= "use loja_ii;"
consulta = "SELECT * FROM tabela"

# Executar a consulta
cursor.execute(selecionarDB)
cursor.execute(consulta)

# Recuperar os resultados
resultados = cursor.fatall()

# Imprimir os resultados
for linha in resultados:
    print(linha)

# Fechar o cursor e a conexão
cursor.close()
conexao.close()

