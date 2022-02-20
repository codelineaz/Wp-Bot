import webbrowser
import pyautogui
import time
webbrowser.open('https://web.whatsapp.com/')

time.sleep(10)
print(pyautogui.position())
pyautogui.click(184,189)
pyautogui.typewrite('srv')
