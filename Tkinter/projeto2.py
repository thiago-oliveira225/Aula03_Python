from tkinter import *


def mensagem():
    texto_teste.config(text="Teste1")


janela = Tk()
janela.title ("Banco de Talentos")

texto_orientacao = Label(janela, text= "Clique na opção desejada" )
texto_orientacao.grid (column=0, row=0)

botao = Button(janela, text= "Opção 1. Incluir Candidato", command=mensagem)
botao.grid (column=0, row=1)

texto_teste = Label (janela, text="")
texto_teste.grid (column=0, row=2)



janela.mainloop()

    


