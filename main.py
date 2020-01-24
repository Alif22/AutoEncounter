import time
import pyautogui
import keyboard

cyan = (60,232,233)
def keyPressForTime(holdTime,key):
    startTime = time.time()
    ifMapOnScreen = True
    pyautogui.keyDown(key)
    while time.time() - startTime < holdTime and ifMapOnScreen:
        ifMapOnScreen = pyautogui.pixelMatchesColor(1257,23,cyan)
    pyautogui.keyUp(key)
    return ifMapOnScreen


if __name__ == "__main__":
    #TODO get hold time from a txt file
    holdTime = 1
    programRun = True
    while programRun:
        Input = input("Enter r to run program:")
        AMRun = False
        if Input.lower() == 'r':
            AMRun = True
            print("running the program in 5 seconds. Click your game")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("4")
            time.sleep(1)
        else:
            print("Thats not R u retard!!")
            print("Im done. Rage quitting")
            time.sleep(2)
        
        while AMRun and programRun:
            #press b to stop move
            try:
                if keyboard.is_pressed('b'):
                    AMRun = False
            except:
<<<<<<< HEAD
                print("b not pressed")
=======
                print("do nothing")
>>>>>>> testBranch
                #do nothing just catchin error
            mapStillOnScreen = True
            if mapStillOnScreen:
                mapStillOnScreen = keyPressForTime(holdTime,'d')
                mapStillOnScreen = keyPressForTime(holdTime,'s')
                mapStillOnScreen = keyPressForTime(holdTime,'a')
                mapStillOnScreen = keyPressForTime(holdTime,'w')
            else:
                AMRun = False