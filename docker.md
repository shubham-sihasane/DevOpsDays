`docker version` ⌘ Check the docker version

`systemctl <start/stop/enable/disable> docker` ⌘ Start/Stop/Enable/Disable docker service (dcokerd)

`docekrd --debug` ⌘ Display docker service logs in debug mode

`docker system df` ⌘ Show docker disk usage

`docker system events --since 60m` ⌘ Get real time events from the server, since last 60 min optional

`docker system info` ⌘ Display system-wide information

`docker system prune` ⌘ Remove unused data

`docker container ps` ⌘ List the running docker containers

`docker container ps -a` ⌘ List the running and non-running docker containers

`docker container create <image-name>` ⌘ Create a docker container from docker image

`docker container ls` ⌘ List running containers, -a for all including non-running containers, -l for extra details, -q for only docker-ID's, -aq for all ID's

`docker container start <image-name/ID>` ⌘ Start a docker container

`docker container run <image-name>:<tag-name>` ⌘ Run docker container based on docker image:tag (start and run together)

`docker container stop <container-name>/<container-ID>` ⌘ Stop a running docker container, -f to forcefully stop running container

`docker container --restart=<no/on-failure/always/unless-stopped>` ⌘ Apply policy for restarting a container, default is 'NO', Container must start at least once then only policy is applicable, on-failure=non-zero exit code, always=regardless of exist state, unless-stopped=always unless manually stopped

`docker container kill -SISGTOP <process-name>` ⌘ Pause the process inside the container

`docker container kill -SIGCONT <process-name>` ⌘ Unpause the process inside the container

`docker container kill -SIGTERM <process-name>` ⌘ Terminate the process inside the container politely

`docker container kill -SIGKILL` ⌘  Terminate the process inside the container and kill the process

`docker container pause <container-name/ID>` ⌘ Pause the running docker container

`docker container unpause <container-name/ID>` ⌘ Unpause the paused container

`docker container exec <container-name/ID> <command-name>` ⌘ Run a command on a running container

`docker container cp <source-path> <container-name>:<destination_path>` ⌘ Copy source content to destination, destination must exists else fails

`docker container rm <container-name>/<container-ID>` ⌘ Remove a stopped docker container

`docker container run -d --rm <image-name>` ⌘ Remove a container when it stops

`docker container prune` ⌘ Remove all stopped containers

`docker container run -d <image-name/ID>` ⌘ Run a docker container in the background

`docker container run -it <image-name/ID> <bash/sh>` ⌘ Run a container and attach interactive terminal to the running container

`docker container run -d --name <container-name> <image-name/ID>` ⌘ Run container in background and give a custom name to container

`docker container attach <container-name/ID>` ⌘ Attach to the terminal of a running container

`docker container run -d --name <container-name> -p <host-port:container-port> <image-name>:<tag>` ⌘ Map a host port to container port

`docker container run -P <image-name>` ⌘ Exposes port from docker image file if ports not given, Mapping = Exposed Port:Random port on host

`docekr container run -P --expose=8080 <image-name>` ⌘ Expose specific host port while creating container

`docker container run -it --name=<container-name> --hostname=<hostname> <image-name>` ⌘ Create container with name and hostname, hostname could be same for containers while container name must be unique

`docker container rename <old-name> <new-name>` ⌘ Rename a docker container

`docker container -v <host-path>:<container-path> <image-name>` ⌘ Map / Mount the host path with container path

`docker container inspect <container-name/ID>` ⌘ Get details of a docker container

`docker container stats` ⌘ Get details around all running containers around cpu/memory/IO details

`docker container top <container-name/ID>` ⌘ List the processes and ID of a container

`docker container logs <container-name>/ID` ⌘ Get the logs of the container

####--------------IMAGES----------------------------------------

`docker image ls` ⌘ List all the docker images

`docker image search <image-name>` ⌘ Search images on docker hub, --limit N for N images, --filter stars=N for images having N stars

`docker image pull <image-name>` ⌘ Pull/Download the docker image

`docker image list` ⌘ List the docker images

`docker login <server/registry-name>` ⌘ Login to private registry

`docker logout` ⌘ Logout from private registry

`docker image rmi <image-name>` ⌘ Remove a docker image (Image should not have a container created out of that image)

`docker image prune` ⌘ Remove all unused docker images

`docker image history <image-name>` ⌘ Get the image history / layers information

`docker image inspect <image-name>` ⌘ Get detailed information about the image

`docker image save <image-name>:<tag-name> -o <tarfile-name>` ⌘ Create a tarball file from docker image

`docker image load -i <tarfile-name>` ⌘ Convert tarball file into docker image

`docker export <container-name> > <tarfile-name>` ⌘ Export a container as tar file

`docker image import <tarfile-name> <image-name>` ⌘ Import a container tarfile into a docker image

`docker image build <Docker-Context> -t <image-name>` ⌘ Create a docker image from dockerfile by providing docker context for dockerfile, -f and dockerfile path if required

`IMAGE = registry/account/image-name` ⌘ docker.io/library/nginx

*Docker Networking*
- Bridge Network - Default Network, private, 172.17.0.1 range IP
- Host Network - Map host and container port on the same port
- None Network - No outside network access for container

####-------------------NETWORK-------------------------

`docker network ls` ⌘ List the default and custom networks

`docker network create --driver <driver-name> --subnet <subnet-range> <network-name>` ⌘ Create custom bridge network

`docker network inspect <network-name>` ⌘ Inspect the network details

`docker network connect <network-name> <container-name>` ⌘ Connect container to a network

`docker network disconnect <network-name> <container-name>` ⌘ Disconnect container from the network

`docker network rm <network-name>` ⌘ Remove the network

`docker network prune` ⌘ Prune (Remove one or more) docker network

`docker -H=<docker-daemon-host>:2375 run <image-name>` ⌘ Run docker container remotely

`docker run --cpus=<value> --memory=<value> <image-name>` ⌘ Create a container with specific amount of cpu and memory

####------------------VOLUME-------------------

*Docker Filesystem*
- /var/lib/docker - Docker's default location

`docker volume create <volume-name>` ⌘ Create a docker volume

`docker volume ls` ⌘ List the docker volumes in the system

`docker volume inspect <volume-name>` ⌘ Display detailed information on one or more volumes

`docker volume rm <volume-name>` ⌘ Remove one or more volumes

`docker volume prune` ⌘ Remove unused local volumes

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

