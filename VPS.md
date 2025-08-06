## [Setting up a VPS](https://3.basecamp.com/3695031/buckets/42750717/todos/8783061488)
- Virtual private server. A virtual machine sold as a service by a cloud hosting provider.
- A VPS is functionaly equivalent to a dedicated physical server (but way cheaper). eg:
  -  Digital Ocean droplets
  -  AWS EC2
  -  GCP computer Engine.
### [Hypervisors](https://www.ibm.com/think/topics/hypervisors)
- Type 1 hypervisors
- Type2 hypervisors
  - eg Oracle
- You can move hypervisors to other machiens instantly
- benefits:
  - cost savings (physical infastructure)
  - Agility/speed
  - lowers downtime (hosts unexpectedly going down).
### What are we doing with VPSs:
- Each capstone student will be setting up a  VPS and installing several different pieces of software on it . It will act as a basic architecture that can run multiple applicatuons including a dynamic one backed by a data later.
- We will be installing:
  - A webserver that can route requests to 2 different applications
  - A static site, one of our applicatuion
  - A dynamic application: outn other apoplication server that queries two different databases.
  - MongoDB, our non-relational, document database
  - PostgreSQL, our relational database:

<img width="665" height="598" alt="Screenshot 2025-07-28 at 11 49 36" src="https://github.com/user-attachments/assets/5191b973-7a22-4b52-b9ea-083023b5a3c3" />

### Why are we doing it?

- learn by doing

### How do we do it?

1. Set up the VPS
2. Buy a cheap domain
3. Set up DNS
4. Install Nginx
5. Deploy a static site
6. Install ProstgreSQL
7. Install MOngoDB
8. Deploy a dynamuc app that stores/ retrieves data from both Postgres and Mongo

### [tutorial](https://launchschool.com/gists/79b8e672)

#### Youtube tutorial:

- How to set up a virtual Private Server on Digital Ocean -> a way to host your own website on the cloud.
- Virtual Private server: a computer that someone else is managing for you (here DigitalOcean)
- [01:32] We will build a VPS which can serve a website we've build. To do this it needs a few components:
  - VPS
  - Other servers on the same machine:
    - The firewall (a bouncer for network traffic)
      - SSH is the traffic which is allowed
      - Also HTTP
      - and HTTPS
    - [02:50] A web server
    - [02:52] A reverse Proxy (NginX):
      -  once traffic has made it through the firewall this web server will route the request to the appropriate app on the machine. (a traffic cop/manager)
      -  [03:27] We'll configure this with an SSL certificate, which will encrypt trafffic to our server so we can take HTTPS as well as HTTP. We do this with 'let's encrypt'.
-  [04:08] after all of this we can run our website. We do this with a process manager called PM2. Normally we would have to manually start the process that starts the website, like with `node` or `bundle exec rake`, but if you're hosting on the cloud you don't want to have to do this. So if the app fails, PM2 will restart it for us.

<img width="823" height="464" alt="Screenshot 2025-07-29 at 08 27 35" src="https://github.com/user-attachments/assets/c9ce199d-4a0a-4e93-9170-e2f989271118" />

- [05:22] Step 1: create a VPS we can connect to through an IP address.
  - Have an account on digital Ocean.

- digital ocean passphrase 5.8.25: 'not on your nelly'
- [10:00] : Your public key has been saved in /Users/sandyboy/.ssh/id_ed25519.pub
  - Your identification has been saved in /Users/sandyboy/.ssh/id_ed25519
  - cat ~/.ssh/id_ed25519.pub
  - name: `digital-ocean-1`
  - hostname: `ubuntu-s-1vcpu-512mb-10gb-ams3-01`

IS THE BIG TAKE-AWAY FROM THIS HELLISH DEBUGGING EXPERIENCE THAT IT'S OFTEN BETTER TO GO SCORCHED EARTH?

- [13:22] next step: SECURITY
  - firewall to disable traffic except for SSH
- Create an unprivileged account without using `sudo` (the principle of least privilege).
  - ssh root@164.92.150.102
  - `yes`
  - `adduser sandy`
  - password: `bloast`
- allow user to escalate to sudo when necessary:
  - `usermod -aG sudo sandy`
- [17:00] move the public SSH key to the VPS into this unprivileged account. (from root to sandy):
  - `rsync --archive --chown=sandy:sandy ~/.ssh/home/sandy` -> FAIL
  - `rsync --archive --chown=sandy:sandy ~/.ssh/ /home/sandy/.ssh/` -> success (chatGPT)
  - To test this works:
    - disconnect with control-D
    - reconnect with ssh sandy@164.92.150.102 -> success
  - [19:10] test it works with `sudo apt-get update` -> works
- [19:30] Set up firewall
- ufw is the name of the software firewall that comes with "the machine"
- `ufw status` -> error: you need to be root to run this command
- `sudo ufw status` (sudo password: bloast)
  - status : inactive
- Step 1 enable ssh trafic:
  - `sudo ufw allow OpenSSH`
- Step 2: block everything else:
  - `sudo ufw enable`
- Step 3: disable root account (as a "good practice" precaution)
  - `sudo vim /etc/ssh/sshd_config`
    - `i` to enter editing mode
    - change `permit root login` to `no`
    - `escape` to leave editing mode.
    - exit with `:wq`
  - refresh with `sudo service ssh restart`
    - `logout`
    - try and log in with `ssh root@164.92.150.102` -> not permitted -> correct
    - log in with `ssh sandy@164.92.150.102` -> allowed -> correct
- [23:50] Awesome -> we have successfully:
  1. Turned on the firewall
  2. created an unprivileged account
  3. given that unprivileged account a way to escalate its permissions
  4. Disabled root to help further lock-down the server
- Next steps:
  1. install node (because we're going to be running an express app that was written in javascript)
     - `sudo apt update`
     - `sudo apt install nodejs`
     - `sudo apt install npm`
   2. Clone app from Github:
      - `https://github.com/SandyRodger/dummy_app.git` (clone with HTTPS)
      - in terminal: `git clone https://github.com/SandyRodger/dummy_app.git`
   3. [27:00] 
      - confirm presence of app with `ls`
      - check firewall status with `sudo ufw status`
      - permit the coresponding port to be permitted (3000):
        - `sudo ufw allow 3000`
      - Make sure you have a `package.json` file with `npm init -y`
      - install express: `npm install express`
      - rerun `npm install` to make sure express is there.
      - run app with `node 02.js`
      - re-jig dummy app so the server-side code is seperate from the code that runs in the browser.
      - update from github with `git pull origin main`
      - run with `node server.js` (not node app.js because that would be running the file in node, where it doens't make sense)
        -  but in the instructions he DOES use `node app.js` and it works, so I've done something slightly different here.
  -  [30:15] pause for today
      - `http://164.92.150.102:3000/` works
  - [31:00] Ido (the narrator) demonstrates that if you shut down the app (with control +C) then it is no longer accessible in the browser. But my app is accessible. Presumably because I am running the server on the digital ocean droplet, not running that one file. I'm a little unclear on this, but I'll keep going.
- [31:15] close off the firewall in order to perform a test:
  - `sudo ufw delete allow 3000`
  - confirm it's been deleted with `sudo ufw status`
4. [32:10] Give it a domain name:
  - `bloast.nl` with squarespace
  - squarespace domain
    - [33:35] DNS "where it should point traffic that's trying to hit bloast.nl`
      - "the way that you do that is through these what are called 'A-records'
      - custom records (not the same on the video because he's using google where I'm using squarespace.
      - 'we were unable to save this record. if the problem persists please contact customer support'.
      - and thw `www` doesn't work for a different reason: "This host is already in use by a CNAME record."
      - So I deleted the squarespace defaults and it fixed both problems (hooray)

