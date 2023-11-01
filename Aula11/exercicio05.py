funcionarios = {} ## DICIONARIO VAZIO PARA INCLUIR OS FUNCIONARIOS


class Funcionario: ## CLASSE MÃE

    def __init__(self, nome, salario_base): ## METODO CONSTRUTOR COMUM PARA TODOS OS TIPOS DE FUNCIONARIOS
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self): ## APENAS ATRELANDO ESSE METODO NA CLASSE MAE PARA SER UTILIZADO PARA AS CLASSES FILHAS
        pass


class CLT(Funcionario): ## CLASSE FILHA
   def calcular_salario(self):
        funcionarios[self.nome] = {"Contrato":"CLT","Salário": (self.salario_base)}
        

class Estagiario(Funcionario):

    def calcular_salario(self):
        funcionarios[self.nome] = {"Contrato":"Estágio","Salário": self.salario_base / 2}
        


class Comissionado(Funcionario):
    def __init__(self, nome, salario_base, comissao):
        self.comissao = comissao
        super().__init__(nome, salario_base)

    def calcular_salario(self):
        funcionarios[self.nome] = {"Contrato":"Comissionado","Salário": self.salario_base + self.comissao}
        

## PROGRAMA MAIN

while True:
    print(" Escolha uma opção = ")
    print(" Opção 1. Incluir Funcionário CLT ")
    print(" Opção 2. Incluir Funcionario Comissionado ")
    print(" Opção 3. Incluir Funcionário Estagiário ")
    print(" Opção 4. Mostrar todos os Funcionários ")
    print(" Opção 5. Sair \n")
    

    opcao = input("")

    match opcao:
    
        case "1":       

            clt = CLT(input ("Digite o nome do Funcionario = "), int(input ("Digite o salário do Funcionario = ")))

            clt.calcular_salario()

            print (f"\n#### Funcionário incluído com sucesso ####\n")

        case "2": 

            comissionado = Comissionado((input ("Digite o nome do Funcionario = ")), int(input ("Digite o salário do Funcionario = ")), int(input ("Digite a comissao do Funcionario = ")))

            comissionado.calcular_salario()

            print (f"\n#### Funcionário incluído com sucesso ####\n")

        case "3": 

            estagiario = Estagiario (input ("Digite o nome do Funcionario = "), int(input ("Digite o salário referencia do CLT = ")))

            estagiario.calcular_salario()

            print (f"\n#### Funcionário incluído com sucesso ####\n")

        case "4": 

            print (funcionarios)


        case "5": 

            print("#######  Obrigado por utilizar o Programa de Funcionários ####### ")

            break

        case _:
            print("\nEscolha uma opção válida !!!!\n")
