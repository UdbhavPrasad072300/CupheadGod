from grabscreen import grab_screen
from preprocess import preprocess

from directkeys import PressKey, ReleaseKey, W, A, S, D, UP, DOWN, LEFT, RIGHT

import time
from PIL import Image

print(getkeys.key_check())

while True:
    #time.sleep(1000)
    PressKey(W)
    time.sleep(1)
    ReleaseKey(W)
    time.sleep(1)
    #exit()

# ReleaseKey(0x11)
# time.sleep(1)

if __name__ == '__main__':
    last_time = time.time()
    while True:
        screen = preprocess(grab_screen((0, 0, 2560, 1440)))

        img = Image.fromarray(screen)
        # img.show()

        exit()
