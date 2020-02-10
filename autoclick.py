import pyautogui
import schedule
import time
import random

x=15
y=32
date = f"{x}:{y}"
xe=2
ye=20
date2 = f"0{xe}:{ye}"


def click():
    pyautogui.click()
    x=random.randint(8,11)
    y=random.randint(0,59)
    date = f"{x}:{y}"

    print(f"Will click at {date}")

def click2():
    pyautogui.click()
    x=random.randint(0,3)
    y=random.randint(0,59)
    date2 = f"0{xe}:{ye}"

    print(f"Will click at {date}")


print(f"Next click at {date} and {date2}")
schedule.every().day.at(date).do(click)
schedule.every().day.at(date).do(click2)



while True:
    schedule.run_pending()
    time.sleep(1)