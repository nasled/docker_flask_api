# docker_flask_api
Example of Flask API application wrapped in Docker

# build image
sudo docker build -t art/flask .

# run container
sudo docker run -d --name flaskc art/flask

sudo docker run -d -p 5000:5000 –-restart=always --name flaskc art/flask


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


# test from host
curl -XGET localhost:5000