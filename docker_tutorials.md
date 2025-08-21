https://www.youtube.com/watch?v=pg19Z8LL06w

### Intro
- [00:00]

### 1. What/why docker
[02:55]
- what is it? Why was it created? What problem does it solve?
- a veirtualisation software that makes deploying apps much easier than it was before
- It does this by packaging everything in a container
[03:55]
- What problem does it solve?
  - before devs had to install all the dependencies on their system.
  - All devs on the team had to instal and configure them on their environment. It would be different for different machiens
  - This involved many steps, which means the chances of something going wrong was quite high, also tedious.
- with containers:
  - you don;t have to install anything directly on your machine.
  - It's its own isolated environment
  - It will be the same commands for each container on any local dev environment.
  - With docker you can have different versions of the same app without any conflicts
- Deployment before containers was:
  - dev team creates an artifact with installation instructions.
  - They give it to the operations team, adb they handle installing and configuring everything.
  - There are many potential problems here.
    - miscommunication
- with containers:
  - devs make the package that contains everything:
    - configuration
    - app source code
    - dependencies
  - so there's less room for problems, and the ops team just have to run the docker intructions on the server.


### 2. Docker vs Virtual machines
[11:40]

- why is docker better than pre-existing virtual machines.
- [12:50] how an OS is set up
- Docker virtualises the applications layer
- Docker machines use the hosts Kernel.
- Docker images are much smaller and therefore faster

### 3. Install docker locally
### 4. Images vs containers
### 5. Public and private registries
### 6. Run containers
### 7. Create own image (Dockerfile)
### 8. Main docker commands
### 9. Image Versioning
### 10. Docker workflow big picture
