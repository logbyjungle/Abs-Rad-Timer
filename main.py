import pyautogui
import time
start = time.time()
def sectominandsec(sec):
    minutes = int(sec/60)
    seconds = sec-minutes*60
    seconds = seconds if seconds >= 10 else "0" + str(seconds)
    return str(minutes) + ":" + str(seconds)
with open('times.txt','r') as file:
    times = [int(taim.split(':')[0]) * 60 + int(taim.split(':')[1]) for taim in [line.strip() for line in file.readlines()]]
print("Initializing Abs Rad Timer...")
if len(times)!=0:
    print("your average time is: " + sectominandsec(int(sum(times)/len(times))))
    print("your PB is: " + str(sectominandsec(min(times))))
print("Abs Rad Timer has been initialized")
while True:
    if pyautogui.locateOnScreen('start.png',confidence = 0.7):
        start = time.time()
        enable = True
    if pyautogui.locateOnScreen('end.png', confidence = 0.7) and enable == True:
        end = int(abs(start - time.time())-10)
        thetimeittook = sectominandsec(end)
        with open("times.txt", "a") as file:
            file.write(thetimeittook + "\n")
        print("the time is: " + thetimeittook)
        enable = False
        if len(times) != 0:
            if end < min(times):
                print("NEW PB! " + "(-" + str(min(times)-end) + "s)")
        times.append(end)
        print("your new average time is: " + sectominandsec(int(sum(times)/len(times))))
