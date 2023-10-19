agenda = [{}]

while True:
    print ("Escolha uma opção: \n")
    print("Opção 1: Adicionar um contato na agenda: \n")
    print("Opção 2: Listar todos os contatos: \n")
    print("Opção 3: Verificar um contato específico: \n")
    print("Opção 4: Sair do programa: \n")

    opcao = int(input())

    if opcao == 1:
    
        nomeContato = (input("Digite o nome a ser adicionada = "))
        numeroContato = int(input("Digite o numero a ser adicionado = "))
        contato = {"Nome": nomeContato, "Telefone":numeroContato}
        agenda.append(contato)

    elif opcao == 2:    
        for i in agenda:
            print(i, "\n")

    elif opcao ==3:
        nome = (input("Digite o nome a ser buscado = "))
        if nome in agenda:
            print(f"Nome: {nomeContato}, Telefone: {numeroContato}")
        else:
            print("Contato não existe !!")

    else:
        print("Obrigado por utilizar a agenda")