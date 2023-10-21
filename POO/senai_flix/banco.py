class Banco:
    def __init__(self, nome, conta, agencia):
        self.nome = nome
        self.conta = conta
        self.agencia = agencia

    def pagamento(self, saldo, valor_aluguel):
        #conta = int(input("Digite o número da sua conta"))
        #agencia = int(input("Digite o número de sua agência"))
        if saldo >= valor_aluguel:
            return saldo - valor_aluguel
        else:
            print("Saldo Insuficiente")

        