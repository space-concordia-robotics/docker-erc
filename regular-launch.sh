#! bin/bash
xhost +local:host
sudo docker run --rm --device=/dev/dri -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY --name erc_img  erc_img
