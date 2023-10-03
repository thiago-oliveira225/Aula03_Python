print ("######## Identificador de legibilidade para voto ###########")

idade = int(input("Digite a sua idade = "))

if (idade < 16):
    print ("Não pode votar")

elif (idade >= 16 and idade <18):
    print ("Voto facultativo")

elif (idade >= 18 and idade <=66):
    print ("Voto obrigatório")

else:
    print ("Voto facultativo")
