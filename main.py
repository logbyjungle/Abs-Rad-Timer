import pyautogui
import time
while True:
    if pyautogui.locateOnScreen('start.png',confidence = 0.7):
        start = time.time()
        print("timer started")
        time.sleep(5)
    if pyautogui.locateOnScreen('end.png', confidence = 0.7):
        end = int(abs(start - time.time())-10)
        with open("times.txt", "a") as file:
            file.write(str(int(end/60)) + ":" + str(end - (int(end/60))*60) + "\n")
        print("gg, the time is: " + str(int(end / 60)) + ":" + str(end - (int(end / 60)) * 60))
        time.sleep(5)
