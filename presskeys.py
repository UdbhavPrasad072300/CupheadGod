from directkeys import PressKey, ReleaseKey

import time


def presskey(key):
    PressKey(key)
    time.sleep(1)
    ReleaseKey(key)
    time.sleep(1)
