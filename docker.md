`docker -v` OR `docker --version` ⌘ Print docker version information and quit

`docker system info` ⌘ Display system-wide information around docker

`docker system df` ⌘ Display docker disk usage

`docker system prune` ⌘ Remove unused docker data

`docker system events` ⌘ Get real time events from docker

`docker container ps` OR `docker container ls` ⌘ Display running containers

`docker container ps -a` OR `docker container ls -a` ⌘ Display running and stopped containers

`docker container run <image>` ⌘ Create and run a new container from image

`docker container logs <name/ID>` ⌘ Fetch the logs of a container

`docker container inspect <name/ID>` ⌘ Display detailed information of container

`docker container stop <name/ID>` ⌘ Stop one or more running containers

`docker container create <name/ID>` ⌘ Create a new container

`docekr container restart <name/ID>` ⌘ Restart a one or more stopped container

`docker container start <name/ID>` ⌘ Start one or more stopped containers

`docker container pause <name/ID>` ⌘ Pause one or more running containers

`docker container unpause <name/ID>` ⌘ Unpause one or more paused containers

`docker container rename <old-name> <new-name>` ⌘ Rename container old name with new name

`docker container stats` ⌘ Display docker containers statistics

`docker container top`⌘ Display the running processes of a container

`docker container rm <name/ID>` ⌘ Remove stopped container

`docker container kill <name/ID>` ⌘ Kill one or more running containers

`docker container prune` ⌘ Remove all stopped containers

`docker container exec <name/ID> <command>` ⌘ Execute a command in a running container

`docker container attach <name/ID>` ⌘ Attach local standard input, output, and error streams to a running container

`docker container run -it <-image-name>` ⌘ Create a container and attach interactive terminal

`docker container run -d --name <name> -p <host-port>:<container-port> <image>` ⌘ All in one

  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  export      Export a container's filesystem as a tar archive
  port        List port mappings or a specific mapping for the container
  update      Update configuration of one or more containers
  wait        Block until one or more containers stop, then print their exit codes

------------------------

`docker image build .` OR `docker image build -f <dockerfile> .`  Build a docker image

`docker image history <image-name>` ⌘ Show the history of image

`docker image inspect <image-name>` ⌘ Display detailed information of one or more image

`docker image ls` ⌘ List docker images on system

`docker image prune` ⌘ Remove unused images

`docker image pull <image-name>` ⌘ Pull docker image from docker hub by default

`docker image push <image-name>` ⌘ Push docker image to docker hub by default

`docker login` ⌘ Login to docker registry, docker hub by default

`docker logout` ⌘ Logout from docker registry, docker hub by default

`docker image rm <image-name>` OR `docker image rmi <image-name>` ⌘ Remove one or more local docker images

  import      Import the contents from a tarball to create a filesystem image
  load        Load an image from a tar archive or STDIN
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  
`docker volume create <volume-name>` ⌘ Create a docker volume

`docker volume inspect <volume-name>` ⌘ Display detailed information on one or more volumes

`docker volume ls` ⌘ List volumes

`docker volume rm <volume-name>` ⌘ Remove one or more volumes

`docker volume prune` ⌘ Remove unused local volumes