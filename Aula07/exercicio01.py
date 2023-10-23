print ("########## Bem vindo a calculadora ############# \n")
from menu import* #importando o menu

while (True):
        
        menu()# chamamos o menu importado acima

        opcao = int(input()) #pede uma opção de operação para o usuário

        if opcao == 5: ## programa para a execução logo no inicio
            print("Obrigado por utilizar a calculadora !!!!")
            break    

        num1 = int(input("Digite o primeiro numero = ")) #pede o primeiro numero para o usuario
        num2 = int(input("Digite o primeiro numero = ")) #pede o segundo numero para o usuario

        def soma(num1, num2):## no parametro estão as duas variaveis solicitadas para o usuário no input
            return print(f"O Resultado da Soma é {num1 + num2}") ## aqui está a ação que a função deverá fazer com as variaveis, ou seja somar e printar

        def subtracao(num1, num2):
            return print(f"O Resultado da Subtração é {num1 - num2}")

        def multiplicacao(num1, num2):
            return print(f"O Resultado da Multiplicação é {num1 * num2}")

        def divisao(num1, num2):
            return print(f"O Resultado da Divisão é {num1 / num2}")
        
        match opcao:
            case 1: #caso a variavel opcao seja 1 execute a função soma
                soma(num1,num2)
            case 2:
                subtracao(num1,num2)
            case 3:
                multiplicacao(num1,num2) 
            case 4:
                divisao(num1,num2)






















