import pyautogui

print(pyautogui.position())

for x in range(2):
	pyautogui.click( x=211, y=866, clicks=1, interval=1, button='left')
	pyautogui.PAUSE = 1.50 # make a pause between each instruction
	pyautogui.click()
	pyautogui.click( button='right' ) # open mouse submenu
	pyautogui.move(40, 190) # move mouse to menu item "copying"
	pyautogui.click(button='left') # click on "copying"
    pyautogui.move(310, 33) # move mouse to submenu item "Move To"
    pyautogui.click(button='left') # click on "Move To"
    pyautogui.move(1315, 363) # move mouse to "Path:"
    pyautogui.click(button='left') # click on "Path:"
    pyautogui.hotkey('ctrl', 'a') # select all
    pyautogui.typewrite('/sitecore/media library/Images/LeicaGeosystems/Products/uncategorized-products') # Write the path of uncatogorized folder
    pyautogui.move(0, 90) # move mouse over button "Move"
    pyautogui.click(button='left') # click on "Move"

