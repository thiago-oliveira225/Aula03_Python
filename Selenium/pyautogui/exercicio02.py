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

# Copia o texto 
pyautogui.hotkey('Ctrl', 'A')
pyautogui.hotkey('Ctrl', 'C')

# Abre o outro bloco de notas
pyautogui.press ('winleft')
programa1 = 'Bloco de Notas'
pyautogui.write (programa1)
pyautogui.press ('enter')
time.sleep(2)

# Cola o texto copiado
pyautogui.hotkey('Ctrl', 'V')

#Aguarda a abertura do programa
time.sleep(2)

