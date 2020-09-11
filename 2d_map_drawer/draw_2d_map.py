#!/usr/bin/env python2

import cv2
import numpy as np
import ast

import json
import sys

def convert_coordinates(coordinates, frame):
    #magic number calculated from the min max offset of the waypoints given for ERC2020
    x_offset = 2.53/2.0
    #y_offset = (23.89+13.24)/2.0
    y_offset = (30.06+13.24)/2.0
    FRAME_HEIGHT = frame.shape[0]
    FRAME_WIDTH = frame.shape[1]
    MARSYARD_WIDTH = 36.3
    MARSYARD_HEIGHT = 43.3
    x = coordinates[0]
    y = coordinates[1]
    x = float(x)
    y = float(y)
    print('x:', x)
    print('y:', y)
    x = (x+x_offset)/(MARSYARD_WIDTH) * FRAME_WIDTH
    y = (y+y_offset)/(MARSYARD_HEIGHT) * FRAME_HEIGHT
    print('x', x)
    print('y', y)
    return (int(x),int(y))

def draw_circles(img, coordinates, radius, color, thickness):
    frame = np.array(img, dtype=np.uint8)
    final_map = None

    for item in coordinates.items():
        item = (item[1][0], item[1][1])
        item = convert_coordinates(item, frame)
        # ADD CORRECTION SHIFT
        #item[1][0] = 
        #item[1][1] =
        print(item)
        final_map = cv2.circle(frame, item, radius, color, thickness)

    #print('coordinates.items()[1]:', coordinates.items()[1])
    #print('type --> :', coordinates.items()[1])

    #final_map = cv2.circle(frame, coordinates[0][1], radius, color, thickness)
    # save image
    cv2.imwrite('marked_map.jpg', final_map )

if len(sys.argv) <= 1:
    print('input arg missing: file name')
    sys.exit(1)

input_file = sys.argv[1]

#Reading images in color and grayscale
img = cv2.imread(input_file)

# convert the image to a numpy array since most cv2 functions
# require numpy arrays
frame = np.array(img, dtype=np.uint8)

shape = frame.shape                                                                                                                              
height = shape[0]
width = shape[1]

# Red color in BGR
color = (0, 0, 255)

# Line thickness of 2 px
thickness = 5

mid_x = width/2
mid_y = height/2
center_coordinates = (mid_x, mid_y)
radius = 5

# test data

#test_data = {'one':(mid_x, mid_y), 'two':(mid_x + mid_x/2, mid_y + mid_y/2)}

final_map = None

with open('data.json', 'r') as f:
    datastore = json.load(f)

#print('dir', dir(datastore))

draw_circles(img, datastore, radius, color, thickness)

'''
# Draw a rectangle with blue line borders of thickness of 2 px
for item in test_data.items():
    print('item[1]', item[1])
    print('item[1][0]', item[1][0])
    # ADD CORRECTION SHIFT
    #item[1][0] = 
    #item[1][1] = 
    final_map = cv2.circle(frame, item[1], radius, color, thickness)
'''

