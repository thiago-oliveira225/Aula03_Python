import requests
from bs4 import BeautifulSoup

def pesquisar_no_mercado_livre():
    # Solicitar uma pesquisa do usuário
    produto_pesquisa = input("Qual produto você está procurando: ")

    # Substituir os espaços por '+' para formatar corretamente a URL
    produto_pesquisa = produto_pesquisa.replace(' ', '+')

    # URL de pesquisa do Mercado Livre
    url = f'https://lista.mercadolivre.com.br/{produto_pesquisa}'

    # Enviar uma solicitação GET para a página de pesquisa
    response = requests.get(url)

    # Verificar se a solicitação foi bem-sucedida (código status 200)
    if response.status_code == 200:
        # Criar um objeto BeautifulSoup para analisar o conteúdo da página de pesquisa
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar todos os elementos HTML correspondentes à pesquisa
        resultados = soup.find_all('li', class_='ui-search-layout__item')

        # Exibir informações sobre os primeiros resultados
        for resultado in resultados[:5]:  # Exibe os 5 primeiros resultados
            nome_produto = resultado.find('h2', class_='ui-search-item__title').text

            # Procurar pelo elemento de preço correto
            preco_produto_element = resultado.find('span', class_='price-tag-fraction')
            preco_produto = preco_produto_element.text if preco_produto_element else 'Preço não disponível'

            link_produto = resultado.find('a', class_='ui-search-link')['href']

            print(f'Produto: {nome_produto}')
            print(f'Preço: {preco_produto}')
            print(f'Link: {link_produto}')
            print('-' * 30)
    else:
        print(f"A solicitação falhou. Status: {response.status_code}")

pesquisar_no_mercado_livre()
