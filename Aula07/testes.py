nomes = ["João", "Pedro", "Thiago", "José", "Taís"] #chaves
profissoes = ["Professor", "Médico", "Programador", "Dentista", "Psicóloga"] #valores

profissionais = {nome: profissao for nome, profissao in zip(nomes, profissoes)} #Junta duas listas e um dicionario

del profissionais["João"] #apaga uma chave de um dicionario, juntamente com seu valor

profissionais ["Felipe"] = "Arquiteto" #adiciona ao final da lista essa nova chave e valor

profissionais ["Fulanos"] = profissionais.pop("Pedro") # substitui o nome de uma chave especifica
