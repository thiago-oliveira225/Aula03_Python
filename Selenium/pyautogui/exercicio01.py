import pyautogui
import time

#Abrir o paint
pyautogui.press ('winleft')
programa = 'Bloco de Notas'
pyautogui.write (programa)
pyautogui.press ('enter')

#Aguarda a abertura do programa
time.sleep(2)

# Escreve no bloco de notas
frase = 'Curso de Python'
pyautogui.write (frase)

# salva o arquivo

pyautogui.hotkey('Ctrl', 'S')
save = 'teste.txt'
pyautogui.write (save)
pyautogui.press ('enter')
