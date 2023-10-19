estoque = {}

def menu():
    print ("\n############## Bem vindo ao controle de estoque ################\n")
    print ("Escolha uma das opções abaixo\n")
    print ("Opção1. Inserir um item no estoque")
    print ("Opção2. Ler o itens do estoque")
    print ("Opção3. Atualizar quantidade de um item do estoque")
    print ("Opção4. Apagar um item do estoque")
    print ("Opção5. Sair do programa")



def inserirItem(codigo,item,quantidade):
    if codigo not in estoque: # checando se o item ja consta no dicionario
        estoque[codigo] = {"item":item, "quantidade": quantidade} ## criando os itens dentro do dicionario referenciando pelo codigo
        print(f"Item {item} adicionado com sucesso !!! ")
    else:
        print(f"O item ja contém no estoque, digite a opção 2 para checar")

def ler_Itens ():
    for item in estoque:
        print(estoque[item])

def atualizar_Quantidade (codigo):
    if codigo in estoque:
        nova_Quantidade = int(input("Digite a nova quantidade do item = "))
        estoque[codigo]["quantidade"]= nova_Quantidade 
        print(f"Quantidade atualizada com sucesso !!! ")
    else:
        print("Item não encontrado no estoque") 

def apagar_Item (codigo):
    if codigo in estoque:
        del estoque[codigo]
        print("Item excluido com sucesso !!! ")   
    else:
        print("Item não encontrado no estoque")

def sair ():     
    print("Obrigado por utilizar o programa !!!!")
    

while True:

    menu()

    opcao = int(input())

    match opcao:
        case 1:
            codigo = int(input("Digite o código do item = "))
            item = (input("Digite o o nome do item = "))
            quantidade = int(input("Digite o a quantidade do item = "))
            inserirItem(codigo, item, quantidade)

        case 2:
            ler_Itens()

        case 3:
            codigo = int(input("Digite o código do item que deseja atualizar = "))
            atualizar_Quantidade(codigo)

        case 4:
            codigo = int(input("Digite o código do item que deseja apagar = "))
            apagar_Item(codigo)

        case 5:
            sair()
            break       

 
    
    
    
    
    
    
    
    
    
    
    
    
