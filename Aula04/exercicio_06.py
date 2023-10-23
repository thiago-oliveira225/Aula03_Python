lista = [1,3,15,256,45,185,10,30,20,40,50,10,1,2,10,45,16,25]

lista.reverse() #inverte a ordem da lista
print(lista)

lista.sort() #coloca a lista em ordem crescente
print (lista)

cumprimento_lista = len(lista) # conta quantos elementos tem na lista
print (cumprimento_lista)

maxLista = max(lista) # exibe o numero maximo da lista
minLista = min(lista) # exibe o numero minimo da lista
print (maxLista)
print (minLista)

contagem = lista.count(25) # exibe quantas vezes o numero escolhido aparece na lista
print(contagem)

lista.append(100) #append inclui o numero escolhido na sequencia da lista
print(lista)

lista.remove(100) #remove o item escolhido da lista
print(lista)




