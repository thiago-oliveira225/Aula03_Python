filmes_acao = ["Filme A", "Filme B", "Filme C"]
filmes_suspense = ["Filme D", "Filme E", "Filme F"]

class Filmes_Generos:

    def menu_generos():
        print("\nEscolha uma opção de gênero do filme = ")
        print(" Opção 1. Ação ")
        print(" Opção 2. Suspense ")
        print(" Opção 3. Sair ")

        opcao_genero = int(input("Digite a sua opção = "))

        if opcao_genero == 1:
            print (f" Esses são os filmes de ação {filmes_acao}\n")

            while True:
            
                escolha_filme = input ("Digite qual filme deseja assistir = ")

                if escolha_filme in filmes_acao:
                    print (f"{escolha_filme} selecionado com sucesso, !!! \n")
                    print ("                ### BOM FILME ###               ")
                    break 

                else:
                    print (f"Filme não encontrado, escolha uma opção válida !!! \n")

    
        elif opcao_genero == 2:
            print (f" Esses são os filmes de suspense{filmes_suspense}")

        else:
            print ("### Obrigado por utilizar o Senai Flix ###")

    