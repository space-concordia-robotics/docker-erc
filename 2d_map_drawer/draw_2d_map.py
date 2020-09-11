#!/usr/bin/env python3

import sys
import json
import argparse

import cv2
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('-map', help='path to map file (.jpg image)')
parser.add_argument('-x', help='add meters to x offset')
parser.add_argument('-y', help='add meters to y offset')
args = parser.parse_args()


# magic number calculated from the min max offset of the waypoints given for ERC2020
x_offset = 2.53/2.0
if args.x:
    x_offset = x_offset+float(args.x)

y_offset = (30.06+13.24)/2.0-2
if args.y:
    y_offset = y_offset-float(args.y)

print(x_offset, y_offset)

# Mars yard dimensions 36.3 m x 46.3 m
MARSYARD_WIDTH = 36.3
MARSYARD_HEIGHT = 43.3

def convert_coordinates(coordinates, frame):

    x_m = float(coordinates[0])
    y_m = float(coordinates[1])
    x = int((x_m+x_offset)/(MARSYARD_WIDTH) * width)
    y = int((y_offset-y_m)/(MARSYARD_HEIGHT) * height)
    print('------------CONVERSION-------------')
    print('x: {:-1} m -> {:-1} px'.format(x_m, x))
    print('y: {:-1} m -> {:-1} px'.format(y_m, y))
    print()
    return (x,y)

def draw_circles(img, coordinates):

    # Radius of circle
    radius = 30

    # Red color in BGR
    color = (0, 0, 255)

    # Line thickness of 5 px
    thickness = 2

    frame = np.array(img, dtype=np.uint8)
    final_map = None

    count = 0

    for item in (coordinates.items()):
            
            # Print different color for start
            if count == 0:
                color = (255, 0, 255)
            elif count == 15:
                color = (255, 0, 255)
            else:
                color = (0, 0, 255)
            item = (item[1][0], item[1][1])
            item = convert_coordinates(item, frame)
            final_map = cv2.circle(frame, item, radius, color, thickness)
            if count < 10:
                final_map = cv2.putText(frame, str(count), (item[0]-10, item[1]+12), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255),2, cv2.LINE_AA)
            else:
                final_map = cv2.putText(frame, str(count), (item[0]-22, item[1]+12), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255),2, cv2.LINE_AA)
                
            count += 1

    cv2.imwrite('marked_map.jpg', final_map )
    return final_map

def draw_grid(img):

    final_map = None

    # Draw a rectangle with blue line borders of thickness of 2 px
    thickness = 1
    
    # White color in BGR
    color = (0, 255, 0)
    y_step = int(height/MARSYARD_HEIGHT)
    x_step = int(width/MARSYARD_WIDTH)

    y_stepy = height/MARSYARD_HEIGHT
    x_stepy = width/MARSYARD_WIDTH
    print('x: ', x_stepy)
    print('y: ', y_stepy)
    
    # draw vertical
    for step in range(0, width, x_step*5):
        starting_point = tuple([step, 0])
        ending_point = tuple([step, height])
        final_map = cv2.line(img, starting_point, ending_point, color, thickness)
        final_map = cv2.putText(img, str(step/x_step), (step+1, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0),1, cv2.LINE_AA)
        
    # draw horizontal
    for step in range(0, height, y_step*5):
        starting_point = tuple([0, step])
        ending_point = tuple([width, step])
        final_map = cv2.line(img, starting_point, ending_point, color, thickness) 
        final_map = cv2.putText(img, str(step/y_step), (5, step-1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0),1, cv2.LINE_AA)
    thickness = 2
    color = (255, 255, 0) 
    final_map = cv2.line(img, tuple([0,0]), tuple([0, height]), color, thickness)
    final_map = cv2.line(img, tuple([width-thickness,0]), tuple([width-thickness, height]), color, thickness)
    final_map = cv2.line(img, tuple([0, 0]), tuple([height, 0]), color, thickness)
    final_map = cv2.line(img, tuple([0, height-thickness]), tuple([height, height-thickness]), color, thickness)
         
    cv2.imwrite('marked_map.jpg', final_map )
    return final_map



if len(sys.argv) <= 1:
    print('input arg missing: file name')
    sys.exit(1)
#input_file = sys.argv[1]
input_file = args.map
    
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

# draw waypoints with label
img = draw_circles(img, datastore)

# draw grid on map with scale
draw_grid(img)

