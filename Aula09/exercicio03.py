class Pessoa:
    total_pessoas = 0 ## atributo da classe

    def __init__(self,nome,idade): ## método construtos
        self.nome = nome
        self.idade = idade
        Pessoa.total_pessoas += 1

pessoa1 = Pessoa ("Alice", 25)
pessoa2 = Pessoa ("Bob", 25)
pessoa3 = Pessoa ("João", 25)

print(Pessoa.total_pessoas)
