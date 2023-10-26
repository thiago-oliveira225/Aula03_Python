### class Agenda = []
## metodo adicionar, listar, buscar, apagar contato

class Agenda:
    def __init__(self, nome):
        self.nome = nome
        self.contatos = []

    def adicionar_contato(self,contato):
        self.contatos.append(contato)  

    def listar_contatos(self):
        for contato in self.contatos:
            print(contato)  

    def buscar_contatos(self,nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None

    def remover_contato(self, nome):
        if nome in self.contatos:
            self.contatos.remove(nome)
            print (f" Contato {nome} removido com sucesso !!!") 
        else:
            print (f"Contato {nome} não encontrado na agenda ")      




    """def listar_catalogo(self):
        print(f"Catálogo da Locadora{self.nome}: ")
        for filme in self.catalogo:
            print(filme)

            
        self.nomeContato = (input("Digite o nome a ser adicionada = "))
        self.numeroContato = int(input("Digite o numero a ser adicionado = "))
        self.contato = {"Nome": self.nomeContato, "Telefone":self.numeroContato}
        self.lista_contatos.append(contato)
        print ("Contato Adicionado")


    def listar_contatos(self):
        print(f"Lista de Contatos{self.nome}: ")
        for contato in self.lista_contatos:
            print(contato)"""