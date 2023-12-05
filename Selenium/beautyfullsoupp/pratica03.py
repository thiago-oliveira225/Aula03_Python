import requests
from bs4 import BeautifulSoup

def pesquisa_amazon():
    #Solicita uma pesqueisa ao usuário
    produto_pesquisa = input ("Qual produto está procurando: ")

    #Substituindo espaços por "+" para formatar corretamente a URL
    produto_pesquisa = produto_pesquisa.replace(' ', '+')

    #URL de pesquisa
    url = f'https://www.amazon.com.br/{produto_pesquisa}'

    # Envia uma solicitação get para a pagina de pesquisa
    response = requests.get(url)

    #Verificar se a solicitação foi bem sucedida (código status 200)
    if response.status_code == 200:
        #Se a condição acima for atendida deve ser criar um objeto BeatifulSoup para analisar o conteúdo da pagina de pesquisa
        soup = BeautifulSoup(response.text, 'html.parser')

        #Encontrar todos os elementos HTML correspondente a seguinte pesquisa