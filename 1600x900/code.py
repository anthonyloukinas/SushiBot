import ImageGrab
import os
import time
import win32api, win32con

"""
All coordinates assume a screen resolution of 1920x1080, and Chrome 
maximized with the Bookmarks Toolbar disabled.
x_pad = 476
y_pad = 254
Play area =  x_pad+1, y_pad+1, x_pad+640, y_pad+480
"""

## Globals
## -----------

x_pad = 317
y_pad = 255

## -----------
## End Globals

def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+640, y_pad+480)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "Click." # For debugging purposes

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print 'left down'

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'left release'

def mousePos(cord=(0,0)):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
##    x = x - x_pad
##    y = y - y_pad
    print x, y

def startGame():
    #location of first menu
    mousePos((313, 202))
    leftClick()
    time.sleep(.1)

    #location of second menu
    mousePos((310, 393))
    leftClick()
    time.sleep(.1)

    #location of third menu
    mousePos((582, 456))
    leftClick()
    time.sleep(.1)

    #location of fourth menu
    mousePos((320, 379))
    leftClick()
    time.sleep(.1)

class Cord:
    f_shrimp = (32, 335)
    f_rice = (89, 335)
    f_nori = (32, 388)
    f_roe = (89, 392)
    f_salmon = (32,442)
    f_unagi = (89, 442)

#--------------------------------

    phone = (583, 360)

    menu_toppings = (535, 272)

    t_shrimp = (499, 220)
    t_nori = (499, 280)
    t_roe = (576, 280)
    t_salmon = (499, 330)
    t_unagi = (576, 220)
    t_exit = (594, 336)

    menu_rice = (535, 294)
    buy_rice = (541, 280)

    delivery_norm = (492, 296)

def clear_tables():
    print ("Clearing Tables.")
    mousePos((90, 207))
    leftClick()

    mousePos((191, 207))
    leftClick()

    mousePos((292, 207))
    leftClick()

    mousePos((395, 207))
    leftClick()

    mousePos((499, 207))
    leftClick()

    mousePos((596, 207))
    leftClick()
    time.sleep(1)

    print ("Tables Cleared.")



