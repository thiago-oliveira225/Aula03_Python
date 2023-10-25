from cadastro import Cadastro
from login import Login
from generos import Filmes_Generos

print("#########################################")
print("         Bem vindo a SenaiFlix           ")
print("#########################################")
print("          Já possui cadastro ?           ")

while True:

    resposta = input ("Digite 'S' para Sim e 'N' para Não = ")

    if resposta == 'N' or 'Não' or 'n' or 'não':

        # Criando uma instância e apontando para a classe correspondente para puxar os valores de input
        cadastro = Cadastro()
        break

    elif resposta != 'S' or 'Sim' or 's' or 'sim'or 'N' or 'Não' or 'n' or 'não':

        print ("Digite uma resposta válida conforme formato exemplificado")

    else:   

      break     

while True:

    print ("#### Vamos fazer o login #### \n")

    login = Login() # Criando uma instância e apontando para a classe correspondente para puxar os valores de input

    # Comparando os valores e tomando a ação com base na comparação

    if (cadastro.email_cadastro == login.email_login) and (cadastro.senha_cadastro == login.senha_login):
        print(f"Bem vindo {cadastro.nome_cadastro} !!!\n")
        break
            
    else:
        print ("Erro nos dados digitados !!!\n")

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
            
        
                            