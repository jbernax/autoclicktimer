import pyautogui
import schedule
import time
import random
pyautogui.FAILSAFE = False

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

#activehours
hours=random.randint(7,9)
minuts=random.randint(10,59)
date = f"0{hours}:{minuts}"

hourst=random.randint(0,2)
minutst=random.randint(10,59)
date2 = f"0{hourst}:{minutst}"

#launchtime

food=random.randint(13,14)
foodminuts=random.randint(10,59)
endfood=random.randint(15,16)
endfoodminuts=random.randint(10,59)
launch = random.randint(0, 2)
if launch == 0:
    food=14
    foodminuts=random.randint(30,59)
    endfood=15
    endfoodminuts=random.randint(21,59)
date3 = f"{food}:{foodminuts}"
date4 = f"{endfood}:{endfoodminuts}"


freemorning = None
freeevening = None 

#random stops
#
#   

        

#Morning clicking, copy this one for every click action you want

def click():
    global freemorning
    global date

    rwork=random.randint(0,3)
    if rwork == 0:
        freemorning = True
        print ("Will take a break next morning")

    if not freemorning:
        rdelay=random.randint(10,6500)
        time.sleep(rdelay)
        pyautogui.doubleClick(500, 100)

        
        hours=random.randint(7,9)
        minuts=random.randint(10,59)
        date = f"0{hours}:{minuts}"
        print(f"Active from {date} to {date2}")


#Launch
    
def click3():

    if not freemorning:
        launchdelay=random.randint(1,60)
        time.sleep(launchdelay)
        pyautogui.doubleClick(500, 100)
        
        print ("Launch time")


def click4():

    global freeevening
    global date3
    global date4

    rsiesta =random.randint(0,5)
    if rsiesta == 0:
        freeevening = True
        print ("Will take a break next evening")
    else:
    
        launchdelay=random.randint(1,60)
        time.sleep(launchdelay)
        pyautogui.doubleClick(500, 100)
        
        launch = random.randint(0, 2)
        
        if launch == 0:
            food=14
            foodminuts=random.randint(30,59)
            endfood=15
            endfoodminuts=random.randint(21,59)
        else:
            food=random.randint(13,14)
            foodminuts=random.randint(10,59)
            endfood=random.randint(15,16)
            endfoodminuts=random.randint(10,59)
            date3 = f"{food}:{foodminuts}"
            date4 = f"{endfood}:{endfoodminuts}"

    print(f"Active from {date} to {date2}")
    
    

#randomstops
#
#




#Evening click
#Remember to add a zero to single decimal ints (or parse it properly to time format)


def click2():
    
    global date2
    if not freeevening:            
        rdelay=random.randint(1,2200)
        time.sleep(rdelay)
        pyautogui.doubleClick(500, 100)
        hourst=random.randint(0,2)
        minutst=random.randint(10,59)
        date2 = f"0{hourst}:{minutst}"
        print(f"Next click at {date} and {date2}")


print(f"Active from {date} to {date2}")
print(f"Launch from {date3} to {date4}")
schedule.every().day.at(date).do(click)
schedule.every().day.at(date2).do(click2)
schedule.every().day.at(date3).do(click3)
schedule.every().day.at(date4).do(click4)






while True:
    schedule.run_pending()
    time.sleep(1)
