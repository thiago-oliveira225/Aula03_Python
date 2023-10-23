lista_numeros = []
soma = sum(lista_numeros)


while True:

    numero1 = int(input("Digite um numero: "))
    lista_numeros.append(numero1)
    print(lista_numeros)
    print("Digite 1 para incluindo mais numeros ou 2 para tirar a média: " )

    resposta = int(input())

    if (resposta == 1):
        numero2 = int(input("Digite um numero: "))
        lista_numeros.append(numero2)
        print(lista_numeros)
        print("Digite 1 para calcular incluindo mais numeros ou 2 para tirar a média: " )

    else:

        print(soma / lista_numeros.count())
        
        break