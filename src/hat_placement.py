#!/usr/bin/env python3

from math import sqrt
from PIL import Image

# Rekognition doesn't do non-human faces. Do not have time to train a CNN and while scanning for green dots automatically does work, it finds dots in a pattern I don't have time to sus out. Below are the hardcoded coordinates for the four demo pictures.

cat_coord = [{'Image': 'image001_dots.jpg','LEar': (1240, 1732), 'REar': (1776, 1860), 'LEye': (1346, 2160), 'REye': (1575, 2190), 'Nose': (1440, 2350)}, {'Image': 'image002_dots.jpg', 'LEar': (726, 1705), 'REar': (1315, 1635), 'LEye': (1095, 2030), 'REye': (1310, 1960), 'Nose': (1350, 2150)}, {'Image': 'image003_dots.jpg', 'LEar': (140, 940), 'REar': (1190, 890), 'LEye': (705, 1645), 'REye': (1095, 1600), 'Nose': (1010, 1925)}, {'Image': 'image004_dots.jpg', 'LEar': (515, 70), 'REar': (1200, 175), 'LEye': (770, 515), 'REye': (1080, 535), 'Nose': (985, 680)}]

hats = {}

#stack exchange snippet: https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines
def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False
#end of snippet

#for each hat, calculate the x and y-offset of the ref-point


for pic in cat_coord:
    eye_slope = round((pic['LEye'][1] - pic['REye'][1])/(pic['LEye'][0] - pic['REye'][0]), 2)
    hat_rot = eye_slope
    ear_xmidpoint = round((pic['LEar'][0] + pic['REar'][0])/2, 0)
    hat_x = int(ear_xmidpoint)
    # Use the distance between the tips of the ears to dictate size of hat
    hat_size = int(sqrt(abs(pic['LEar'][0] ** 2 - pic['REar'][0] ** 2) + abs(pic['LEar'][1] ** 2 - pic['REar'][1] ** 2)))
    L1 = line([pic['LEar'][0], pic['LEar'][1]], [pic['REye'][0], pic['REye'][1]])
    L2 = line([pic['REar'][0], pic['REar'][1]], [pic['LEye'][0], pic['LEye'][1]])
    hat_y = int(round(intersection(L1, L2)[1], 0))

    print(pic['Image'] + ': (' + str(hat_x) + ', ' + str(hat_y) + '), ' + str(hat_rot) + ', ' + str(hat_size))
