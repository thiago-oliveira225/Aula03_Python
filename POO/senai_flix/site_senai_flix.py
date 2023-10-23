from filmes import Filme, Serie, Documentario
from cliente import Cliente
from login import Login


print("#########################################")
print("         Bem vindo a SenaiFlix           ")
print("#########################################")

login = Login()

login.efetua_login()



while True:
    print(" Escolha uma opção = ")
    print(" Opção 1. Inserir Títulos ")
    print(" Opção 2. Listar Títulos ")
    print(" Opção 3. Atualizar Títulos ")
    print(" Opção 4. Deletar Títulos ")
    print(" Opção 5. Sair ")

    opcao = int (input())

    if opcao == 5 :
        break
    
    elif opcao == 1:
        print(" Escolha uma opção = ")
        print(" Opção 1. Inserir Filmes ")
        print(" Opção 2. Inserir Série ")
        print(" Opção 3. Inserir Documentario ")
        print(" Opção 4. Sair ")

    if opcao == 4:
        break

    if opcao == 1:
        filme = Filme("Matrix", "Ficção", 18, 180)
        

        
