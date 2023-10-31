class Animal:
    def mover(self):
        pass        

class Peixe(Animal):
   def mover(self):
       return "Nadando"

class Ave(Animal):
    def mover(self):
        return "Voando"
      
peixe = Peixe()
ave = Ave()

print(peixe.mover())
print(ave.mover())