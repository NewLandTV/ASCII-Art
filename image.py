# Creation Date: 2022.03.05. Sat, 00:20:23 (AM. 12:20:23)
# Last Modified Date: 2022.03.05. Sat, 00:30:36 (AM. 12:30:36)
# Reference: https://github.com/kairess/ascii-art
import cv2

CHARS = ' .,-~:;=!*#$@' # 13
nw = 100

img = cv2.imread('imgs/286.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = img.shape
nh = int(h / w * nw)

img = cv2.resize(img, (nw * 2, nh))

for row in img:
    for pixel in row: # pixel 0-255 -> CHARS 0-12
        index = int(pixel / 256 * len(CHARS))
        print(CHARS[index], end='')

    print()