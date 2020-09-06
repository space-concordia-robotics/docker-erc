#!/bin/bash
# Arg1 : Port

if [ -z "$1" ]; then
  echo "Missing port. Check Freedom Robotics to get the port"
  exit 1
fi

echo "Password is root. If it doesn't work, you might need to enable SSH on FreedomRobotics. Make sure the port is correct."

scp -P $1 -r regular-launch.sh map/ src/ leo-erc.repos ar_tags/marsyard.world root@0.tunnel.freedomrobotics.ai:/catkin_ws/
ssh root@0.tunnel.freedomrobotics.ai -p $1 ./install_manual.sh
