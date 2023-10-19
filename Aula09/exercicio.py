class Calculadora:
    

    def somar(self, a,b):
        return (f"O Resultado da soma é {a + b}")
    def subtrair(self,a,b):
        return (f"O Resultado da subtração é {a - b}")
    def multiplicacao(self,a,b):
        return (f"O Resultado da multiplicação é {a * b}")
    def divisao(self,a,b):
        if b==0:
            return("Não é possível dividir por zero")
       
        return(f" O Resultado da divisão é {a / b}")
                
    

    