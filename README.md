# docker_flask_api
Example of Flask API application wrapped in Docker


## install dependencies
sudo pacman -S docker docker-compose

# build containers 
sudo docker-compose build

# run in background
sudo docker-compose run -d


# build image
sudo docker build -t art/flask .

# run container
sudo docker run -d -p 5000:5000 --name flaskc art/flask

# remove stopped containers
sudo docker container prune

# remove stopped images
sudo docker image prune

# remove unused data
sudo docker system prune

# remove all images
sudo docker rmi $(sudo docker images -aq)

# view container logs
sudo docker logs flaskc

# shell into the container
sudo docker exec -ti flaskc /bin/bash


# test from host or docker container
curl -XGET localhost:5000