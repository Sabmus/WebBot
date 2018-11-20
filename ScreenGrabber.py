import os
import time
from PIL import ImageGrab
import datetime

now = datetime.datetime.now()

def screenGrab():
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\img\\' + str(int(time.time())) + '.png', 'PNG')


def main():
    time.sleep(5)
    screenGrab()


if __name__ == '__main__':
    main()
