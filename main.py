import time
import pyautogui
import keyboard

cyan = (60,232,233)
def keyPressForTime(holdTime,key):
    startTime = time.time()
    ifMapOnScreen = True
    while time.time() - start < holdTime and ifMapOnScreen:
        ifMapOnScreen = pyautogui.pixelMatchesColor(1257,23,cyan)
        pyautogui.press(key)
    return ifMapOnScreen


if __name__ == "__main__":
    #TODO get hold time from a txt file
    holdTIme = 1
    programRun = True
    while programRun:
        print("Press R to run the program")
        try:
            if keyboard.is_pressed('r'):
                programRun = True
        except:
            print("Press the fucking R you blindman. Im done. Rage quitting")
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
        AMRun = True
        while AMRun and programRun:
            #press b to stop move
            try:
                if keyboard.is_pressed('b'):
                    AMRun = False
            except:
                #do nothing just catchin error
            mapStillOnScreen = True
            if mapStillOnScreen:
                mapStillOnScreen = keyPressForTime(holdTIme,'d')
                mapStillOnScreen = keyPressForTime(holdTime,'s')
                mapStillOnScreen = keyPressForTime(holdTime,'a')
                mapStillOnScreen = keyPressForTime(holdTime,'w')
            else
                AMRun = False