def menu():
    print ("\n############## Bem vindo ao controle sistema oficina ################\n")
    print ("Escolha uma das opções abaixo\n")
    print ("Opção1. Inserir um cliente no sistema")
    print ("Opção2. Ler os dados do sistema")
    print ("Opção3. Atualizar dados do sistema")
    print ("Opção4. Apagar um item do sistema")
    print ("Opção5. Sair do programa")

def incluir_clientes():
    nome = input("Digite o nome do cliente = ")
    telefone = int(input("Digite o telefone do cliente = "))
    email = input ("Digite o email do cliente = ")
    print(" Cliente incluído com sucesso\n")
    print("nome:", nome, "\n")
    print("telefone:", telefone, "\n")
    print("email:", email, "\n")
    

def incluir_veiculo():
    marca = input("Digite a marca do veículo = ")
    modelo = input("Digite o modelo do veículo = ")
    ano = int(input("Digite o ano do véiculo = "))
    print(" Veículo incluído com sucesso\n")
    print("marca:", marca, "\n")
    print("modelo:", modelo, "\n") 
    print("ano:", ano, "\n")