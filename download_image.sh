#!/bin/bash
# Arg1 : Port

if [ -z "$1" ]; then
  echo "Missing port. Check Freedom Robotics to get the port"
  exit 1
fi

mkdir -p ~/rover_images
echo "Password is root. If it doesn't work, you might need to enable SSH on FreedomRobotics. Make sure the port is correct."

scp -P $1 root@0.tunnel.freedomrobotics.ai:/catkin_ws/image_*.png ~/rover_images/

