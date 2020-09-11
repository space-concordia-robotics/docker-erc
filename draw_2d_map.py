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

# Starting coordinate
# Represents the top left corner of rectangle
starting_point = (width/2 - width/5, height/2 - height/5)

# Ending coordinate
# Represents the bottom right corner of rectangle
ending_point = (width/2 + width/5, height/2 + width/5)

# Red color in BGR
color = (0, 0, 255)

# Line thickness of 2 px
thickness = 2

# Draw a rectangle with blue line borders of thickness of 2 px
final_map = cv2.rectangle(frame, starting_point, ending_point, color, thickness)


# save image
cv2.imwrite('marked_map.jpg', final_map )

