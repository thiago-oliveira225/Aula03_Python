lista_tarefas = []
quantidade_tarefas = 0

while True:
    print ("Escolha uma opção: \n")
    print("Opção 1: Adicionar uma tarefa a lista: \n")
    print("Opção 2: Excluir uma tarefa da lista: \n")
    print("Opção 3: Verificar a quantidade de tarefas: \n")
    print("Opção 4: Ordenar as tarefas: \n")
    print("Opção 5: Sair do programa: \n")

    opcao = int(input())

    if opcao == 1:
    
        tarefa1 = (input("Digite a tarefa a ser adicionada = "))
        lista_tarefas.append(tarefa1)
        print (f"Tarefa Adicionada: {lista_tarefas}")
        quantidade_tarefas += 1

    elif opcao == 2:
        print (f"Lista de tarefas atualizada {lista_tarefas}")

        if lista_tarefas == []:
            print ("Não há tarefas para excluir")
        else:
            tarefa2 = (input("Digite a tarefa que deseja remover = "))
            lista_tarefas.remove(tarefa2) 
        
            print (f"Tarefa Removida: {lista_tarefas}")
            quantidade_tarefas = - 1

    elif opcao == 3:
 
        print (f"Essa é a quantidade de tarefas: {quantidade_tarefas} {lista_tarefas}")

    elif opcao == 4:
        lista_tarefas.sort()    
    
        print (f"Tarefas ordenadas: {lista_tarefas}")  

    else:
        print("Obrigado por utilizar o nosso gerenciador de tarefas!!!!!")

        break
