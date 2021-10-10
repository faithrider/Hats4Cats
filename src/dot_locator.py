#!/usr/bin/env python3

import numpy as np
from PIL import Image
import math

hats = ['fez_dot.png', 'party_hat_dot.png', 'santa_hat_dot.png', 'straw_hat_dot.png', 'top_hat_dot.png']

# Load image and ensure RGB - just in case palettised
def find_dot(name):
        im = Image.open(name).convert("RGB")
        #im=Image.open('../samples/image001_crop.jpg').convert("RGB")

        # Make numpy array from image
        npimage = np.array(im)

        # Describe what a single green pixel looks like
        green = np.array([0,255,0],dtype=np.uint8)

        # Find [x,y] coordinates of all green pixels
        dots = np.where(np.all((npimage==green),axis=-1))
        coord = zip(dots[0], dots[1])
        # print(coord)

        tmpArrayX = []
        tmpArrayY = []
        ArrayX = []
        ArrayY = []

        for n, y in enumerate(coord):
                if n == 0 or not tmpArrayX:
                        tmpArrayY.append(y[0])
                        tmpArrayX.append(y[1])
                        continue

                if (abs(tmpArrayX[-1] - y[1]) < 50) and (abs(tmpArrayY[-1] - y[0]) < 50):
                        tmpArrayY.append(y[0])
                        tmpArrayX.append(y[1])
                        continue
                

                dotx = round(np.mean(tmpArrayX), 0)
                doty = round(np.mean(tmpArrayY), 0)
                tmpArrayX = []
                tmpArrayY = []
                ArrayX.append(dotx)
                ArrayY.append(doty)
                print(str(n) + ', ' + str(dotx) + ', ' + str(doty))

for i in range(1, 5):
        name = '../cats/image' + str(i).zfill(3) + '_dots.jpg'
        print(name)
        find_dot(name)

for hat in hats:
        name = '../hats/' + hat
        print(name)
        find_dot(name)
