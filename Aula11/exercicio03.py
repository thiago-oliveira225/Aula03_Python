class Shape:
    def calcular_area(self):
        pass

class Circulo(Shape):
    def calcular_area(self,raio):
        return f"A área do circulo é de {3.14*raio*raio}cm"

class Retangulo(Shape):
    def calcular_area(self,lado1,lado2):    
        return f"A área do retangulo é de {3.14*lado1*lado2}cm"

circulo = Circulo()
retangulo = Retangulo()      

print (circulo.calcular_area(10))
print (retangulo.calcular_area(5,10))


