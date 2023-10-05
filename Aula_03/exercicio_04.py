dia = input("Digite um dia da semana no formato/ Exemplo: Segunda-Feira =")


if (dia == "Segunda-Feira" or dia == "Terça-Feira" or dia == "Quarta-Feira" or dia == "Quinta-Feira" or dia == "Sexta-Feira"):
    print("Dia útil")
elif (dia == "Sábado" or dia == "Domingo"):
    print("Final de Semana")
else:
    print("Formato inválido")