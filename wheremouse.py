#此文件展示鼠标最近的位置
import pyautogui
print("press Ctrl-c to quit")
try:
    while True:
        #得到并打印出鼠标的坐标
        x,y = pyautogui.position()
        positionStr = 'X:'+str(x).rjust(4)+' Y:' + str(y).rjust(4)

except KeyboardInterrupt:
    print("\nDone!")
print(positionStr,end="")
print('\b'*len(positionStr),end='',flush=True)
