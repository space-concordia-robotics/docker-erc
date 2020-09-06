#!/bin/bash

git clone https://github.com/space-concordia-robotics/erc_docker_img

# Install some basic dependencies
apt-get update && apt-get -y install \
  python-rosdep \
  python-catkin-tools \
  python-vcstool \
  ros-melodic-xacro \
  ros-melodic-map-server

# Clone required repos
vcs import < leo-erc.repos

# Rebuild workspace
rm -rf build/ devel/
apt-get update \
  && rosdep update \
  && rosdep install --from-paths src -iy \
  && rm -rf /var/lib/apt/lists/*

catkin config --extend /opt/ros/melodic && catkin build

apt update && apt upgrade -y && apt install vim -y

# allow for AR tags to be inserted into the gazebo world sim

## install dependencies for gazebo_models generation
apt-get install imagemagick -y

mv marsyard.world /src/marsyard/worlds/

mkdir -p /root/.gazebo/models \
  && cp -r /catkin_ws/src/gazebo_models/ar_tags/model/marker0/ /root/.gazebo/models \
  && cd /catkin_ws/src/gazebo_models/ar_tags/images \
  && mv Marker0.png t \
  && mkdir -p /root/temp \
  && mv Marker* /root/temp \
  && mv t Marker0.png \
  && cd ../scripts/ \
  && ./generate_markers_model.py -i ../images/ -s 125 -w 37 \
  && cp -r /root/.gazebo/models/marker0 /catkin_ws/src/marsyard/models/
