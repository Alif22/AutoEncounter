import time
import pyautogui

cyan = (60,232,233)
keySequence = ['d', 's', 'a','w']
x,y = pyautogui.size()
x = round(x * 0.9202)
y = round(y * 0.0299)

def keyPressForTime(holdTime,key):
    startTime = time.time()
    isMapOnScreen = True
    
    pyautogui.keyDown(key)
    while time.time() - startTime < holdTime and isMapOnScreen:
        isMapOnScreen = checkMapOnScreen()
    pyautogui.keyUp(key)

    return isMapOnScreen

def checkMapOnScreen():
    isMapOnScreen = pyautogui.pixelMatchesColor(x,y,cyan)
    return isMapOnScreen

def keyGenerator():
    yield keySequence[0]
    yield keySequence[1]
    yield keySequence[2]
    yield keySequence[3]

if __name__ == "__main__":
    #TODO get hold time from a txt file
    holdTime = 0.4
    mapOnScreen = True
    print("running the program in 3 seconds. Click your game")

    time.sleep(1)
    for i in range(3):
        print(str(i+1))
        time.sleep(1)
    print("Started")

    keyIterator = keyGenerator()
    while True:
        mapOnScreen = checkMapOnScreen()
        if mapOnScreen:
            print("Map found. Looping")
            for i in range(4):
                try:
                    key = next(keyIterator)
                except StopIteration:
                    keyIterator = keyGenerator()
                    key = next(keyIterator)
                
                mapOnScreen = keyPressForTime(holdTime,key)
                print("clicking key "+ str(key))

                if not mapOnScreen:
                    print("In fight, AutoMovement paused")
                    break
        
