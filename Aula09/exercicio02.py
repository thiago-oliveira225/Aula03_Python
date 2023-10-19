class Aluno:
    def __init__(self, nome, idade, nota1, nota2, nota3):
        self.nome = nome
        self.idade = idade
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcula_media(self, nota1, nota2, nota3):
        media = ((nota1 + nota2 + nota3)/3)
        return (media)

    def aprovacao(self,media):
        if media >=6:
            print("Aluno Aprovado")
        else:
            print("Aluno Reprovado")    

teste = Aluno("Thiago", 28, 2, 3 ,6)

print (teste.aprovacao())