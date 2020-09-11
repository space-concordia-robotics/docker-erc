#!/usr/bin/env python2

import cv2
import numpy as np

import sys

def draw_circles():
    return False

if len(sys.argv) <= 1:
    print('input arg missing: file name')
    sys.exit(1)

input_file = sys.argv[1]

#Reading images in color and grayscale
color_img = cv2.imread(input_file)

# convert the image to a numpy array since most cv2 functions
# require numpy arrays
frame = np.array(color_img, dtype=np.uint8)

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

test_data = {'one':(mid_x, mid_y), 'two':(mid_x + mid_x/2, mid_y + mid_y/2)}

final_map = None
# Draw a rectangle with blue line borders of thickness of 2 px
for item in test_data.items():
    print('frame', frame)
    print('item', item)
    print('radius', radius)
    print('color', color)
    print('thickness', thickness)
    final_map = cv2.circle(frame, item[1], radius, color, thickness)

# save image
cv2.imwrite('marked_map.jpg', final_map )

def draw_circles(img, coordinates, radius, color, thickness):
    frame = np.array(img, dtype=np.uint8)
    final_map = None

    # Draw a rectangle with blue line borders of thickness of 2 px
    for item in test_data.items():
        frame = np.array(final_map, dtype=np.uint8)
        final_map = cv2.circle(frame, item, radius, color, thickness)

    return False
