#!/usr/bin/env python2
import sys

import rospy
import cv2
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

class arTrackerDemo():
    def __init__(self):
        # necessary for handling images from topics
        self.node_name = 'ar_tracker'
        rospy.init_node(self.node_name)

        # what we do during shutdown
        rospy.on_shutdown(self.cleanup)

        # create the cv_bridge object
        self.bridge = CvBridge()

        # subscribe to the camera image and depth topics and set
        # the appropriate callbacks
        self.image_sub = rospy.Subscriber('/camera/image_raw', Image, self.image_callback)

        # create publisher for new feed with overlay
        self.image_pub = rospy.Publisher('/camera/image_ar', Image, queue_size=10)

        rate = rospy.Rate(1) # 1hz, take it easy 8-)

        rospy.loginfo('Waiting for image topics...')

    def image_callback(self, ros_image):
        # use cv_bridge() to convert the ROS image to OpenCV format
        try:
            frame = self.bridge.imgmsg_to_cv2(ros_image, 'bgr8')
            #print('frame', frame)
        except CvBridgeError:
            traceback.print_exc()

        # convert the image to a numpy array since most cv2 functions
        # require numpy arrays
        frame = np.array(frame, dtype=np.uint8)

        #print('np_frame', frame)

        # Starting coordinate, here (100, 100)
        # Represents the top left corner of rectangle
        starting_point = (100, 100)

        # Ending coordinate, here (400, 400)
        # Represents the bottom right corner of rectangle
        ending_point = (300, 300)

        # Blue color in BGR
        color = (255, 0, 0)

        # Line thickness of 2 px
        thickness = 2

        # Draw a rectangle with blue line borders of thickness of 2 px
        image = cv2.rectangle(frame, starting_point, ending_point, color, thickness)

        # Publish the new overlay including image to topic '/camera/image_ar'
        self.image_pub.publish(self.bridge.cv2_to_imgmsg(image))

    def cleanup(self):
        print('shutting down ar_tracker node')

def main(args):
    try:
        arTrackerDemo()
        rospy.spin()
    except KeyboardInterrupt:
        print('shutting down ar_tracker node')

if __name__ == '__main__':
    main(sys.argv)
