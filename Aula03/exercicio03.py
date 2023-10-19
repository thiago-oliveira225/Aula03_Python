numero1 = float(input("Digite o primeiro numero ="))
numero2 = float(input("Digite o segundo numero ="))
numero3 = float(input("Digite o terceiro numero ="))

if (numero1 > numero2 and numero1 > numero3):
    print("Dentre os numeros", numero1, numero2, numero3 , "O maior é o:",numero1)
elif (numero2 > numero3 and numero2 > numero1):
    print("Dentre os numeros", numero1, numero2, numero3 , "O maior é o:",numero2)
elif (numero3 > numero1 and numero3 > numero2):
    print("Dentre os numeros", numero1, numero2, numero3 , "O maior é o:",numero3)