import os
import time
import win32api, win32con
from PIL import ImageGrab


def screenGrab():
    box = ()
    # (x,y,x,y)el primer x,y es la esquina superior izquierda, el segundo es la esquina inferior derecha
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
            '.png', 'PNG')


def main():
    screenGrab()


if __name__ == '__main__':
    main()

