https://learn.cantrill.io/p/docker-fundamentals
## COURSE INTRODUCTION
### Connect with me and join the community
 - if you want to be successful in tech then you need to network with people.
 - TechStudySlack
 - It's important and you should do all of these things
### course resources

- https://github.com/acantril/docker-fundamentals

## INTRODUCTION TO DOCKER
### Physical servers versus virtual machines
- Buy physical servers upfront -> so you own 100% of it, but 100% of the problems are yours.
- It's just hardware:
  - motherboard
  - CPUs
  - Memory
  - storafe
  - GPUs/Add on cards
- The sizes are the key. You want to use all of it so as not to be wasting money,
- conceptually:
  - You start with the operating system
  - You have a runtime environement
  - on which you have an application
  - Then there's the rest of the server, which is idle. Thhis is either:
    - wasting money
    - or consume it with other applications.
      - If you choose apps that have their usage peaks at different times then you can be quite efficient
      - but if one app fails it can screw up the others

<img width="561" height="321" alt="Screenshot 2025-08-22 at 13 23 04" src="https://github.com/user-attachments/assets/8f66f192-09db-4f75-bb83-e56a73685529" />

- this approach was the traditional way, but it wasn't very effective so was replaced by virtual servers
#### [Virtual servers](https://learn.cantrill.io/courses/docker-fundamentals/lectures/44151189)

- [04:00]
- Hypervisors [04:30] -> it's job is to manage physical resources within a server.
- On top of the hypervisor we run virtual machines.
- [07:30] VM migration
  - can be automated
- virtual machines are faster and more efficient.
- They are cut off from each other. 
<img width="559" height="311" alt="Screenshot 2025-08-22 at 13 29 46" src="https://github.com/user-attachments/assets/7db8b6b4-749c-4fec-b485-d71c3469e03b" />

### [What are containers and how are they different](https://learn.cantrill.io/courses/docker-fundamentals/lectures/44151196)

- Think of containers and docker containers as the same thing.
- Physical hardware -> VM host.
#### Summary
- Containers run on a container host
- ... via container (Docker) engine (<- no 's' ?)
- Containers only run an APP & Libraryies / Runtime Env
- Share the container HOST OS (run as a process on it)
- Lightweight - can be densely packed & started / restarted quickly
- Can be impacted by other containers (noisy neighbours)

- "It works on my computer" => "Ok let's ship your computer"

### [[DEMO] installing Docker on your local machine](https://learn.cantrill.io/courses/docker-fundamentals/lectures/44151197)

- desktop app
  - command line
  - GUI
- `docker`
- `docker version`

## [DOCKER 101 (Architecture and Commands)](https://learn.cantrill.io/courses/docker-fundamentals/lectures/44151958)
- Docker engine
- Docker daemon -> background service, it handles the heavy lifting
- Docker client (CLI & Desktop) -> how we instruct the daemon
- Docker registry -> a library or hub
- Docker images -> snapshots of the containers
- Containers -> running instances of the images

- The client task to the daemon
  - the daemon runs the engine
    - The daemon uses images
      - the images are taken from the registry
        - the result of all this is the containers

- start with Docker host, that runs the daemon

<img width="554" height="303" alt="Screenshot 2025-08-22 at 14 16 56" src="https://github.com/user-attachments/assets/87ca561e-9fc7-4ee9-a8b2-e26a257734ef" />

### Docker Architecture
### [Interacting with Docker Engine](https://learn.cantrill.io/courses/docker-fundamentals/lectures/44706186)

`docker run hello-world`
 - ca't find it locally, so it pulls the latest version down
 - pull complete
 - runs the container using this image
`docker ps`
`docker ps -a`
`docker images`
### [Container and image architecture](https://learn.cantrill.io/courses/docker-fundamentals/lectures/44151202)

- container image is a read-only immutable template
- If you change them you are creating a new image
- creating a container from the image is like making a writable layer
- These writable layers are independent
- Writable layers use the "unon file system"
- If you ned to share data, there are ways, but that's more advanced
- Docker images:
 - a system of layers:
 - each layer only contains the differences from the layer below
  - top: application layer
  - middle: env/libs
  - bottom: base linux
 - layers can be re-used

### [Working with existing docker images](https://learn.cantrill.io/courses/docker-fundamentals/lectures/44151206)

`docker ps` -> no running containers
`docker images` -> shows the image we used earlier

```
hello there: docker images
REPOSITORY                 TAG       IMAGE ID       CREATED       SIZE
hello-world                latest    a0dfb02aac21   2 weeks ago   20.3kB
acantril/containerofcats   latest    3ffa9b0efe79   2 years ago   361MB
```
docker inspect 3ffa9b0efe79
docker run -p 8081:80 acantril/containerofcats
 - you could have done this without pulling the image, it would now pull and run the image
docker run -p 8081:80 -d acantril/containerofcats
  -this is running them in detach mode so you don;t have to keep the terminal ope
docker port 17d6066a0d84
docker exec -it 17d6066a0d84 ps -aux (doesn't work)
docker exec -it 17d6066a0d84 sh
- df -k shows siles
- exit
-cleanup:
 - docker stop 17d6066a0d84
 - docker rm 17d6066a0d84
### [Dockerfile syntax](https://learn.cantrill.io/courses/docker-fundamentals/lectures/44660838)
- the theory of docker files
 - comments start with #
- FROM
- LABEL
- RUN
- COPY
- ADD
- CMD
- ENTRYPOINT
- EXPOSE
### [Build and run a simple containerised application](https://learn.cantrill.io/courses/docker-fundamentals/lectures/44660840)

## MORE DOCKER
### [Containable storage](https://learn.cantrill.io/courses/docker-fundamentals/lectures/44151338)
#### Writable layer
- 1st type available -> the writeable layer
 - like watercolour layers, but only the top layer is changeable.
#### Tmpfs
- tmpfs -> fast in memory storage, but not persistent, and cant be shared between containers
 - use for sensitive storage, for the short term
#### bind mount
- [02:52]
- 2nd type : bind-mount
 - the data is on your machine, but can be accessed by multiple containers.
 - Even the folders on your machine could be network based folders, so mounted remotely
#### Volumes
- docker native
- storage accessible to a container.
- They can remain after the container stops existing

<img width="1105" height="613" alt="Screenshot 2025-08-22 at 23 52 01" src="https://github.com/user-attachments/assets/37caf3ef-adeb-44bc-996d-39afea384f19" />

### Docker container storage
- 1st type: writable layer

<img width="1110" height="617" alt="Screenshot 2025-08-22 at 23 57 57" src="https://github.com/user-attachments/assets/40d5cf7d-ad2f-42e5-9bd7-ed0b90b06ff5" />
### [Docker container networking](https://learn.cantrill.io/courses/docker-fundamentals/lectures/44151341)

- 2 modes: host networking and bridge networking

- containers on the same bridge network can share resources.
- bridges is the default way of networking containers to ports
### [[DEMO] Extending our container application using Environment Variables](https://learn.cantrill.io/courses/docker-fundamentals/lectures/44660845)

https://github.com/acantril/docker-fundamentals/blob/main/docker-container-environment-variables/instructions.md
`docker run --name phpmyadmin -d -p 8081:80 -e PMA_ARBITRARY=1 phpmyadmin/phpmyadmin`
`docker pull mariadb:10.6.4-focal`
`docker inspect mariadb:10.6.4-focal`

```
CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS                      PORTS      NAMES
b9ccd745622f   mariadb:10.6.4-focal       "docker-entrypoint.s…"   7 seconds ago    Up 6 seconds    3306/tcp   db
c11ad600da0a (2nd go)
```
- docker inspect c11ad600da0a 
` "IPAddress": "172.17.0.2",`

- bug-> the page of cat photos is still using port 8081, so I'm just going to run the phpadmin container on 8085:

```
docker stop phpmyadmin 2>/dev/null
docker rm phpmyadmin 2>/dev/null

docker run -d --name phpmyadmin \
  -p 8085:80 \
  --network bridge \
  -e PMA_HOST=db \
  phpmyadmin/phpmyadmin
```

- it's not giving me the option to input the server...
- docker run --name phpmyadmin -d -p 8085:80 -e PMA_ARBITRARY=1 phpmyadmin/phpmyadmin
 - but even though the container is stopped, it's still there, so i need to remove it:
  - `docker rm phpmyadmin vibrant_elion`, then try again:
  - docker run --name phpmyadmin -d -p 8085:80 -e PMA_ARBITRARY=1 phpmyadmin/phpmyadmin
- password: `MYSQL_ROOT_PASSWORD=somewordpress`

- Go into the container via a bash shell:
 - `docker exec -it db bash`
 - df -k
 - cd /var/lib/mysql
 - ls -la
- if we delete this container all of the data will also be deleted. This is a problem the next video will rectify.
- clear-up:
 - exit
 - docker stop db
 - docker rm db
 - docker stop phpmyadmin
 - docker rm phpmyadmin
### [Docker bind mounts & volumes](https://learn.cantrill.io/courses/docker-fundamentals/lectures/45142283)

## FINISHING UP & WHAT'S NEXT
Docker fundamentals
