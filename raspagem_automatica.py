
from grafico import plotar_grafico
import customtkinter
import tkinter as tk
from operator import itemgetter
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd

import pandas as pd
import matplotlib.pyplot as plt

def raspagem():

    lista_produtos = []

    navegador = webdriver.Chrome()

    navegador.get('https://www.mercadolivre.com.br/')

    sleep(2)

    # Obtém o valor do CTkEntry

    pesquisa = seu_produto.get()
    input_place = navegador.find_element(By.ID, 'cb1-edit')

    input_place.send_keys(pesquisa)
    input_place.submit()
    sleep(2)

    page_content = navegador.page_source
    site = BeautifulSoup(page_content, 'html.parser')

    flag_pagina_seguinte = True

    while flag_pagina_seguinte == True:

        produtos = site.findAll('div', attrs={'class': 'ui-search-result'})

        for produto in produtos:
            h_ref = produto.find('a')
            preco = produto.find('span', attrs={'aria-roledescription': 'Preço'}).contents[1].text
            preco = preco.replace('.', '')
            preco = preco.replace(',', '.')
            preco = float(preco)

            lista_produtos.append([h_ref['title'], "{:.2f}".format(preco), h_ref['href'], preco])
        try:
            btn_seguinte = navegador.find_element(By.XPATH, value="//a[@title='Seguinte']") 
            navegador.execute_script("arguments[0].click();", btn_seguinte)
            
        except:
            flag_pagina_seguinte = False
            pass

    lista_ordenada =  sorted(lista_produtos, key = itemgetter(3))

    for item in lista_ordenada:
        del item[3]

    arq_produtos = pd.DataFrame(lista_ordenada, columns=['Título', 'Preço', 'Link'])
    arq_produtos.to_excel(f'{pesquisa}.xlsx', index=False)


def plotar_grafico():
    ranking_vendas = (f'{seu_produto.get()}.xlsx')
    df_grafico = pd.read_excel(ranking_vendas)    


    df_grafico.plot(x='Título', y='Preço', kind="bar")


    plt.title("Pesquisa de produto")

    plt.xlabel("Título")
    plt.ylabel("Preço")
    plt.show()       


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme ("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")


texto = customtkinter.CTkLabel (janela, text = "Digite o produto que deseja: ")
texto.pack(padx = 10, pady = 10)

seu_produto_var = tk.StringVar()
seu_produto = customtkinter.CTkEntry(janela, textvariable=seu_produto_var, placeholder_text="Seu produto")
seu_produto.pack(padx=10, pady=10)

# Cria um botão para salvar o produto
botao1 = customtkinter.CTkButton (janela, text = "Pesquisar", command=raspagem)
botao1.pack (padx = 10, pady = 10)

botao2 = customtkinter.CTkButton (janela, text = "Plotar Gráfico", command=plotar_grafico)
botao2.pack (padx = 10, pady = 10)


janela.mainloop()