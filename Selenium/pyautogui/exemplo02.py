import pyautogui
import time

#Abrir o paint
pyautogui.press ('winleft')
programa = 'Paint'
pyautogui.write (programa)
pyautogui.press ('enter')

#Aguarda a abertura do programa
time.sleep(3)

#Mover o cursor para área de desenho

x=600
y = 500

pyautogui.moveTo(x,y)

#Função para desenhar estrela

def desenhar_estrela (x, y, tamanho):
    pyautogui.click(x,y) # clica no ponto inicial do Paint

    #Calcular os pontos da estrela

    pontas = 5
    angulo = 360 / pontas
    raio_externo = tamanho
    raio_interno = tamanho/2

    for i in range (pontas*2):
        if i % 2 != 0:
            pyautogui.dragRel (raio_interno, 0, duration = 1)
            #Desenha a linha interna
        else:
            pyautogui.dragRel (raio_externo, 0, duration=1)
            #Desenha a linha externa
        pyautogui.moveRel(0,0)    

#Aguardar alguns segundos
time.sleep(5)

#Coordenadas do ponto inicial e tamanho da estrela
x_inicial, y_inicial = 100
tamanho_estrela = 50

desenhar_estrela (10,5,5)