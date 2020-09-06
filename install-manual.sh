#!/bin/bash

# Install some basic dependencies
apt-get update && apt-get -y install \
  python-rosdep \
  python-catkin-tools \
  python-vcstool \
  ros-melodic-xacro \
  ros-melodic-map-server

# Clone required repos
cd /catkin_ws
vcs import < leo-erc.repos

# Rebuild workspace
rm -rf build/ devel/
apt-get update \
  && rosdep update --rosdistro=melodic \
  && rosdep install --rosdistro=melodic --from-paths src -iy \
  && rm -rf /var/lib/apt/lists/*

catkin config --extend /opt/ros/melodic && catkin build

source devel/setup.bash

apt update && apt upgrade -y && apt install vim -y
