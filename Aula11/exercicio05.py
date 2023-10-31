funcionarios = {}


class Funcionario:

    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self, nome, salario_base):
        if nome not in funcionarios:
            funcionarios[nome] = {"Salário": salario_base}
        else:
            print("Funcionário já existe no sistema")


class CLT(Funcionario):
   def calcular_salario(self):
        pass

class Comissionado(Funcionario):
    def calcular_salario(self):
        pass
    
class Estagiario(Funcionario):
    def calcular_salario(self):
        pass    
      

clt = CLT("Thiago", "3500")
comissionado = Comissionado()
estagiario = Estagiario()


print(clt.calcular_salario())
print(comissionado.calcular_salario())
print(estagiario.calcular_salario())