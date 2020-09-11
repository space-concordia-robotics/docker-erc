#!/usr/bin/env python2

import cv2
import numpy as np
import ast

import json
import sys

# magic number calculated from the min max offset of the waypoints given for ERC2020
x_offset = 2.53/2.0
y_offset = (30.06+13.24)/2.0

# Mars yard dimensions 36.3 m x 46.3 m
MARSYARD_WIDTH = 36.3
MARSYARD_HEIGHT = 43.3

def convert_coordinates(coordinates, frame):

    x = float(coordinates[0])
    y = float(coordinates[1])
    print('------------INPUT--------------')
    print('x:', x)
    print('y:', y)
    x = (x+x_offset)/(MARSYARD_WIDTH) * width
    y = (y+y_offset)/(MARSYARD_HEIGHT) * height
    print('------------OUTPUT--------------')
    print('x', x)
    print('y', y)
    return (int(x),int(y))

def draw_circles(img, coordinates):

    # Radius of circle
    radius = 5

    # Red color in BGR
    color = (0, 0, 255)

    # Line thickness of 5 px
    thickness = 5

    frame = np.array(img, dtype=np.uint8)
    final_map = None

    count = 0

    for item in sorted (coordinates.items()):
            if count == 0:
                color = (255, 0, 255)
            else:
                color = (0, 0, 255)
            item = (item[1][0], item[1][1])
            item = convert_coordinates(item, frame)
            final_map = cv2.circle(frame, item, radius, color, thickness)
            count += 1

    cv2.imwrite('marked_map.jpg', final_map )
    return final_map


def draw_grid(img):

    final_map = None

    # Draw a rectangle with blue line borders of thickness of 2 px
    thickness = 1
    
    # White color in BGR
    color = (0, 255, 0)
    y_step = int(height/43.3)
    x_step = int(width/36.3)
    
    # draw vertical
    for step in range(0, width, x_step*5):
        starting_point = tuple([step, 0])
        ending_point = tuple([step, height])
        final_map = cv2.line(img, starting_point, ending_point, color, thickness)    
        
    # draw horizontal
    for step in range(0, height, y_step*5):
        starting_point = tuple([0, step])
        ending_point = tuple([width, step])
        final_map = cv2.line(img, starting_point, ending_point, color, thickness)    
         
    cv2.imwrite('marked_map.jpg', final_map )
    return final_map

if len(sys.argv) <= 1:
    print('input arg missing: file name')
    sys.exit(1)
input_file = sys.argv[1]
    
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

with open('data.json', 'r') as f:
    datastore = json.load(f)

print(type(datastore))

#sort_json(datastore)

img = draw_circles(img, datastore)
draw_grid(img)

