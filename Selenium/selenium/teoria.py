#importar bibliotecas do selenium
from selenium import webdriver
import time
import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Instanciar um nagegador

navegador = webdriver.Chrome()

# Navegador para uma URL

try: # Encapsula um código
    navegador.get('https://www.google.com.br/')

    # Encontrar um elemento pelo ID
    elemento = navegador.find_element(By.ID,"APjFqb")
    time.sleep(2)

    # Digite um texto no campo selecionado
    elemento.send_keys("Greve de Metro em São Paulo")
    time.sleep(2)

    # Simula a tecla enter
    elemento.send_keys(Keys.RETURN)
    time.sleep(3)

except:
    print("Erro")

finally:
    navegador.close()
    

