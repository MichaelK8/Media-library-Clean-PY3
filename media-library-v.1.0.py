# Author: Jiri Svab
# screen resolution needed: width=2560, height=1440
# dependencies: Python3, PyAutogui
# notes: Taking the tasks "Move To" from HOME (alt+h) menu
# notes: Browser zoom level needs to be 100%
# notes: PyAutogui doesnt support dual monitors currently (21/10/19). 
# notes: Nevertheless it is recommended to launch this program in separate screen.

import pyautogui, sys

for x in range(2): # run throught this program x times
    pyautogui.click( x=115, y=505, clicks=1, interval=1, button='left' ) # starting location of mouse
    pyautogui.PAUSE = 1.50 # make a pause between each instruction
    pyautogui.click( button='right' ) # open mouse submenu
    pyautogui.move(40, 190) # move mouse to menu item "copying"
    pyautogui.click(button='left') # click on "copying"
    pyautogui.move(310, 33) # move mouse to submenu item "Move To"
    pyautogui.click(button='left') # click on "Move To"
    pyautogui.move(1315, 363) # move mouse to "Path:"
    pyautogui.click(button='left') # click on "Path:"
    pyautogui.hotkey('ctrl', 'a') # select all
    pyautogui.typewrite('/sitecore/media library/uncategorized') # Write the path of uncatogorized folder
    pyautogui.move(0, 90) # move mouse over button "Move"
    pyautogui.click(button='left') # click on "Move"
