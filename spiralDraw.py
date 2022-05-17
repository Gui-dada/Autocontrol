import pyautogui ,time
time.sleep(5)
pyautogui.click()#点击画画
distance = 200
while distance > 0:
    pyautogui.dragRel(distance,0,duration=0.2)#向右移动
    distance -=5
    pyautogui.dragRel(0,distance,duration = 0.2)#向下移动
    pyautogui.dragRel(-distance,0,duration = 0.2)#向👈移动
    distance -=5
    pyautogui.dragRel(0,-distance,duration = 0.2)#向上移动