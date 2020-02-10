import pyautogui
import schedule
import time
import random

hours=7
minuts=32
date = f"0{hours}:{minuts}"
hourst=2
minutst=20
date2 = f"0{hourst}:{minutst}"

#Morning clicking, copy this one for every click action you want

def click():

    #Position

    pyautogui.moveTo(500, 100)


    pyautogui.doubleClick()
    hours=random.randint(7,9)
    minuts=random.randint(10,59)
    date = f"0{hourst}:{minutst}"

    print(f"Will click at {date2}")


#Evening click
#Remember to add a zero to single decimal ints (or parse it properly to time format)


def click2():
    pyautogui.moveTo(500, 100)
    pyautogui.doubleClick()
    hourst=random.randint(0,2)
    minutst=random.randint(10,59)
    date2 = f"0{hours}:{minuts}"

    print(f"Will click at {date}")


print(f"Next click at {date} and {date2}")
schedule.every().day.at(date).do(click)
schedule.every().day.at(date).do(click2)



while True:
    schedule.run_pending()
    time.sleep(1)