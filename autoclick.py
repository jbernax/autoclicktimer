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
hours=random.randint(10,11)
minuts=random.randint(10,59)
date = f"{hours}:{minuts}"

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
    global date2

    rwork=random.randint(0,3)
    if rwork == 0:
        freemorning = True
        print(datetime.datetime.now())

        print ("Will take a break next morning")

    if not freemorning:

        print(datetime.datetime.now())


        print("Morning click")
        rdelay=random.randint(1,59)
        time.sleep(rdelay)
        pyautogui.doubleClick(500,100)

        
        print(f"Active from {date} to {date2}")
        rsleep=random.randint(300,1400)
        rback=random.randint(360,2500)
        print(datetime.datetime.now())

        print(f"Will take a break of {rback} seconds after {rdelay+rsleep} seconds")
        time.sleep(rsleep)
        pyautogui.doubleClick(500,100)
        time.sleep(rback)
        pyautogui.doubleClick(500,100)
        print(datetime.datetime.now())

        print("End of the break")



#Launch
    
def click3():

    global freemorning

    if not freemorning:
        launchdelay=random.randint(1,60)
        time.sleep(launchdelay)
        pyautogui.doubleClick(500,100)
        print(datetime.datetime.now())

        
        print ("Launch time click")


def click4():

    global freeevening
    global date3
    global date4

    global date2
    global date

    hours=random.randint(10,11)
    minuts=random.randint(10,59)
    date = f"{hours}:{minuts}"


    hourst=random.randint(0,2)
    minutst=random.randint(10,59)
    date2 = f"0{hourst}:{minutst}"


    rsiesta =random.randint(0,5)
    if rsiesta == 0:
        freeevening = True
        print(datetime.datetime.now())

        print ("Will take a break next evening")
    else:

        print(datetime.datetime.now())

        print ("Click after launch")    
        launchdelay=random.randint(1,60)
        time.sleep(launchdelay)
        pyautogui.doubleClick(500,100)
        

        
#randomstops

        breaksevening=random.randint(0,3)
        if breaksevening != 0:
            rsleep=random.randint(300,2500)
            rback=random.randint(360,5000)
            print(datetime.datetime.now())

            print(f"Will take a break of {rback} seconds after {rsleep} seconds")
            time.sleep(rsleep)
            pyautogui.doubleClick(500,100)
            time.sleep(rback)
            pyautogui.doubleClick(500,100)
            print(datetime.datetime.now())

            print("End of the break")

        if breaksevening !=1:
            rsleep2=random.randint(300,3000)
            rback2=random.randint(360,9900)
            print(datetime.datetime.now())

            print(f"Will take a break of {rback2} seconds after {rsleep2} seconds")
            time.sleep(rsleep2)
            pyautogui.doubleClick(500,100)
            time.sleep(rback2)
            pyautogui.doubleClick(500,100)
            print(datetime.datetime.now())

            print("End of the break")
        if breaksevening !=2:
            rsleep3=random.randint(400,1500)
            rback3=random.randint(360,8500)
            print(datetime.datetime.now())

            print(f"Will take a break of {rback3} seconds after {rsleep3} seconds")
            time.sleep(rsleep3)
            pyautogui.doubleClick(500,100)
            time.sleep(rback3)
            pyautogui.doubleClick(500,100)
            print(datetime.datetime.now())

            print("End of the break")



    
    
    

#
#




#Evening click
#Remember to add a zero to single decimal ints (or parse it properly to time format)


def click2():

    global freeevening    
    global date2
    global date3
    global date4

    launch = random.randint(0,2)
        
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


    if freeevening:
        print(datetime.datetime.now())

        print ("Sleeping early without click")
    else: 
        print(datetime.datetime.now())
        print("Click and Sleep")           
        rdelay=random.randint(1,2200)
        time.sleep(rdelay)
        pyautogui.doubleClick(500,100)
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
