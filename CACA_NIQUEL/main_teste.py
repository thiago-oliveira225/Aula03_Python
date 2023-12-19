import tkinter as tk

def menu_cn():
    print(" ----------------------------------- ")
    print("       BEM VINDO AO CAÇA NIQUEL      ")
    print(" ----------------------------------- ")
    print("      [1] JOGAR  |   [2] HELP        ")
    print(" ----------------------------------- ")
    print("      [3] SAIR   |   [4] REGISTRO    ")
    print(" ----------------------------------- ")

class TelaTkinter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Menu Caça Níquel")

        # Adicione um rótulo com o texto do menu
        self.label_menu = tk.Label(self, text=menu_cn(), font=("Arial", 12))
        self.label_menu.pack(pady=20)

        # Adicione um botão para cada opção do menu
        self.button_jogar = tk.Button(self, text="JOGAR", command=self.acao_jogar)
        self.button_jogar.pack(pady=10)

        self.button_help = tk.Button(self, text="HELP", command=self.acao_help)
        self.button_help.pack(pady=10)

        self.button_sair = tk.Button(self, text="SAIR", command=self.acao_sair)
        self.button_sair.pack(pady=10)

        self.button_registro = tk.Button(self, text="REGISTRO", command=self.acao_registro)
        self.button_registro.pack(pady=10)

    def acao_jogar(self):
        print("Opção JOGAR selecionada")

    def acao_help(self):
        print("Opção HELP selecionada")

    def acao_sair(self):
        print("Opção SAIR selecionada")

    def acao_registro(self):
        print("Opção REGISTRO selecionada")

# Crie uma instância da sua tela personalizada
tela = TelaTkinter()

# Inicie o loop principal do Tkinter
tela.mainloop()
