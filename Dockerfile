FROM ros:melodic

# These values will be overrided by `docker run --env <key>=<value>` command
ENV ROS_IP 127.0.0.1
ENV ROS_MASTER_URI http://127.0.0.1:11311

# Install some basic dependencies
RUN apt-get update && apt-get -y install \
  curl ssh \
  ros-melodic-cv-bridge \
  ros-melodic-tf \
  python-pip python3-pip \
  python-rosdep \
  python-catkin-tools \
  python-vcstool \
  ros-melodic-xacro \
  ros-melodic-map-server \
  && rm -rf /var/lib/apt/lists/*
  #ros-melodic-ar-track-alvar \

# Set root password
RUN echo 'root:root' | chpasswd

# Permit SSH root login
RUN sed -i 's/#*PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config

# Install Freedom agent
ARG FREEDOM_URL
RUN curl -sSf $FREEDOM_URL | \
  sed 's:a/nmkK3DkqZEB/ngrok-2.2.8-linux-arm64.zip:c/4VmDzA7iaHb/ngrok-stable-linux-arm64.zip:' | python \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /root/.cache/pip/* 

# Install catkin-tools
RUN apt-get update && apt-get install -y python-catkin-tools \
  && rm -rf /var/lib/apt/lists/*

# Copy packages and build the workspace
WORKDIR /catkin_ws
COPY leo-erc.repos ./
COPY src ./src
COPY map ./map
RUN vcs import < leo-erc.repos

# maybe useful, but not necessary for now ...
#COPY launch/marsyard_ar.launch ./src/leo_gazebo/launch

RUN apt-get update \
  && rosdep update \
  && rosdep install --from-paths src -iy \
  && rm -rf /var/lib/apt/lists/*

RUN catkin config --extend /opt/ros/melodic && catkin build

COPY start.sh /

RUN apt update && apt upgrade -y && apt install vim -y


ENTRYPOINT []
CMD ["/start.sh"]

# allow for AR tags to be inserted into the gazebo world sim

## install dependencies for gazebo_models generation
RUN apt-get install imagemagick -y

COPY ar_tags/marsyard.world ./src/marsyard/worlds/

## do the thing
### HACKY --> ammend later (maybe)

RUN mkdir -p /root/.gazebo/models \
  && cp -r /catkin_ws/src/gazebo_models/ar_tags/model/marker0/ /root/.gazebo/models \ 
  && cd /catkin_ws/src/gazebo_models/ar_tags/images \
  && mv Marker0.png t \
  && mkdir -p /root/temp \
  && mv Marker* /root/temp \
  && mv t Marker0.png \
  && cd ../scripts/ \
  && ./generate_markers_model.py -i ../images/ -s 125 -w 37 \
  && cp -r /root/.gazebo/models/marker0 /catkin_ws/src/marsyard/models/ 

