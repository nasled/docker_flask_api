# docker_flask_api
RESTful API Web Service Implementation based on Flask wrapped in Docker 

This service saves and outputs Car Document to MongoDB.
Document example:
```
{
    title: "Jeep Wrangler Sahara",
    drive_type: "4wd",
    transmission: "automatic",
    engine_size: 3.6,
    year: 2018,
    cylinders: 6,
    width: 73.7,
    height: 72.6,
    weight: 4055
}
```

## How to Deploy

### Install dependencies
```
sudo pacman -S docker docker-compose
```

### Build containers 
```
sudo docker-compose build
```

### Run in background
```
sudo docker-compose up -d
```

## How to Use

### Test from host or docker container
```
curl -XGET localhost:5000
curl -XPOST http://localhost:5000/save -d '{"title": "Jeep Wrangler Sahara", "drive_type": "4wd", "transmission": "automatic", "engine_size": 3.6, "year": 2018, "cylinders": 6, "width": 73.7, "height": 72.6, "weight": 4055}'
curl -XPOST http://localhost:5000/save -d '{"title": "Dodge Ram", "drive_type": "4wd", "transmission": "automatic", "engine_size": 3.6, "year": 2016, "cylinders": 6, "width": 79, "height": 75, "weight": 5226}'
curl -XPOST http://localhost:5000/save -d '{"title": "Honda Accord EX-L", "drive_type": "2wd", "transmission": "automatic", "engine_size": 3.5, "year": 2016, "cylinders": 6, "width": 73, "height": 56, "weight": 3528}'
curl -XPOST http://localhost:5000/save -d '{"title": "2015 Hyundai Sonata", "drive_type": "2wd", "transmission": "automatic", "engine_size": 2.4, "year": 2016, "cylinders": 4, "width": 73, "height": 58, "weight": 3245}'
curl -XGET http://localhost:5000/list
curl -XGET http://localhost:5000/get/5cc016f93b80a16ee15ffd36
```

## Usefull Commands

### Build image
```
sudo docker build -t art/flask .
```

### Run container
```
sudo docker run -d -p 5000:5000 --name flaskc art/flask
```

### Remove stopped containers
```
sudo docker container prune
```

### Remove stopped images
```
sudo docker image prune
```

### Remove unused data
```
sudo docker system prune
```

### Remove all images
```
sudo docker rmi $(sudo docker images -aq)
```

### View container logs
```
sudo docker logs flaskc
```

### Shell into the container
```
sudo docker exec -ti flaskc /bin/bash
```
   

