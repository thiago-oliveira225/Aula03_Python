# Lista de tarefas
tarefas = []

while True:
    print("1. Adicionar tarefa")
    print("2. Marcar tarefa como concluída")
    print("3. Exibir tarefas pendentes")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        tarefa = input("Digite a tarefa a ser adicionada: ")
        tarefas.append(tarefa)
        
    elif escolha == "2":
        if tarefas:
            print("Tarefas pendentes:")
            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1}. {tarefa}")
            numero = int(input("Digite o número da tarefa concluída: ")) - 1
            if 0 <= numero < len(tarefas):
                del tarefas[numero]
            else:
                print("Número de tarefa inválido.")
        else:
            print("Não há tarefas pendentes.")
    elif escolha == "3":
        if tarefas:
            print("Tarefas pendentes:")
            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1}. {tarefa}")
        else:
            print("Não há tarefas pendentes.")
    elif escolha == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")
