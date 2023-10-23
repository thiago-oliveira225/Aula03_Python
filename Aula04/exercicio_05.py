print ("########## Bem vindo a calculadora ############# \n")

while (True):
    print("Escolha uma opção \n")
    print("Opção 1: Adição \n")
    print("Opção 2: Subtração \n")
    print("Opção 3: Multiplicação \n")
    print("Opção 4: Divisão \n")
    print("Opção 5: Sair \n")

    opcao = int(input())    

    if (opcao == 1):
        print ("Adição Selecionada")
        numero1 = int(input("Digite o primeiro numero ="))
        numero2 = int(input("Digite o segundo numero ="))
        resultadoAdicao = numero1 + numero2
        print (f"O resultado da adição é: {resultadoAdicao}\n")

    elif (opcao == 2):
        print ("Subtração Selecionada")
        numero1 = int(input("Digite o primeiro numero ="))
        numero2 = int(input("Digite o segundo numero ="))
        resultadoSubtracao = numero1 - numero2
        print (f"O resultado da subtração é: {resultadoSubtracao}")

    elif (opcao == 3):
        print ("Multiplicação Selecionada")
        numero1 = int(input("Digite o primeiro numero ="))
        numero2 = int(input("Digite o segundo numero ="))
        resultadoMultiplicacao = numero1 * numero2
        print (f"O resultado da subtração é: {resultadoMultiplicacao}")

    elif (opcao == 4):
        print ("Divisão Selecionada")
        numero1 = int(input("Digite o primeiro numero ="))
        numero2 = int(input("Digite o segundo numero ="))
        resultadoDivisao = numero1 / numero2
        print (f"O resultado da subtração é: {resultadoDivisao}") 

    elif (opcao == 5):
    
        print ("Obrigado por utilizar a calculadora !!!")
        break    