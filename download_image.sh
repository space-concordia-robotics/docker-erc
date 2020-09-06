#!/bin/bash
# Arg1 : Port
# Arg2 : Start of address - the first number of the address sometimes changes

if [ -z "$1" ]; then
  echo "Missing port. Check Freedom Robotics to get the port"
  exit 1
fi

if [ -z "$2" ]; then
  echo "Missing start of address. Check Freedom Robotics to get the number of the address"
  exit 1
fi

mkdir -p ~/rover_images
echo "Password is root. If it doesn't work, you might need to enable SSH on FreedomRobotics. Make sure the port is correct."

scp -P $1 root@$2.tunnel.freedomrobotics.ai:/catkin_ws/image_*.png ~/rover_images/
