import pyautogui
import schedule
import time
import datetime
import random
pyautogui.FAILSAFE = False

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.


datetime.datetime.now()

print(datetime.datetime.now())
print("Starting")


#activehours
hours=random.randint(10,13)
minuts=random.randint(10,59)
date = f"{hours}:{minuts}"
hourst=random.randint(0,2)
minutst=random.randint(10,59)
date2 = f"0{hourst}:{minutst}"


        

#Morning clicking, copy this one for every click action you want

def click():
    global date
    global date2

    print(datetime.datetime.now())

    hourst=random.randint(0,2)
    minutst=random.randint(10,59)
    date2 = f"0{hourst}:{minutst}"

    print("Good morning ")
    rdelay=random.randint(1,6000)
    time.sleep(rdelay)
    print(datetime.datetime.now())
    pyautogui.doubleClick(500,100)
    print ("Click")
    print(f"Will click at {date} and {date2}")





def click2():

    global date    
    global date2

    hours=random.randint(10,14)
    minuts=random.randint(10,59)
    date = f"{hours}:{minuts}"

    print(datetime.datetime.now())
    print("Good night")           
    rdelay=random.randint(1,3500)
    time.sleep(rdelay)
    print(datetime.datetime.now())
    pyautogui.doubleClick(500,100)
    print ("Click")
    print(f"Will click at {date} and {date2}")

print(f"Active from {date} to {date2}")
schedule.every().day.at(date).do(click)
schedule.every().day.at(date2).do(click2)





while True:
    schedule.run_pending()
    time.sleep(1)
