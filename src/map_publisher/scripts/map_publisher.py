#! /usr/bin/env python

import sys
import os
from datetime import datetime

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image

import cv2

if __name__ == "__main__":
    rospy.init_node('map_publisher')

    pub = rospy.Publisher('/map', 'nav_msgs/OccupancyGrid', queue_size=10)

    try:
        map = open("map.jpg", "r")
        pub.Publish(map)
    except:
        print("Failed to load map image.")

    rospy.spin()
