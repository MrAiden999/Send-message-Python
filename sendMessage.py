#Mr. Aiden creation, it only works on Windows
import pyautogui as p
import time as t

#open Browser
p.moveTo(215, 1062, 0.0)
t.sleep(1)
p.click()
t.sleep(0.5)
p.write('Firefox')
t.sleep(1)
firefox = p.moveTo(153, 392, 0.5)
p.doubleClick(firefox)

#search bitcoin value
t.sleep(3)
p.write('bitcoin valore')
t.sleep(1)
p.press('enter')
t.sleep(1.5)
p.moveTo(240, 341)
p.doubleClick(button = 'left')
p.dragTo(630, 429, 0.5)
p.hotkey('ctrl', 'c') #copy
t.sleep(2)

#new page
new_page = p.moveTo(300, 0, 0.0)
t.sleep(1)
p.click(new_page)
t.sleep(0.5)
p.write('https://web.whatsapp.com/')#open whatsapp
t.sleep(1)
p.press('enter')
t.sleep(2)
cerca = p.moveTo(190, 220, 0.0)#search contact
t.sleep(7)
p.click(cerca)
p.write('Bot')#my group
t.sleep(1)
contatto = p.moveTo(190, 375, 0.0)
p.click(contatto)
t.sleep(3.5)
p.hotkey('ctrl', 'v')#paste
p.press('enter')#send message
