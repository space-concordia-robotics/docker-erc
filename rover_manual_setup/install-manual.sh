#!/bin/bash

git clone https://github.com/space-concordia-robotics/docker-erc.git

# Copy required files to catkin workspace
cp -r docker-erc/src/* /catkin_ws/src/
cp -r docker-erc/map /catkin_ws/map
cp -r docker-erc/leo-erc.repos /catkin_ws/
cp -r docker-erc/controllers.yaml /catkin_ws/src/leo_gazebo/config/
cp -r docker-erc/octomap/terrain_mapping.launch /catkin_ws/src/octomap_mapping/octomap_server/launch/

# Install some basic dependencies
apt-get update && apt-get -y install \
  curl ssh \
  ros-melodic-cv-bridge \
  ros-melodic-tf \
  python-pip python3-pip \
  python-rosdep \
  python-catkin-tools \
  python-vcstool \
  ros-melodic-xacro \
  ros-melodic-map-server \
  ros-melodic-ar-track-alvar \
  ros-melodic-rqt-graph \
  sl \
  imagemagick \
  && rm -rf /var/lib/apt/lists/*

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
