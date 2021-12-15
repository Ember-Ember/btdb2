import pyautogui
from time import sleep
import random

print(pyautogui.size())
print(pyautogui.position())


def towerplace():
    pixels_moved_down = 0
    pixels_moved_right = 0
    start_location = pyautogui.position().x
    #print(start_location)
    while pixels_moved_down < 330:
        random_placement_positive = random.randrange(0, 50)
        random_placement_negative = random.randrange(0, 40)
        pyautogui.keyDown('w')
        sleep(0.02 + random.uniform(0, 0.06))
        pyautogui.keyUp('w')
        #print('place attempt left')
        pyautogui.leftClick()
        pyautogui.keyDown('esc')
        sleep(0.02 + random.uniform(0, 0.06))
        pyautogui.keyUp('esc')
        pyautogui.move(0, 70 + random_placement_positive - random_placement_negative)
        pixels_moved_down += 60 + random_placement_positive - random_placement_negative
        pixels_moved_right = 0
        pyautogui.moveTo(start_location, pyautogui.position().y)
        #print(pixels_moved_down)
        while pixels_moved_right < 900:
            random_placement_positive_x = random.randrange(0, 50)
            random_placement_negative_x = random.randrange(0, 40)
            random_placement_positive_y = random.randrange(0, 40)
            random_placement_negative_y = random.randrange(0, 40)
            pyautogui.keyDown('w')
            sleep(0.02 + random.uniform(0, 0.06))
            pyautogui.keyUp('w')
            #print('place attempt right')
            return_value = pyautogui.position().y
            pyautogui.move(60 + random_placement_positive_x - random_placement_negative_x, random_placement_positive_y - random_placement_negative_y)
            pyautogui.leftClick()
            pyautogui.moveTo(pyautogui.position().x, return_value)
            pyautogui.keyDown('esc')
            sleep(0.02 + random.uniform(0, 0.06))
            pyautogui.keyUp('esc')
            pixels_moved_right += 60 + random_placement_positive_x - random_placement_negative_x
            #print(pixels_moved_right)
            if pyautogui.locateOnScreen("defooted.png", confidence=0.8) != None:
                while True:
                    if pyautogui.locateOnScreen("defooted.png", confidence=0.8) != None:
                        pyautogui.moveTo(pyautogui.locateOnScreen("chest.png", confidence=0.9))
                        pyautogui.move(280, 0)
                        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                        pyautogui.leftClick()
                        return
            if pyautogui.locateOnScreen("victree.png", confidence=0.8) != None:
                while True:
                    if pyautogui.locateOnScreen("victree.png", confidence=0.8) != None:
                        pyautogui.moveTo(pyautogui.locateOnScreen("chest.png", confidence=0.9))
                        pyautogui.move(280, 0)
                        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                        pyautogui.leftClick()
                        return


def btdb():
    print('activated automater')
    sleep(2 + random.uniform(0, 2))
    if pyautogui.locateOnScreen("Chests-full.png", confidence=0.8) != None:
        pyautogui.moveTo(pyautogui.locateOnScreen("Chests-full.png", confidence=0.8))
        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
        pyautogui.leftClick()
        print('got rid of pesky chest screen')
        return
    elif pyautogui.locateOnScreen("fancybb.png", confidence=0.8) != None:
        print('Clicked battle button')
        pyautogui.moveTo(pyautogui.locateOnScreen("fancybb.png", confidence=0.8))
        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
        pyautogui.leftClick()
        if pyautogui.locateOnScreen("failed_connect.png", confidence=0.8) != None:
            sleep(random.uniform(0, 2))
            pyautogui.moveTo(pyautogui.locateOnScreen("failed_connect.png", confidence=0.8))
            pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
            pyautogui.leftClick()
            return
        if pyautogui.locateOnScreen("Chests-full.png", confidence=0.8) != None:
            pyautogui.moveTo(pyautogui.locateOnScreen("Chests-full.png", confidence=0.8))
            pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
            pyautogui.leftClick()
            print('got rid of pesky chest screen')
            return
        while True:
            if pyautogui.locateOnScreen("failed_connect.png", confidence=0.8) != None:
                pyautogui.moveTo(pyautogui.locateOnScreen("failed_connect.png", confidence=0.8))
                pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                pyautogui.leftClick()
                return
            sleep(2 + random.uniform(0, 2))
            if pyautogui.locateOnScreen("Ready-hero-button.png", confidence=0.8) != None:
                print('Clicked hero select button')
                pyautogui.moveTo(pyautogui.locateOnScreen("Ready-hero-button.png", confidence=0.8))
                pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                pyautogui.leftClick()
                if pyautogui.locateOnScreen("Chests-full.png", confidence=0.8) != None:
                    pyautogui.moveTo(pyautogui.locateOnScreen("Chests-full.png", confidence=0.8))
                    pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                    pyautogui.leftClick()
                    print('got rid of pesky chest screen')
                    return
                while True:
                    if pyautogui.locateOnScreen("failed_connect.png", confidence=0.8) != None:
                        pyautogui.moveTo(pyautogui.locateOnScreen("failed_connect.png", confidence=0.8))
                        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                        pyautogui.leftClick()
                        return
                    sleep(2 + random.uniform(0, 2))
                    pyautogui.moveTo()
                    pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                    pyautogui.leftClick()
                    if pyautogui.locateOnScreen("Ready-tower-button.png", confidence=0.8) != None:
                        print('Clicked tower select button')
                        pyautogui.moveTo(pyautogui.locateOnScreen("Ready-tower-button.png", confidence=0.8))
                        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                        pyautogui.leftClick()
                        if pyautogui.locateOnScreen("failed_connect.png", confidence=0.8) != None:
                            pyautogui.moveTo(pyautogui.locateOnScreen("failed_connect.png", confidence=0.8))
                            pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                            pyautogui.leftClick()
                            return
                        if pyautogui.locateOnScreen("Chests-full.png", confidence=0.8) != None:
                            pyautogui.moveTo(pyautogui.locateOnScreen("Chests-full.png", confidence=0.8))
                            pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                            pyautogui.leftClick()
                            print('got rid of pesky chest screen')
                            return
                        while True:
                            sleep(2 + random.uniform(0, 2))
                            if pyautogui.locateOnScreen("failed_connect.png", confidence=0.8) != None:
                                pyautogui.moveTo(pyautogui.locateOnScreen("failed_connect.png", confidence=0.8))
                                pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                pyautogui.leftClick()
                                return
                            if (pyautogui.locateOnScreen("top-left.png", confidence=0.9) != None) or (pyautogui.locateOnScreen("alt-top-left.png", confidence=0.9) != None):
                                pyautogui.moveTo(pyautogui.locateOnScreen("top-left.png", confidence=0.9))
                                pyautogui.moveTo(pyautogui.locateOnScreen("alt-top-left.png", confidence=0.9))
                                pyautogui.move(25, 125)
                                if pyautogui.locateOnScreen("Chests-full.png", confidence=0.8) != None:
                                    pyautogui.moveTo(pyautogui.locateOnScreen("Chests-full.png", confidence=0.8))
                                    pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                    pyautogui.leftClick()
                                    print('got rid of pesky chest screen')
                                    return
                                if pyautogui.locateOnScreen("failed_connect.png", confidence=0.8) != None:
                                    pyautogui.moveTo(pyautogui.locateOnScreen("failed_connect.png", confidence=0.8))
                                    pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                    pyautogui.leftClick()
                                    return
                                towerplace()
                                while True:
                                    if pyautogui.locateOnScreen("failed_connect.png", confidence=0.8) != None:
                                        pyautogui.moveTo(pyautogui.locateOnScreen("failed_connect.png", confidence=0.8))
                                        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                        pyautogui.leftClick()
                                        return
                                    if pyautogui.locateOnScreen("defooted.png", confidence=0.8) != None:
                                        if pyautogui.locateOnScreen("chest.png", confidence=0.8) != None:
                                            pyautogui.moveTo(pyautogui.locateOnScreen("chest.png", confidence=0.9))
                                            pyautogui.move(280, 0)
                                            pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                            pyautogui.leftClick()
                                            return
                                    if pyautogui.locateOnScreen("victree.png", confidence=0.8) != None:
                                        if pyautogui.locateOnScreen("chest.png", confidence=0.8) != None:
                                            pyautogui.moveTo(pyautogui.locateOnScreen("chest.png", confidence=0.9))
                                            pyautogui.move(280, 0)
                                            pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                            pyautogui.leftClick()
                                            return
                                    print('trying surrender')
                                    sleep(2 + random.uniform(0, 2))
                                    if pyautogui.locateOnScreen("surrender.png", confidence=0.7) != None:
                                        print('Clicked surrender button')
                                        pyautogui.moveTo(pyautogui.locateOnScreen("surrender.png", confidence=0.8))
                                        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                        pyautogui.leftClick()
                                        while True:
                                            sleep(2 + random.uniform(0, 2))
                                            if pyautogui.locateOnScreen("surrender_confirm.png", confidence=0.8) != None:
                                                print('Clicked surrender confirm button')
                                                pyautogui.moveTo(pyautogui.locateOnScreen("surrender_confirm.png",confidence=0.8))
                                                pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                                pyautogui.leftClick()
                                                while True:
                                                    sleep(2 + random.uniform(0, 2))
                                                    if pyautogui.locateOnScreen("chest.png",confidence=0.9) != None:
                                                        print('Clicked ok button')
                                                        pyautogui.moveTo(pyautogui.locateOnScreen("chest.png",confidence=0.9))
                                                        pyautogui.move(280, 0)
                                                        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                                        pyautogui.leftClick()
                                                        sleep(2 + random.uniform(0, 2))
                                                        return




while True:
    #print('align')
    #sleep(2)
    #print(pyautogui.position())
    #sleep(5)
    #print(pyautogui.position())
    btdb()
    #print(pyautogui.locateOnScreen("fancybb.png", confidence=0.8))
    sleep(2 + random.uniform(0, 2))