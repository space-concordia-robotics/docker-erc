#!/usr/bin/env python2

import cv2
import numpy as np

import sys

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

# Draw a rectangle with blue line borders of thickness of 2 px
#final_map = cv2.rectangle(frame, starting_point, ending_point, color, thickness)
final_map = cv2.circle(frame, center_coordinates, radius, color, thickness)

# save image
cv2.imwrite('marked_map.jpg', final_map )

