#!/bin/bash -em

source /catkin_ws/devel/setup.bash

echo "source /catkin_ws/devel/setup.bash" >> /etc/bash.bashrc
echo "ROS_IP=${ROS_IP}" >> /etc/environment
echo "ROS_MASTER_URI=${ROS_MASTER_URI}" >> /etc/environment

python /root/.local/lib/python2.7/site-packages/freedomrobotics/agent.py &

roslaunch erc_example erc_bringup.launch &

# CUSTOM SCRIPTS GO HERE
roslaunch webcam_ar_track webcam_indiv.launch &
rosrun camera_vision ar_tracker.py &

fg %1
