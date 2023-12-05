import requests
from bs4 import BeautifulSoup

def pesquisar_no_mercado_livre():
    #solicitar uma pesquisa do usuário
    produto_pesquisa= input ("Qual produto você está procurando: ")

    #Substituir os espacos por '+' para formatar corretamente a URL
    produto_pesquisa= produto_pesquisa.replace ('', '+')

    #URL de pesquisa do Mercado Livre

    url= f'https://www.mercadolivre.com.br/{produto_pesquisa}'

    response = requests.get(url)
        #Verificar se a solicitação foi bem-sucedida (código status 200)


    if response.status_code == 200:
        #Criar um objeto BeautifulSoup para analisar o conteúdo da pagina de pesquisa
        soup = BeautifulSoup(response.text, 'html.parser')

        #Encontrar todos os elementos HTML correspondentes a pesquisa

        resultados = soup.find_all ('li', class_='ul-search-layout__item')

        #Exibir informações sobre os primeiros resultados

        for resultado in resultados[:5]: # Exibe os 5 pri,eiros resultados
            nome_produto = resultado.find('h2', class_='ui-search-item__title').text
            preco_produto = resultado.find('spam', class_='price-tag-fraction').text
            link_produto = resultado.find('a', class_='ui-search-link')['href']

            print(f'Produto: {nome_produto}')
            print(f'Produto: {preco_produto}')
            print(f'Produto: {link_produto}')
    else:
        print(f"A solicitação falhou status {response.status_code}")

pesquisar_no_mercado_livre()     