import pyautogui
import time
start = time.time()
while True:
    if pyautogui.locateOnScreen('start.png',confidence = 0.7):
        if time.time()-start > 5:
            print("timer started")
        start = time.time()
    if pyautogui.locateOnScreen('end.png', confidence = 0.7):
        end = int(abs(start - time.time())-10)
        with open("times.txt", "a") as file:
            file.write(str(int(end/60)) + ":" + str(end - (int(end/60))*60) + "\n")
        print("gg, the time is: " + str(int(end / 60)) + ":" + str(end - (int(end / 60)) * 60))
        time.sleep(5)
