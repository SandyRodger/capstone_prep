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
- [16:00] Hypervisor layer...

### 3. Install docker locally

[17:20]
- go to their website and follow the steps

### 4. Images vs containers

[21:38] -images versus containers
- Images:
  - can be easily shared or removed
  - an executable application artifact
  - add evironement variables, create directories
#### Docker Registries
- [26:57]
- dockerhub
- image versioning [29:50]
  - 'latest' is the default
- pull an image [31:00]
  - `docker pull nginx:1.23`
  - `docker run nginx:1.23`
  - `docker ps`

#### [39:00] Port binding

- container port versus host binding.
[43:00] - standard to use the same port on your local machine that is on the other thing.
- docker run creates a new container every time.
- you can use the container name as a command instead of the ID.
  - `docker stop 0384802320`
  - `docker stop fervent_bardeem`

### 5. Public and private registries
[46:00]
- docker hub is public image registary
- Compoanies create private images of their apps
- Almost all cloud providers have docker registaries.
#### repository
[48:25]

### 6. Run containers
[49:10]
```Dockerfile
FROM node:19-alpine

COPY [ackage.json /app/
COPY src /pp/

WORKDIR /app

RUN npm install
CMD ["node, "server.js"]
```
### 7. Create own image (Dockerfile)
[58:30] 

- `docker build -t node-app:1.0 .`
- `node run -d -p node-app:1.0`
### 8. Main docker commands
### 9. Image Versioning
### 10. Docker workflow big picture\
[01:03:00]
- example developing a JS app, using a mongo DB database.

<img width="797" height="437" alt="Screenshot 2025-08-21 at 22 59 20" src="https://github.com/user-attachments/assets/3e18c1e5-5873-4644-be89-0611a2001182" />
