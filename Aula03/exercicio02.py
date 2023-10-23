print ("########## Identificador de Voto #############")

idade = int(input("Digite a sua idade ="))


if (idade < 16):
    print( "Não Pode Votar")
elif (idade >= 16 and idade <18):
    print( "Voto Facultativo")
elif (idade > 18 and idade <66):
    print("Voto Obrigatório")   
else:
    print("Voto Facultativo")    


