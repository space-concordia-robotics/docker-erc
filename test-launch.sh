#! /bin/bash
xhost +local:root
sudo docker run --rm -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY --gpus all -e NVIDIA_DRIVER_CAPABILITIES=all --name test_img test_img
