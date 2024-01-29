import pyautogui
import time
start = time.time()
while True:
    if pyautogui.locateOnScreen('start.png',confidence = 0.7):
        if time.time()-start > 5:
            print("timer started")
        start = time.time()
        enable = True
    if pyautogui.locateOnScreen('end.png', confidence = 0.7) and enable == True:
        end = int(abs(start - time.time())-10)
        if end - (int(end/60))*60 >= 10:
            seconds = str(end - (int(end/60))*60)
        else:
            seconds = "0" + str(end - (int(end/60))*60)
        with open("times.txt", "a") as file:
            file.write(str(int(end/60)) + ":" + seconds + "\n")
        print("gg, the time is: " + str(int(end / 60)) + ":" + str(end - (int(end / 60)) * 60))
        enable = False
