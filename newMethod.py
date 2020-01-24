import time
import pyautogui
import keyboard

cyan = (60,232,233)
keySequence = ['d', 's', 'a','w']

def keyPressForTime(holdTime,key):
    startTime = time.time()
    isMapOnScreen = True
    pyautogui.keyDown(key)
    while time.time() - startTime < holdTime and isMapOnScreen:
        isMapOnScreen = checkMapOnScreen()
    pyautogui.keyUp(key)
    return isMapOnScreen

def checkMapOnScreen():
    isMapOnScreen = pyautogui.pixelMatchesColor(1257,23,(60,232,233))
    return isMapOnScreen
    

if __name__ == "__main__":
    #TODO get hold time from a txt file
    holdTime = 0.5
    mapOnScreen = True
    print("running the program in 5 seconds. Click your game")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("3")
    time.sleep(1)
    #print("4")
    #time.sleep(1)
    temp = 0
    while True:
        mapOnScreen = checkMapOnScreen() 
        if mapOnScreen:
            print("Map found. Looping")
            i = 0
            while i < 4:
                print("The current is "+ keySequence[i])
                mapOnScreen = keyPressForTime(holdTime,keySequence[i])
                i += 1
                if not mapOnScreen:
                    temp = i-1
                    print("temp value " + str(temp))
                    break
                 
