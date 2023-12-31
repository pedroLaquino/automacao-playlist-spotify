import pyautogui
from time import sleep
import time

#clicar no spotify
pyautogui.click(316,1062)
time.sleep(3)
#maximizar janela
pyautogui.click(1678,116)
time.sleep(1)
#buscar
pyautogui.click(91,125)
time.sleep(1)
#digitar nome do artista
pyautogui.write('Kweller')
time.sleep(2)
#clicar perfil do artista
pyautogui.click(602,334)
time.sleep(1)
#clicar e arrastar
x_inicial, y_inicial = 1477,188
x_final, y_final = 1477,361
pyautogui.mouseDown(x=x_inicial, y=y_inicial)
pyautogui.moveTo(x_final, y_final, duration=1.0)
pyautogui.mouseUp()
time.sleep(1)
#clicar em mostrar todas musicas
pyautogui.click(1419,326)
time.sleep(1)
#clicar no lançamento
pyautogui.click(539,273)
time.sleep(1)
#adicionar na playlist
pyautogui.rightClick(900,566)
time.sleep(1)
x_final1, y_final1 = 1011,597
pyautogui.dragTo(x_final1, y_final1, duration=0)
time.sleep(1)
pyautogui.click(1269,115)
time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.press('delete')
time.sleep(1)
pyautogui.write('Kweller - Todas')
time.sleep(1)
pyautogui.click(1264,188)
#voltar na busca e procurar playlist
pyautogui.click(91,125)
time.sleep(1)
pyautogui.write('Kweller - Todas')
time.sleep(2)
pyautogui.click(614,322)
#colocar a música no topo
x_inicial3, y_inicial3 = 1477,100
x_final3, y_final3 = 1477,904
pyautogui.mouseDown(x=x_inicial3, y=y_inicial3)
pyautogui.moveTo(x_final3, y_final3, duration=1.0)
pyautogui.mouseUp()
time.sleep(1)
pyautogui.click(847,259)
time.sleep(1)
pyautogui.hotkey('ctrl', 'x')
time.sleep(1)
x_inicial2, y_inicial2 = 1477,904
x_final2, y_final2 = 1477,100
pyautogui.mouseDown(x=x_inicial2, y=y_inicial2)
pyautogui.moveTo(x_final2, y_final2, duration=1.0)
pyautogui.mouseUp()
time.sleep(2)
pyautogui.click(715,491)
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
x_inicial4, y_inicial4 = 747,554
x_final4, y_final4 = 747,485
pyautogui.mouseDown(x=x_inicial4, y=y_inicial4)
pyautogui.moveTo(x_final4, y_final4, duration=1.0)
pyautogui.mouseUp()