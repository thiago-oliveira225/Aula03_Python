class Filme:
    def __init__(self, titulo, genero, duracao, disponivel = True):
        self.titulo = titulo    
        self.genero = genero
        self.duracao = duracao
        self.disponivel = disponivel

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"Filme: {self.titulo} \n, {self.genero} \n, Duração: {self.duracao} minutos \n Status: {status}"
    
    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            return "Filme alugado com sucesso"
        else:
            return "Este filme não está disponível para locação."
        
    def devolver (self):
        if not self.disponivel:
            self.disponivel = True
            return "Filme devolvido com sucesso"
        else:
            return "Este filme já está disponivel"    





      