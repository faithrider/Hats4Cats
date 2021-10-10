#!/usr/bin/env python3

import math
from PIL import Image

# Rekognition doesn't do non-human faces. Do not have time to train a CNN and while scanning for green dots automatically does work, it finds dots in a pattern I don't have time to sus out. Below are the hardcoded coordinates for the four demo pictures.

cats = [{'Image': 'image001', 'LEar': (1240, 1732), 'REar': (1776, 1860), 'LEye': (1346, 2160), 'REye': (1575, 2190), 'Nose': (1440, 2350)},
    {'Image': 'image002', 'LEar': (726, 1705), 'REar': (1315, 1635), 'LEye': (1095, 2030), 'REye': (1310, 1960), 'Nose': (1350, 2150)},
    {'Image': 'image003', 'LEar': (140, 940), 'REar': (1190, 890), 'LEye': (705, 1645), 'REye': (1095, 1600), 'Nose': (1010, 1925)},
    {'Image': 'image004', 'LEar': (515, 70), 'REar': (1200, 175), 'LEye': (770, 515), 'REye': (1080, 535), 'Nose': (985, 680)}]

# for each hat, calculate the x and y-offset of the ref-point
hats = [{'Image': 'fez', 'refpoint': (5045, 5330)},
    {'Image': 'party_hat', 'refpoint': (5040, 6475)},
    {'Image': 'santa_hat', 'refpoint': (5980, 4250)},
    {'Image': 'straw_hat', 'refpoint': (5215, 5000)},
    {'Image': 'top_hat', 'refpoint': (5175, 5260)}]

# stack exchange snippet: https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines
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


for cat in cats:
    eye_slope = round((cat['LEye'][1] - cat['REye'][1])/(cat['LEye'][0] - cat['REye'][0]), 2)
    hat_rot = eye_slope
    ear_xmidpoint = round((cat['LEar'][0] + cat['REar'][0])/2, 0)
    #eye_xmidpoint = round((cat['LEye'][0] + cat['REye'][0])/2, 0)
    hat_x = int(ear_xmidpoint)
    #hat_x = int(eye_xmidpoint)
    # Use the distance between the tips of the ears to dictate size of hat
    hat_size = int(math.sqrt(abs(cat['LEar'][0] ** 2 - cat['REar'][0] ** 2) + abs(cat['LEar'][1] ** 2 - cat['REar'][1] ** 2)))
    Line1 = line([cat['LEar'][0], cat['LEar'][1]], [cat['REye'][0], cat['REye'][1]])
    Line2 = line([cat['REar'][0], cat['REar'][1]], [cat['LEye'][0], cat['LEye'][1]])
    hat_y = int(round(intersection(Line1, Line2)[1], 0))

    print(cat['Image'] + ': (' + str(hat_x) + ', ' + str(hat_y) + '), ' + str(hat_rot) + ', ' + str(hat_size))

    for hat in hats:
        catPath = "../cats/" + cat['Image'] + '.jpg'
        hatPath = "../hats/" + hat['Image'] + '.png'
        outPath = "../cats/" + cat['Image'] + '_' + hat['Image'] + '.png'
        imgCat = Image.open(catPath)
        imgHat = Image.open(hatPath)
        largeSize = imgHat.size
        refxpercent = (hat['refpoint'][0])/largeSize[0]
        refypercent = (hat['refpoint'][1])/largeSize[1]
        newXsizeRatio = (hat_size)/largeSize[0]
        newXsize = int(largeSize[0] * newXsizeRatio)
        newYsize = int(largeSize[1] * newXsizeRatio)
        newXref = hat_x - int(newXsize * refxpercent)
        newYref = hat_y - int(newYsize * refypercent)
        newRefPoint = (newXref, newYref)
        imgHat = imgHat.rotate(eye_slope, resample=Image.BILINEAR,
            expand=(newXsize, newYsize), center=newRefPoint)
        # TODO: Make hat rotate good and do other stuff good too
        # imgHat = imgHat.rotate(math.degrees(math.atan(eye_slope)), resample=Image.BILINEAR,
        #     center=newRefPoint)
        imgHat = imgHat.resize((newXsize, newYsize), Image.BILINEAR)
        print(f'largeSize: {largeSize}, refxpercent: {refxpercent}, refypercent: {refypercent}, newXsizeRatio: {newXsizeRatio}, newXsize: {newXsize}, newYsize: {newYsize}, newXref: {newXref}, newYref: {newYref}, newRefPoint: {newRefPoint}')
        imgCat.paste(imgHat, newRefPoint, imgHat)
        imgCat.save(outPath)
