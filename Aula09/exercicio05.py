class Tarefa:   
    def __init__(self,nome_tarefa,data_vencimento): ## método construtor
        self.nome_tarefa = nome_tarefa
        self.data_vencimento = data_vencimento
        self.status = "Pendente"

    def marcar_concluida(self):
        self.status = "Concluída"    

    def verificar_vencimento(self):

        data_tarefa = input("Digite a data da tarefa = ")    
        if self.status == "Pendente" and self.data_vencimento < data_tarefa:
            return (f"A tarefa {self.nome_tarefa} está atrasada")
        elif:
            return (f"A tarefa {self.nome_tarefa} está em dia")
    
tarefa1 = Tarefa("Passear com cachorro", "2023-10-17")

print(tarefa1.verificar_vencimento())
print(tarefa1.status)

 