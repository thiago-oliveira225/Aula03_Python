numero = int(input("Digite um número: "))

resultado = numero % 2
    
if (resultado == 0):
    resultadoFinal = numero/2
    print(f"Esse número tem {resultadoFinal} numeros pares")

elif(resultado == 1):
    resultadoFinal = numero/3
    print(f"Esse número tem {resultadoFinal} numeros pares")

