while True:

    print("Escolha uma opção \n")
    print("Opção 1: Adição \n")
    print("Opção 2: Subtração \n")
    print("Opção 3: Multiplicação \n")
    print("Opção 4: Divisão \n")
    print("Opção 5: Sair \n")

    opcao = int(input())

    num1Digitado = int(input("Digite o primeiro numero = "))
    num2Digitado = int(input("Digite o primeiro numero = "))

    def soma(num1, num2):#dentro do parenteses é a variavel
        resultado = num1 + num2
        print(f"O resultado da soma é {resultado}")#essa é a mensagem fixa que vai juntar com a variavel da função quando chamar

    num1Digitado = int(input("Digite o primeiro numero = "))
    num2Digitado = int(input("Digite o primeiro numero = "))

    def subtracao(num1, num2):#dentro do parenteses é a variavel
        resultado = num1 - num2
        print(f"O resultado da soma é {resultado}")#essa é a mensagem fixa que vai juntar com a variavel da função quando chamar
    
    num1Digitado = int(input("Digite o primeiro numero = "))
    num2Digitado = int(input("Digite o primeiro numero = "))

    def multiplicacao(num1, num2):#dentro do parenteses é a variavel
        resultado = num1 + num2
        print(f"O resultado da soma é {resultado}")#essa é a mensagem fixa que vai juntar com a variavel da função quando chamar
    
    num1Digitado = int(input("Digite o primeiro numero = "))
    num2Digitado = int(input("Digite o primeiro numero = "))

    def divisao(num1, num2):#dentro do parenteses é a variavel
        resultado = num1 + num2
        print(f"O resultado da soma é {resultado}")#essa é a mensagem fixa que vai juntar com a variavel da função quando chamar
    
    match opcao:
        case 1:
            soma(num1Digitado,num2Digitado)
        case 2:
            subtracao(num1Digitado,num2Digitado)
        case 3:
            multiplicacao(num1Digitado,num2Digitado) 
        case 4:
            divisao(num1Digitado,num2Digitado)    
        case 5:
            print("Obrigado por utilizar a calculadora !!!!")
            break
    
   

