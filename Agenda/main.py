from contatos import Contatos
from agenda import Agenda

def main():

    minha_agenda = Agenda ("Minha Agenda")

    while True:
        print ("Escolha uma opção: \n")
        print("Opção 1: Adicionar um contato na agenda: \n")
        print("Opção 2: Listar todos os contatos: \n")
        print("Opção 3: Verificar um contato específico: \n")
        print("Opção 4: Sair do programa: \n")

        opcao = int(input())

        if opcao == 1:

            minha_agenda.adicionar_contato()
        
            

        '''elif opcao == 2:    
            for i in agenda:
                print(i, "\n")

        elif opcao ==3:
            nome = (input("Digite o nome a ser buscado = "))
            if nome in agenda:
                print(f"Nome: {nomeContato}, Telefone: {numeroContato}")
            else:
                print("Contato não existe !!")

        else:
            print("Obrigado por utilizar a agenda")



    

    minha_agenda = Agenda ("Minha Agenda")

    while True:
        print ("        \nOpções"           )
        print ("Opção 1 - Adicionar Contatos")
        print ("Opção 2 - Listar Contato")
        print ("Opção 3 - Buscar Contato")
        print ("Opção 4 - Apagar Contato")
        print ("Opção 5 -   Sair"          )

        opcao = input ("Escolha uma opção = ")

        if opcao == "1":
            minha_agenda.adicionar_contato()'''


if __name__:
    main()