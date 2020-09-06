#! bin/bash
echo "Enter the freedom api URL:"
read URL
sudo docker build -t erc_img --build-arg FREEDOM_URL="$URL" .

