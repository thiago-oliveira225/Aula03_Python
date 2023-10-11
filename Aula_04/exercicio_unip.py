nota1_aluno = float(input("Digite a nota n1 do aluno "))
nota2_aluno = float(input("Digite a nota n2 do aluno "))
n1 = (nota1_aluno * 0.4)
n2 = (nota2_aluno * 0.6)

media = n1 + n2


if (media >= 5):
    print ("Aluno aprovado")

else:
    print ("Aluno reprovado")    
