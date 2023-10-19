from menu import* #importando o menu
from exercicio import Calculadora #importando a classe calculadora
calculadora = Calculadora ()

while (True):
        
        menu()# chamamos o menu importado acima

        opcao = int(input()) #pede uma opção de operação para o usuário

        if opcao == 5: ## programa para a execução logo no inicio
            print("Obrigado por utilizar a calculadora !!!!")
            break

        elif opcao != 1 and 2 and 3 and 4:
            print("Digite uma opção válida")
            
        else:

            num1 = int(input("Digite o primeiro numero = ")) #pede o primeiro numero para o usuario
            num2 = int(input("Digite o segundo numero = ")) #pede o segundo numero para o usuario
            
            match opcao:
                case 1: #caso a variavel opcao seja 1 execute a função soma
                    print( calculadora.somar(num1,num2))
                case 2: #caso a variavel opcao seja 1 execute a função subtrair
                    print( calculadora.subtrair(num1,num2))   
                case 3: #caso a variavel opcao seja 1 execute a função subtrair
                    print( calculadora.multiplicacao(num1,num2))   
                case 4: #caso a variavel opcao seja 1 execute a função subtrair
                    print( calculadora.divisao(num1,num2))    
               

