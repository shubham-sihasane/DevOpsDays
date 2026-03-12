`docker version` ⌘ Check the docker version

`docker run <image-name>:<tag-name>` ⌘ Run docker container based on docker image:tag

`docker ps` ⌘ List the running docker containers

`docker ps -a` ⌘ List the running and non-running docker containers

`docker stop <container-name>/<container-ID>` ⌘ Stop a running docker container, -f to forcefully stop running container

`docker rm <container-name>/<container-ID>` ⌘ Remove a stopped docker container

`docker image ls` ⌘ List all the docker images

`docker rmi <image-name>` ⌘ Remove a docker image (Image should not have a container created out of that image)

`docker image pull <image-name>` ⌘ Pull/Download the docker image

`docker container exec <container-name/ID> <command-name>` ⌘ Run a command on a running container

`docker container run -d <image-name/ID>` ⌘ Run a docker container in the background

`docker container run -it <image-name/ID> <bash/sh>` ⌘ Run a container and attach interactive terminal to the running container

`docker container run -d --name <container-name> <image-name/ID>` ⌘ Run container in background and give a custom name to container

`docker container attach <container-name/ID>` ⌘ Attach to the terminal of a running container

`docker container run -d --name <container-name> -p <host-port:container-port> <image-name>:<tag>` ⌘ Map a host port to container port

`docker container -v <host-path>:<container-path> <image-name>` ⌘ Map / Mount the host path with container path

`docker container inspect <container-name/ID>` ⌘ Get details of a docker container

`docker container logs <container-name>/ID` ⌘ Get the logs of the container

`docker image history <image-name>` ⌘ Get the image history / layers information

`docker image build <Docker-Context> -t <image-name>` ⌘ Create a docker image from dockerfile by providing docker context for dockerfile, -f and dockerfile path if required

`IMAGE = registry/account/image-name` ⌘ docker.io/library/nginx

`docker login <server/registry-name>` ⌘ Login to private registry

`docker logout` ⌘ Logout from private registry

*Docker Networking*
- Bridge Network - Default Network, private, 172.17.0.1 range IP
- Host Network - Map host and container port on the same port
- None Network - No outside network access for container

`docker network ls` ⌘ List the default and custom networks

`docker network create --driver <driver-name> --subnet <subnet-range> <network-name>` ⌘ Create custom bridge network

`docker network inspect <network-name>` ⌘ Inspect the network details

`docker network connect <network-name> <container-name>` ⌘ Connect container to a network

`docker network disconnect <network-name> <container-name>` ⌘ Disconnect container from the network

`docker network rm <network-name>` ⌘ Remove the network

`docker network prune` ⌘ Prune (Remove one or more) docker network

`docker -H=<docker-daemon-host>:2375 run <image-name>` ⌘ Run docker container remotely

`docker run --cpus=<value> --memory=<value> <image-name>` ⌘ Create a container with specific amount of cpu and memory

*Docker Filesystem*
- /var/lib/docker - Docker's default location

`docker run -v <volume-name>:<container-path> <image-name>` ⌘ Create a volume mount

`docker run --mount type=bind,source=/data/mysql,target=<container-path> <image-name>` ⌘ Create container with storage

*Environment Variables*
`docker run -d -e <KEY>:<VALUE> <image-name>` ⌘ Create container by passing environment variable


```Dockerfile
FROM ubuntu
RUN apt-get update
RUN apt-get install pythong
RUN pip install flask
RUN pip install flask-mysql
COPY . /opt/source-code
ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
```

