# uses numpy, pillow
# contains a random dithering function commented out on line 27

from PIL import Image
import numpy
import random

img = Image.open('lighthouse.png')
img = numpy.array(img).astype(int)
new_img = numpy.array(img)
threshold = 0
t = 0

ditherMatrix = 1/16 * numpy.array([
    [15, 7, 13, 5], [3, 11, 1, 9],
    [12, 4, 14, 6], [0, 8, 2, 10]
])

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        #contrast -
       new_img[y, x] = (t*img[y, x]) + (1-t)*127
       # saturation -
       L = 0.3 * img[y,x][0] + 0.59*img[y,x][1] + 0.11*img[y,x][2]
       new_img[y, x] = (t*img[y, x]) + (1-t)*L

       #random dithering
       #randomNum = random.randint(0,2)
       #if randomNum != 0:
       #     if new_img[y,x, 0] > 127:
       #         new_img[y,x] = 255
       #     else:
       #         new_img[y,x] = 0

       threshold = ditherMatrix[y % 4, x % 4] * 255
       if new_img[y,x, 0] > threshold:
           new_img[y,x] = 255
       else:
            new_img[y,x] = 0

new_img = numpy.clip(new_img, 0, 255)
Image.fromarray(new_img.astype(numpy.uint8)).save('output.png')
