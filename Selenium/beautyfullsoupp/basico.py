#Importar a biblioteca BS4

from bs4 import BeautifulSoup
import requests

# URL da página web a ser raspada

url = 'https://www.mercadolivre.com.br/'

# Enviar uma solicitação GET para nossa página

response = requests.get(url)

#Verificar se solicitação foi bem sucedida

if response.status_code ==200:
    #Criar um objeto BeautifulSoup para analisar o nosso conteúdo html da página

    soup = BeautifulSoup (response.text, 'html.parser')

h1 = soup.find('h1')

# Exibir o texto dentro da tag h1

print(f'Título da Página: {h1.text}')

# Exibir todos os elementos HTML correspondente a uma tag específica

#Procura por todos os links na página
todos_links = soup.find_all('a')

#Exibir os URLS de todos os links na pagina
for link in todos_links:
    print(link.get('href'))

# Acessar atributos de um elemento HTML
img_src = soup.find ('img') ['src']   

#Navegar pela arvore DOM, navegar pelo HTML para encontrar elementos alinhados

conteudo_div = soup.find('div', class_='ui-pdp-header__title-container')

#Exibir o texto dentro da tag < div class= 'conteudo'>

print ('Conteudo da Div:')
print (conteudo_div.text.strip())

# Encontrar todos os elementos de uma classe específica

todos_elementos_classe_x = soup.find_all(class_= 'ui-search-result-image__element')

print(todos_elementos_classe_x.text.strip())

#Encontrar o próximo elemento irmão

elemento_filho = title_tag.find_next_sibling ()

#Encontrar elemento pelo selector CSS
elemento_css = soup.select('.minha_classe_css')

