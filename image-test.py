import pyautogui as pg

print("skript jede\n")

btnMove = pg.locateCenterOnScreen('btn-move-middle.png')
locPath = pg.locateOnScreen('path.png')

if locPath != None:
	print("našel jsem screenshot path")
	print(locPath)
elif btnMove != None:
	print("našel jsem screenshot move\n")
	pg.moveTo(btnMove, duration=0.4, tween=pg.easeInOutQuad)
	pg.click(button='right', clicks=2, interval=0.25)
else:
	print("žádný screenshot jsem nenašel")

