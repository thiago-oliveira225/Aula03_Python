print ("########## Adivinhador de numero #############")

import random
numero_sorteado = random.randint(1,100)
tentativas = 0

while True:

    palpite = int(input("Adivinhe o número:"))
    tentativas += 1

    if (palpite == numero_sorteado):
        print (f"Acertou o número em {tentativas} tentativas")

        break
    elif (palpite < numero_sorteado):   
        print ("Tente um numero maior")
    else: 
        print ("Tente um numero menor")







