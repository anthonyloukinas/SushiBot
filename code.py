import ImageGrab
import os
import time
import win32api, win32con
import ImageOps
from numpy import *

"""
All coordinates assume a screen resolution of 1920x1080, and Chrome
maximized with the Bookmarks Toolbar disabled.
x_pad = 476
y_pad = 254
Play area =  x_pad+1, y_pad+1, x_pad+640, y_pad+480
"""

## Globals
## -----------

x_pad = 476
y_pad = 253

## -----------
## End Globals
def main():
    startGame()
    while True:
        check_bubs()

def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+640, y_pad+480)
    im = ImageGrab.grab(box)

    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def grab():
    box = (x_pad + 1,y_pad+1,x_pad+640,y_pad+480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    return a

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

def get_seat_one():
    box = (26,61,26+63,61+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a
def get_seat_two():
    box = (127,61,127+63,61+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_three():
    box = (228,61,228+63,61+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_four():
    box = (329,61,329+63,61+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_five():
    box = (430,61,430+63,61+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_six():
    box = (531,61,531+63,61+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()

sushiTypes = {1059:'onigiri',
              1314:'caliroll',
              1263:'gunkan',}

class Blank:
    seat_1 = 8119
    seat_2 = 5986
    seat_3 = 11598
    seat_4 = 10532
    seat_5 = 6782
    seat_6 = 9041

class Cord:
    f_shrimp = (32, 335)
    f_rice = (89, 335)
    f_nori = (32, 388)
    f_roe = (89, 392)
    f_salmon = (32,442)
    f_unagi = (89, 442)

#--------------------------------
    f_mat = (172, 381)
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

'''
Recipes:

    onigiri
        2 rice, 1 nori

    caliroll:
        1 rice, 1 nori, 1 roe

    gunkan:
        1 rice, 1 nori, 2 roe
'''
foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

def makeFood(food):
    if food == 'caliroll':
        print 'Making a CaliRoll'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        foldMat()
        time.sleep(1.5)

    elif food == 'onigiri':
        print 'Making a OniGiri'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        foldMat()
        time.sleep(1.5)

    elif food == 'gunkan':
        print 'Making a Gunkan Maki'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

def foldMat():
    mousePos(Cord.f_mat)
    leftClick()
    time.sleep(.1)


def buyFood(food):
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.1)
        leftClick()
        s = screenGrab()

        if s.getpixel(Cord.buy_rice) != (109, 123, 127):
            print 'Rice is available'
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] +=10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'Rice is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.1)
        leftClick()
        s = screenGrab()

        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (33, 30, 11):
            print 'Nori is available'
            mousePos(Cord.f_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] +=10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'Nori is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.1)
        leftClick()
        s = screenGrab()

        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (33, 30, 11):
            print 'Roe is available'
            mousePos(Cord.f_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] +=10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'Roe is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)


def checkFood():
    for i, j in foodOnHand.items():
        if i =='nori' or i == 'rice' or i == 'roe':
            if j<=4:
                print '%s is low and needs to be replenished' % i
                buyFood(i)
def check_bubs():

    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if sushiTypes.has_key(s1):
            print 'table 1 is occupied and needs %s' % sushiTypes[s1]
            makeFood(sushiTypes[s1])
        else:
            print 'sushi not found!\n sushiType = %i' % s1

    else:
        print 'Table 1 unoccupied'

    clear_tables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if sushiTypes.has_key(s2):
            print 'table 2 is occupied and needs %s' % sushiTypes[s2]
            makeFood(sushiTypes[s2])
        else:
            print 'sushi not found!\n sushiType = %i' % s2

    else:
        print 'Table 2 unoccupied'

    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if sushiTypes.has_key(s3):
            print 'table 3 is occupied and needs %s' % sushiTypes[s3]
            makeFood(sushiTypes[s3])
        else:
            print 'sushi not found!\n sushiType = %i' % s3

    else:
        print 'Table 3 unoccupied'

    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if sushiTypes.has_key(s4):
            print 'table 4 is occupied and needs %s' % sushiTypes[s4]
            makeFood(sushiTypes[s4])
        else:
            print 'sushi not found!\n sushiType = %i' % s4

    else:
        print 'Table 4 unoccupied'

    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if sushiTypes.has_key(s5):
            print 'table 5 is occupied and needs %s' % sushiTypes[s5]
            makeFood(sushiTypes[s5])
        else:
            print 'sushi not found!\n sushiType = %i' % s5

    else:
        print 'Table 5 unoccupied'

    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if sushiTypes.has_key(s6):
            print 'table 1 is occupied and needs %s' % sushiTypes[s6]
            makeFood(sushiTypes[s6])
        else:
            print 'sushi not found!\n sushiType = %i' % s6

    else:
        print 'Table 6 unoccupied'

    clear_tables()

'''
    mousePos(Cord.menu_toppings)

    mousePos(Cord.t_shrimp)
    mousePos(Cord.t_nori)
    mousePos(Cord.t_roe)
    mousePos(Cord.t_salmon)
    mousePos(Cord.t_unagi)
    mousePos(Cord.t_exit)

    mousePos(Cord.menu_rice)
    mousePos(Cord.buy_rice)

    mousePos(Cord.delivery_norm)
'''


