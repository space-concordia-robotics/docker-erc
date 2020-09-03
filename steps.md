# Steps for setting up the container

## clone the repo 
```
git clone https://github.com/space-concordia-robotics/erc_docker_img.git
```

## Build the docker image (this will take a while). 
The url is found under fleet>ERC>leorover>settings>installation. Only copy the https string **not the whole thing**.
```
docker build -t erc_img --build-arg FREEDOM_URL="<YOUR_URL>" .
``` 

## Allow docker user to connect to X window display
```
xhost +local:root
```

## Launch the image 
### With Nvidia GPU:
Install the [Nvidia Container Toolkit](https://github.com/NVIDIA/nvidia-docker)
And run:
```
docker run --rm -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY --gpus all -e NVID
IA_DRIVER_CAPABILITIES=all --name erc_img erc_img
```

### With intergrated graphics:
```
docker run --rm --device=/dev/dri -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY --name erc_img  erc_img
```
5. Open a new terminal window and start a terminal in the docker session
```
docker exec -it erc_img bash
```

