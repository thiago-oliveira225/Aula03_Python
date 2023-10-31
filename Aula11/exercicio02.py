class Veiculo:
    def mover(self):
        pass        

class Carro(Veiculo):
   def mover(self):
       return "Dirigindo"

class Aviao(Veiculo):
    def mover(self):
        return "Voando"
      
carro = Carro()
aviao = Aviao()

print(carro.mover())
print(aviao.mover())

    


