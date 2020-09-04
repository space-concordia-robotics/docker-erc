#!/bin/bash

mkdir -p ~/rover_images

scp -P 10900 root@0.tunnel.freedomrobotics.ai:/catkin_ws/image_*.png ~/rover_images/

