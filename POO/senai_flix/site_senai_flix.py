from login import Cadastro_Login
from generos import Filmes_Generos


print("#########################################")
print("         Bem vindo a SenaiFlix           ")
print("#########################################")

cadastro_login = Cadastro_Login ()

cadastro_login.efetua_cadastro_login()

while True:
    print(" Escolha uma opção = ")
    print(" Opção 1. Escolher Filme ")
    print(" Opção 2. Escolher Série ")
    print(" Opção 3. Escolher Documentário ")
    print(" Opção 4. Sair ")

    opcao = int(input("Digite a sua opção = "))

    if opcao == 1:       
        
        filmes_generos = Filmes_Generos

        filmes_generos.menu_generos()

        break

        