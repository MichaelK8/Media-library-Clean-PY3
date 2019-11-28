# Author: Jiri Svab
# screen resolution needed: width=2560, height=1440
# dependencies: Python3, PyAutogui
# notes: Taking the tasks "Move To" from HOME (alt+h) menu
# notes: Browser zoom level needs to be 100%
# notes: PyAutogui doesnt support dual monitors currently (21/10/19).
# notes: Nevertheless it is recommended to launch this program in separate screen.

import pyautogui, sys

for x in range(10): # run throught this program x times
    pyautogui.PAUSE = 0.30 # make a pause between each instruction
    pyautogui.click( x=200, y=1285, clicks=2, interval=0.5, button='left') # starting location of mouse
    pyautogui.hotkey('alt', 'h') # opens HOME menu
    pyautogui.moveTo(690, 360, 1, pyautogui.easeInOutQuad) # move mouse over "Move To" in HOME menu
    pyautogui.click(button='left') # click mouse on "Move To" in HOME menu
    pyautogui.moveTo(1834, 1127, duration=4.4, tween=pyautogui.easeInOutQuad) # move mouse to "Path:"
    pyautogui.click(button='left') # click on "Path:"
    pyautogui.hotkey('ctrl', 'a') # select all
    pyautogui.typewrite('/sitecore/media library/Images/LeicaGeosystems/Products/uncategorized-products') # Write the path of uncatogorized folder
    pyautogui.move(0, 90, 1, pyautogui.easeInOutQuad) # move mouse over button "Move"
    pyautogui.click(button='left') # click on "Move"
    pyautogui.move(-190,0, duration=5.9)
