from grabscreen import grab_screen
import time
from PIL import Image

if __name__ == '__main__':
    last_time = time.time()
    while True:
        screen = grab_screen((0, 0, 2560, 1440))
        img = Image.fromarray(screen)
        # img.show()
        print(type(img))
