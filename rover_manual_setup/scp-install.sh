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

echo "Password is root. If it doesn't work, you might need to enable SSH on FreedomRobotics. Make sure the port is correct."

scp -P $1 -r install-manual.sh root@$2.tunnel.freedomrobotics.ai:/catkin_ws/
ssh root@$2.tunnel.freedomrobotics.ai -p $1 . /catkin_ws/install-manual.sh
