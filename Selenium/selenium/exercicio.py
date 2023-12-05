### LOGANDO EM UMA CONTA DE EMAIL ###

#Importa as bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import by
from selenium.webdriver.common.by import By
import time

# Instancia um navegador

navegador = webdriver.Chrome()

navegador.get('https://www.anhanguera.com/')

elemento = navegador.find_element(By.CLASS_NAME,"menu-btn")
elemento.click()
time.sleep(3)

elemento.find_element(By.XPATH,'//*[@id="vueApp"]/div/div/a[20]')
elemento.click()
time.sleep(3)

