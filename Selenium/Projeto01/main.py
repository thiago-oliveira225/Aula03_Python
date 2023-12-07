from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# Configurando o ChromeDriver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Passo 1: Navegando para o site
navegador.get('https://www.amazon.com.br/')



campo_firstname = navegador.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
campo_firstname.send_keys("celular motorola 256gb")


campo_firstname2 = navegador.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]')
campo_firstname2.click()

campo_firstname3 = navegador.find_element(By.XPATH, '//*[@id="p_36/17270946011"]/span/a/span')
campo_firstname3.click()




input("Pressione Enter para fechar o navegador...")

# Passo 2: Inserindo texto em um campo no site

# Fechar o navegador
navegador.quit()

'''from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Para simular a tecla "Enter"
import time

# Inicializa o driver (no exemplo, é utilizado o Chrome)
driver = webdriver.Chrome()  # Certifique-se de ter o driver do navegador para essa linha funcionar

# Acessa a URL desejada
driver.get('https://www.youtube.com')

# Encontra um elemento utilizando XPath e insere texto
elemento_texto = driver.find_element(By.XPATH, '//*[@id="search"]')  # Substitua o XPath pelo caminho real do elemento
elemento_texto.send_keys("Música Gospel")
time.sleep(2)  # Tempo para aguardar a inserção do texto

# Pressiona Enter para realizar a busca
elemento_texto.send_keys(Keys.RETURN)

time.sleep(5)  # Tempo para visualizar a página após a busca

# Aumenta o tempo para visualizar a página antes de fechar o navegador
time.sleep(10)

# Fecha o navegador
driver.quit()'''










