from datetime import datetime,timezone
import pyautogui
from time import sleep
import random
import time

print(pyautogui.size(), 'Current time:',datetime.today().strftime("%I:%M:%S %p"))
print(pyautogui.position(), 'Current time:',datetime.today().strftime("%I:%M:%S %p"))
global Battles
Battles = 0
Time_started = datetime.today().strftime("\nDay: %j, %I:%M:%S %p")
Time_started_UNIX_timecode = time.time()

def towerplace():
    no_further = pyautogui.locateOnScreen("titleName.png", confidence=0.8).top   #680
    #Box(left=1533, top=383, width=65, height=53)
    pixels_moved_down = 0
    pixels_moved_right = 0
    start_location = pyautogui.position().x
    #print(start_location)
    while pixels_moved_down < 370:
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
            pyautogui.move(70 + random_placement_positive_x - random_placement_negative_x, random_placement_positive_y - random_placement_negative_y)
            pyautogui.leftClick()
            #pyautogui.keyDown(',')
            #sleep(0.07 + random.uniform(0, 0.05))
            #pyautogui.keyUp(',')
            pyautogui.keyDown('esc')
            sleep(0.02 + random.uniform(0, 0.06))
            pyautogui.keyUp('esc')
            pyautogui.move(0, random.randrange(-70, 70))
            pyautogui.keyDown('q')
            sleep(0.02 + random.uniform(0, 0.06))
            pyautogui.keyUp('q')
            pyautogui.leftClick()
            pyautogui.keyDown('esc')
            sleep(0.02 + random.uniform(0, 0.06))
            pyautogui.keyUp('esc')
            pyautogui.moveTo(pyautogui.position().x, return_value)
            pixels_moved_right += 70 + random_placement_positive_x - random_placement_negative_x
            #print(pixels_moved_right)
            if pyautogui.position().y > 680 + no_further:
                pixels_moved_down = 380
                pixels_moved_right = 910
            if pyautogui.locateOnScreen("defooted.png", confidence=0.8) != None:
                while True:
                    if pyautogui.locateOnScreen("defooted.png", confidence=0.8) != None:
                        pyautogui.moveTo(pyautogui.locateOnScreen("chest.png", confidence=0.9))
                        pyautogui.moveTo(pyautogui.locateOnScreen("battle_chest.png", confidence=0.9))
                        pyautogui.move(0, 440, 6 + random.uniform(0, 3))
                        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                        pyautogui.leftClick()
                        return
            if pyautogui.locateOnScreen("victree.png", confidence=0.8) != None:
                while True:
                    if pyautogui.locateOnScreen("victree.png", confidence=0.8) != None:
                        pyautogui.moveTo(pyautogui.locateOnScreen("chest.png", confidence=0.9))
                        pyautogui.moveTo(pyautogui.locateOnScreen("battle_chest.png", confidence=0.9))
                        pyautogui.move(0, 440, 6 + random.uniform(0, 3))
                        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                        pyautogui.leftClick()
                        return
        pyautogui.move(0, 90 + random_placement_positive - random_placement_negative)
        pixels_moved_down += 90 + random_placement_positive - random_placement_negative


def btdb():
    print('activated automater', 'Current time:',datetime.today().strftime("%I:%M:%S %p"))

    sleep(2 + random.uniform(0, 2))
    if pyautogui.locateOnScreen("Chests-full.png", confidence=0.8) != None:
        pyautogui.moveTo(pyautogui.locateOnScreen("Chests-full.png", confidence=0.8))
        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
        pyautogui.leftClick()
        pyautogui.move(60, 0)
        print('got rid of pesky chest screen', 'Current time:',datetime.today().strftime("%I:%M:%S %p"))
        return
    elif pyautogui.locateOnScreen("fancybb.png", confidence=0.8) != None:
        print('Clicked battle button. \n', 'Current time:',datetime.today().strftime("%I:%M:%S %p"))
        pyautogui.moveTo(pyautogui.locateOnScreen("fancybb.png", confidence=0.8))
        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
        pyautogui.leftClick()
        global Battles
        global Time_started_UNIX_timecode
        Time_since = time.time() - Time_started_UNIX_timecode
        print('\nThere have been {0} battles since {1}\n{2} Seconds have passed since starting the script'.format(Battles, Time_started, round(Time_since, 2)))
        Battles += 1
        if (pyautogui.locateOnScreen("failed_connect.png", confidence=0.8) != None) or ( pyautogui.locateOnScreen("failed_server_c.png", confidence=0.8) != None):
            sleep(random.uniform(0, 2))
            pyautogui.moveTo(pyautogui.locateOnScreen("failed_connect.png", confidence=0.8))
            pyautogui.moveTo(pyautogui.locateOnScreen("failed_server_c.png", confidence=0.8))
            pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
            pyautogui.leftClick()
            return
        if pyautogui.locateOnScreen("Chests-full.png", confidence=0.8) != None:
            pyautogui.moveTo(pyautogui.locateOnScreen("Chests-full.png", confidence=0.8))
            pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
            pyautogui.leftClick()
            print('got rid of pesky chest screen', 'Current time:',datetime.today().strftime("%I:%M:%S %p"))
            return
        while True:
            if (pyautogui.locateOnScreen("failed_connect.png", confidence=0.8) != None) or ( pyautogui.locateOnScreen("failed_server_c.png", confidence=0.8) != None):
                pyautogui.moveTo(pyautogui.locateOnScreen("failed_connect.png", confidence=0.8))
                pyautogui.moveTo(pyautogui.locateOnScreen("failed_server_c.png", confidence=0.8))
                pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                pyautogui.leftClick()
                return
            sleep(2 + random.uniform(0, 2))
            if pyautogui.locateOnScreen("Ready-hero-button.png", confidence=0.8) != None:
                print('Clicked hero select button', 'Current time:',datetime.today().strftime("%I:%M:%S %p"))
                pyautogui.moveTo(pyautogui.locateOnScreen("Ready-hero-button.png", confidence=0.8))
                pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                pyautogui.leftClick()
                if pyautogui.locateOnScreen("Chests-full.png", confidence=0.8) != None:
                    pyautogui.moveTo(pyautogui.locateOnScreen("Chests-full.png", confidence=0.8))
                    pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                    pyautogui.leftClick()
                    print('got rid of pesky chest screen', 'Current time:',datetime.today().strftime("%I:%M:%S %p"))
                    return
                while True:
                    if (pyautogui.locateOnScreen("failed_connect.png", confidence=0.8) != None) or ( pyautogui.locateOnScreen("failed_server_c.png", confidence=0.8) != None):
                        pyautogui.moveTo(pyautogui.locateOnScreen("failed_connect.png", confidence=0.8))
                        pyautogui.moveTo(pyautogui.locateOnScreen("failed_server_c.png", confidence=0.8))
                        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                        pyautogui.leftClick()
                        return
                    sleep(2 + random.uniform(0, 2))
                    pyautogui.moveTo()
                    pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                    pyautogui.leftClick()
                    if pyautogui.locateOnScreen("Ready-tower-button.png", confidence=0.8) != None:
                        print('Clicked tower select button', 'Current time:',datetime.today().strftime("%I:%M:%S %p"))
                        pyautogui.moveTo(pyautogui.locateOnScreen("Ready-tower-button.png", confidence=0.8))
                        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                        pyautogui.leftClick()
                        if pyautogui.locateOnScreen("defooted.png", confidence=0.8) != None:
                            if (pyautogui.locateOnScreen("chest.png", confidence=0.95) != None) or (pyautogui.locateOnScreen("battle_chest.png", confidence=0.8) != None):
                                pyautogui.moveTo(pyautogui.locateOnScreen("chest.png", confidence=0.9))
                                pyautogui.moveTo(pyautogui.locateOnScreen("battle_chest.png", confidence=0.9))
                                pyautogui.move(0, 440, 6 + random.uniform(0, 3))
                                pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                pyautogui.leftClick()
                                return
                        if pyautogui.locateOnScreen("victree.png", confidence=0.8) != None:
                            if (pyautogui.locateOnScreen("chest.png", confidence=0.95) != None) or (pyautogui.locateOnScreen("battle_chest.png", confidence=0.8) != None):
                                pyautogui.moveTo(pyautogui.locateOnScreen("chest.png", confidence=0.9))
                                pyautogui.moveTo(pyautogui.locateOnScreen("battle_chest.png", confidence=0.9))
                                pyautogui.move(0, 440, 6 + random.uniform(0, 3))
                                pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                pyautogui.leftClick()
                                return
                        if (pyautogui.locateOnScreen("failed_connect.png", confidence=0.8) != None) or ( pyautogui.locateOnScreen("failed_server_c.png", confidence=0.8) != None):
                            pyautogui.moveTo(pyautogui.locateOnScreen("failed_connect.png", confidence=0.8))
                            pyautogui.moveTo(pyautogui.locateOnScreen("failed_server_c.png", confidence=0.8))
                            pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                            pyautogui.leftClick()
                            return
                        if pyautogui.locateOnScreen("Chests-full.png", confidence=0.8) != None:
                            pyautogui.moveTo(pyautogui.locateOnScreen("Chests-full.png", confidence=0.8))
                            pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                            pyautogui.leftClick()
                            print('got rid of pesky chest screen', 'Current time:',datetime.today().strftime("%I:%M:%S %p"))
                            return
                        while True:
                            sleep(2 + random.uniform(0, 2))
                            if pyautogui.locateOnScreen("defooted.png", confidence=0.8) != None:
                                if (pyautogui.locateOnScreen("chest.png", confidence=0.95) != None) or (pyautogui.locateOnScreen("battle_chest.png", confidence=0.8) != None):
                                    pyautogui.moveTo(pyautogui.locateOnScreen("chest.png", confidence=0.9))
                                    pyautogui.moveTo(pyautogui.locateOnScreen("battle_chest.png", confidence=0.9))
                                    pyautogui.move(0, 440, 6 + random.uniform(0, 3))
                                    pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                    pyautogui.leftClick()
                                    return
                            if pyautogui.locateOnScreen("victree.png", confidence=0.8) != None:
                                if (pyautogui.locateOnScreen("chest.png", confidence=0.95) != None) or (pyautogui.locateOnScreen("battle_chest.png", confidence=0.8) != None):
                                    pyautogui.moveTo(pyautogui.locateOnScreen("chest.png", confidence=0.9))
                                    pyautogui.moveTo(pyautogui.locateOnScreen("battle_chest.png", confidence=0.9))
                                    pyautogui.move(0, 440, 6 + random.uniform(0, 3))
                                    pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                    pyautogui.leftClick()
                                    return
                            if (pyautogui.locateOnScreen("failed_connect.png", confidence=0.8) != None) or ( pyautogui.locateOnScreen("failed_server_c.png", confidence=0.8) != None):
                                pyautogui.moveTo(pyautogui.locateOnScreen("failed_connect.png", confidence=0.8))
                                pyautogui.moveTo(pyautogui.locateOnScreen("failed_server_c.png", confidence=0.8))
                                pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                pyautogui.leftClick()
                                return
                            if (pyautogui.locateOnScreen("top-left.png", confidence=0.95) != None) or (pyautogui.locateOnScreen("alt-top-left.png", confidence=0.95) != None):
                                pyautogui.moveTo(pyautogui.locateOnScreen("top-left.png", confidence=0.95))
                                pyautogui.moveTo(pyautogui.locateOnScreen("alt-top-left.png", confidence=0.95))
                                pyautogui.move(20, 145)
                                if pyautogui.locateOnScreen("Chests-full.png", confidence=0.8) != None:
                                    pyautogui.moveTo(pyautogui.locateOnScreen("Chests-full.png", confidence=0.8))
                                    pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                    pyautogui.leftClick()
                                    print('got rid of pesky chest screen', 'Current time:',datetime.today().strftime("%I:%M:%S %p"))
                                    return
                                if (pyautogui.locateOnScreen("failed_connect.png", confidence=0.8) != None) or ( pyautogui.locateOnScreen("failed_server_c.png", confidence=0.8) != None):
                                    pyautogui.moveTo(pyautogui.locateOnScreen("failed_connect.png", confidence=0.8))
                                    pyautogui.moveTo(pyautogui.locateOnScreen("failed_server_c.png", confidence=0.8))
                                    pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                    pyautogui.leftClick()
                                    return
                                towerplace()
                                while True:
                                    if (pyautogui.locateOnScreen("failed_connect.png", confidence=0.8) != None) or ( pyautogui.locateOnScreen("failed_server_c.png", confidence=0.8) != None):
                                        pyautogui.moveTo(pyautogui.locateOnScreen("failed_connect.png", confidence=0.8))
                                        pyautogui.moveTo(pyautogui.locateOnScreen("failed_server_c.png", confidence=0.8))
                                        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                        pyautogui.leftClick()
                                        return
                                    if pyautogui.locateOnScreen("defooted.png", confidence=0.8) != None:
                                        if (pyautogui.locateOnScreen("chest.png", confidence=0.95) != None) or (pyautogui.locateOnScreen("battle_chest.png", confidence=0.8) != None):
                                            pyautogui.moveTo(pyautogui.locateOnScreen("chest.png", confidence=0.9))
                                            pyautogui.moveTo(pyautogui.locateOnScreen("battle_chest.png", confidence=0.9))
                                            pyautogui.move(0, 440, 6 + random.uniform(0, 3))
                                            pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                            pyautogui.leftClick()
                                            return
                                    if pyautogui.locateOnScreen("victree.png", confidence=0.8) != None:
                                        if (pyautogui.locateOnScreen("chest.png", confidence=0.95) != None) or (pyautogui.locateOnScreen("battle_chest.png", confidence=0.8) != None):
                                            pyautogui.moveTo(pyautogui.locateOnScreen("chest.png", confidence=0.9))
                                            pyautogui.moveTo(pyautogui.locateOnScreen("battle_chest.png", confidence=0.8))
                                            pyautogui.move(0, 440, 6 + random.uniform(0, 3))
                                            pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                            pyautogui.leftClick()
                                            return
                                    print('trying surrender', 'Current time:',datetime.today().strftime("%I:%M:%S %p"))
                                    sleep(2 + random.uniform(0, 2))
                                    if pyautogui.locateOnScreen("surrender.png", confidence=0.82) != None:
                                        print('Clicked surrender button', 'Current time:',datetime.today().strftime("%I:%M:%S %p"))
                                        pyautogui.moveTo(pyautogui.locateOnScreen("surrender.png", confidence=0.82))
                                        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                        pyautogui.leftClick()
                                        while True:
                                            sleep(1 + random.uniform(0, 2))
                                            if pyautogui.locateOnScreen("defooted.png", confidence=0.8) != None:
                                                if (pyautogui.locateOnScreen("chest.png", confidence=0.95) != None) or (pyautogui.locateOnScreen("battle_chest.png", confidence=0.8) != None):
                                                    pyautogui.moveTo(pyautogui.locateOnScreen("chest.png", confidence=0.9))
                                                    pyautogui.moveTo(pyautogui.locateOnScreen("battle_chest.png", confidence=0.9))
                                                    pyautogui.move(0, 440, 6 + random.uniform(0, 3))
                                                    pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                                    pyautogui.leftClick()
                                                    return
                                            if pyautogui.locateOnScreen("victree.png", confidence=0.8) != None:
                                                if (pyautogui.locateOnScreen("chest.png", confidence=0.95) != None) or (pyautogui.locateOnScreen("battle_chest.png", confidence=0.8) != None):
                                                    pyautogui.moveTo(pyautogui.locateOnScreen("chest.png", confidence=0.9))
                                                    pyautogui.move(0, 440, 6 + random.uniform(0, 3))
                                                    pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                                    pyautogui.leftClick()
                                                    return
                                            if pyautogui.locateOnScreen("surrender_confirm.png", confidence=0.8) != None:
                                                print('Clicked surrender confirm button', 'Current time:',datetime.today().strftime("%I:%M:%S %p"))
                                                pyautogui.moveTo(pyautogui.locateOnScreen("surrender_confirm.png",confidence=0.8))
                                                pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                                pyautogui.leftClick()
                                                while True:
                                                    sleep(2 + random.uniform(0, 2))
                                                    if (pyautogui.locateOnScreen("chest.png", confidence=0.95) != None) or (pyautogui.locateOnScreen("battle_chest.png", confidence=0.8) != None):
                                                        print('Clicked ok button', 'Current time:',datetime.today().strftime("%I:%M:%S %p"))
                                                        pyautogui.moveTo(pyautogui.locateOnScreen("chest.png",confidence=0.9))
                                                        pyautogui.move(0, 440, 6 + random.uniform(0, 3))
                                                        pyautogui.move(random.randrange(-5, 5), random.randrange(-5, 5))
                                                        pyautogui.leftClick()
                                                        sleep(2 + random.uniform(0, 2))
                                                        return



sleep(2)

try:
    while True:
        #print(pyautogui.locateOnScreen("Chests-full.png", confidence=0.8))
        #print('align')
        #sleep(2)
        #print(pyautogui.position())
        #sleep(5)
        #print(pyautogui.position())
        #pyautogui.moveTo(pyautogui.locateOnScreen("chest.png", confidence=0.9))
        #print(pyautogui.locateOnScreen("fancybb.png", confidence=0.8))
        #print(datetime.now(timezone.utc))
        #print(round((time.time()), 2))
        #a = round((time.time()), 2)
        #print(datetime.today().strftime("%I:%M:%S %p"))
        #print(round((time.time() - a), 2))
        pyautogui.keyDown('s')
        btdb()
        sleep(2 + random.uniform(0, 2))


except KeyboardInterrupt:
    pyautogui.keyUp('s')
    Time_since = time.time() - Time_started_UNIX_timecode
    print('\nThere have been {0} battles since {1}\n{2} Seconds have passed since starting the script'.format(Battles, Time_started, round(Time_since, 2)))
    print('KeyBoard interupt detected')
except pyautogui.FailSafeException:
    Time_since = time.time() - Time_started_UNIX_timecode
    print('\nThere have been {0} battles since {1}\n{2} Seconds have passed since starting the script'.format(Battles, Time_started, round(Time_since, 2)))
    print('Pyautogui failsafe detected, Press \'s\'')
#
