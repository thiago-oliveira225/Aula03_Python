# Automação de interface Desktop
import pyautogui
import time

#Abrir o paint
"""pyautogui.press ('winleft')
programa = 'Paint'
pyautogui.write (programa)
pyautogui.press ('enter')

#Aguarda a abertura do programa
time.sleep(3)

#Mover o cursor para área de desenho

x=600
y = 500

pyautogui.moveTo(x,y)

#Criar um desenho simples

pyautogui.dragTo (600,600, duration=1, button= 'left') #Desenha uma linha simples

pyautogui.dragTo (300,300, duration=1, button= 'right') #Desenha uma linha simplesHello, world!"""
























#Aguardar alguns segundos antes de iniciar
time.sleep(5)

largura, altura = pyautogui.size()
print (f"A largura da tela é: {largura} \n. A altura da tela: {altura}.")

#Mover o mouse para as coordenadas (x,y) e clique

pyautogui.move(100,100, duration=2)
pyautogui.click()

# Digite algo usando o teclado virtual
pyautogui.typewrite ("Hello, world!")

#Obter e imprimir a posição atual do mouse

while True:
    x,y = pyautogui.position()
    print (f"A posição atual do mouse é {x} and {y}.")

    pyautogui.move(108,1063, duration=5)
    pyautogui.click()

    pyautogui.typewrite ("Bloco de notas")
    pyautogui.click()

    #Exibir um alerta

    #pyautogui.alert("Este é um alerta!")Hello, world!