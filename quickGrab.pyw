"""
All coordinates assume a screen resolution of 1920x1080, and Chrome 
maximized with the Bookmarks Toolbar disabled.
x_pad = 476
y_pad = 254
Play area =  x_pad+1, y_pad+1, x_pad+640, y_pad+480
"""

import ImageGrab
import os
import time

# Globals
# ------------

x_pad = 476
y_pad = 253

def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+640, y_pad+480)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()
