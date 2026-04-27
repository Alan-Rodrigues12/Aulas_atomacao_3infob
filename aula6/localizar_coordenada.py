import pyautogui

#opcão1:
#localiza uma imagem na tela e retorna uma caixa, com coordenada x e y do ponto inicial da caixa left+top
xy = pyautogui.locateOnScreen('aula6\\btn_8.png', confidence=0.9)
centro_box = pyautogui.center(xy)
print(centro_box)

#opcão2:

xy2 = pyautogui.locateCenterOnScreen('aula6\\btn_8.png', confidence=0.95)
print(xy2) 

