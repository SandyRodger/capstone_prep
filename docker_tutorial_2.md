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


### Container and image architecture
### Working with existing docker images
### Dockerfile syntax
### Build and run a simple containerised application
## MORE DOCKER
## FINISHING UP & WHAT'S NEXT
Docker fundamentals
