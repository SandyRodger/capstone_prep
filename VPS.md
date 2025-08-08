# [Setting up a VPS](https://3.basecamp.com/3695031/buckets/42750717/todos/8783061488)
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

### Youtube tutorial:

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
### clone app from Github
   2. [25:20] Clone app from Github:
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
- [32:10] Give it a domain name:
  - `bloast.nl` with squarespace
  - squarespace domain
    - [33:35] DNS "where it should point traffic that's trying to hit bloast.nl`
      - "the way that you do that is through these what are called 'A-records'
      - custom records (not the same on the video because he's using google where I'm using squarespace.
      - 'we were unable to save this record. if the problem persists please contact customer support'.
      - and thw `www` doesn't work for a different reason: "This host is already in use by a CNAME record."
      - So I deleted the squarespace defaults and it fixed both problems (hooray)
- test if domain is live:
  - `exit` to exit shell terminal
  - `ssh sandy@bloast.nl`
  - enter passphrase ('not on your nelly')
4. [37:10] Set up NGINX
  - update repository to make sure everything's up to date: `sudo apt update`
  - install nginx: `sudo apt install nginx`
    - nginx is going to serve as the web-server and a reverse proxy, so it will route requests on to where they need to go.
    - nginx is a default web-seerver/ reverse proxy for the internet -> super production ready, supported by Apache.
  -  enable traffic to interact with nginx from the internet
  -  `sudo ufw app list`:
```
Available applications:
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
  Nginx QUIC
  OpenSSH
```
  -  [39:50] `sudo ufw allow 'Nginx HTTP'`
  -  check with `sudo ufw status`
  -  `systemctl status nginx` (ctl-c out)
-  [41:40] `sudo vim /etc/nginx/sites-available/default`
  -  change `server_name _;` to `server_name bloast.nl www.bloast.nl`
  -  [42:45] test your config file while making changes:
    -  `sudo nginx -t` - success message.
    - `sudo systemctl reload nginx`
     - test by going to `www.bloast.nl` -> works
   - [44:25] `sudo vim /etc/nginx/sites-available/default` again
     - "We're gonna want to tell nginx to route requests to our app" =>
     - copy some quick config information here:
     - replace location block ith information about out app
     - I don't know where he's pasting this info in from, but I'm going to have to type it out:
```
location / {
  proxy_pass http://localhost:3000;
  proxy_http_version 1.1;
  proxy_set_header Upgrade $http_upgrade;
  proxy_set_header Connection 'upgrade';
  proxy_set_header Host $host;
  proxy_cache_bypass $http_upgrade;
}
```
- confirm that config file is ok : `sudo nginx -t` => success
- `sudo systemctl reload nginx`
- OK here I have a bug caused by the fact that my dummy app is doing something quite different to his. So I'm going to copy his app exactly in order to get around this issue.
- Current state of project files:
- tree
```
hello there: tree
.
├── package.json
├── public
│   ├── index.html
│   └── script.js
└── server.js

2 directories, 4 files
```
- server.js:
```
const express = require('express');
const app = express();
const port = 3000;

app.use(express.static('public'));

app.listen(port, () => console.log('Running your bastard app'));
```
- index.html:
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>sandy's app</title>
    <script type="module" src="./script.js"></script>
  </head>
  <body>
    <button>Click me</button>
  </body>
</html>

```
- script.js:
```
document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('button').addEventListener('click', () => {
    alert('you are a sexy man');
  });
});
```
- [47:00] -> running the app
- [47:40] -> next step: set up PM2 : process manager
  - `sudo npm install pm2@latest -g`
  - `pm2 start server.js`
- Tell pm2 to start up whenever system d starts up
- (system D is like the process manager for linux).
- `pm2 startup systemd`
  - returns : `sudo env PATH=$PATH:/usr/bin /usr/local/lib/node_modules/pm2/bin/pm2 startup systemd -u sandy --hp /home/sandy`
  - copy and paste that in the command line.
  - save changes with `pm2 save`
  - [51:00] `sudo reboot`
  - get back in with `ssh sandy@bloast.nl`
  - [52:00] get outselves an SSL certificate to secure our website and hit it with https.
  - use letsencrypt and certbot:
    - `sudo add-apt-repository ppa:certbot/certbot`
  - hmmm, there's no delay for me.
  - This part is deprecated. Follow these: https://certbot.eff.org/instructions?ws=nginx&os=osx
*********************************** HERE'S WHERE IT'S ALL GOING WRONG *********************************************
    - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
      - This homebrew install is failing.  ->:
        - ChatGPT soultution: create swap memory:
    ```
      sudo fallocate -l 1G /swapfile
      sudo chmod 600 /swapfile
      sudo mkswap /swapfile
      sudo swapon /swapfile
      echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
    ```
- then `free -h` to check it worked.
- then make sure the command is available:
```
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```
- and manually finish the install:
  - `brew update --force --quiet`
- and make sure it's running:
  - `brew doctor`
### Certbot
    - `brew install certbot`
    - `sudo certbot certonly --standalone`
  - BUG: I can't install the certificate:
    - Maybe it's trying to find the app on port 80 rather than port 3000 -> no, it must use port 80
      - stop running server on pm2: `pm2 stop server`
      - `sudo certbot certonly --standalone -d bloast.nl`
    - try and fix by using standalone mode:
      - stop anything on port 80:
        - `sudo systemctl stop nginx`
        - `sudo systemctl stop apache2`
        - `sudo lsof -i :80  # should show nothing`
       
        - Aha maybe the problem is i was trying to certify the domain name, not nginx?:
          -  `sudo certbot --nginx -d bloast.nl -d www.bloast.nl`
          -  ask for email address ->
          -  terms of service -> agree
    -  `sudo certbot renew --dry-run`
   

- ok certbot is installed now, but does not have access to teh `certbot` command from `sudo`, so I need to explicitly run `sudo` with the correct path:
  - `sudo env PATH=$PATH certbot --nginx -d bloast.nl -d www.bloast.nl` AND IT WORKED!

    -  [57:00] Conclusions, we have:
      -  a VPS we can connect to via a domain name using HTTPS, securely, using NGINX as a webserver to route requests to our Express app which is being run as a service by pm2.

### DNS records:
- video: https://d30l2an5huagqb.cloudfront.net/system-design/dns_records_explanation.mp4
- How they work, how they're stored and how they resolve into an IP address
- [00:40] let's start with google.
  - we redister a domain name with google and it now hosts our domain name, it points to an IP address
  - how is 'alberdorfman.de' resolved to the IP address
  - There is a "resolver" which seeks the address.
  - There's a top-level domain name server, which leases the domains to businesses.
- [03:56] The top level registrar ...

### Install PostgreSQL

- `https://www.postgresql.org/download/linux/ubuntu/`
- intall with: `apt install postgresql`


### Install MongoDB

- mongoDB: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/
- What version of UBUNTU is running? `cat /etc/lsb-release` :

```
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=25.04
DISTRIB_CODENAME=plucky
DISTRIB_DESCRIPTION="Ubuntu 25.04"
```

1. Import public key: 
- install `gnpug` and `curl`:
  - `sudo apt-get install gnupg curl`
- Import mongoDB pupblic GPG key:
  -`curl -fsSL https://www.mongodb.org/static/pgp/server-8.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg \
   --dearmor`
2. Create lsit file:
  - `echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list`
3. reload package database: `sudo apt-get update`
4. Install mongoDB community server: `sudo apt-get install -y mongodb-org`

##### Run MongoDB:
- `sudo systemctl start mongod`
- verify it's started: `sudo systemctl status mongod`
- stop mongoDB with this command: `sudo systemctl stop mongod`
- restart with this: `sudo systemctl restart mongod`
- Begin using MongoDB with this: `mongosh`.


### Depoly a dynamic app

- RB185 todolist app
- `git clone https://github.com/SandyRodger/RB185-RB189.git`
`sudo apt update
sudo apt install libpq-dev`
`bundle install`
- BUG -> conflict of using 2 different ruby versions:
  - `sudo snap remove ruby`
  - `export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"`
- Rbenv not installed, install rbenv:
  - `sudo apt update
      sudo apt install -y git curl build-essential libssl-dev libreadline-dev zlib1g-dev`
  - `git clone https://github.com/rbenv/rbenv.git ~/.rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(~/.rbenv/bin/rbenv init -)"' >> ~/.bashrc
source ~/.bashrc
 Now install ruby-build as a plugin
mkdir -p "$(rbenv root)"/plugins
git clone https://github.com/rbenv/ruby-build.git "$(rbenv root)"/plugins/ruby-build`
- `rbenv install 3.2.2
rbenv global 3.2.2
rbenv rehash
`
- run out of space: `/tmp` is 100% full:
  - `sudo rm -rf /tmp/*` -> empties tmp
  - `df -h /tmp` -> check it's empty
  - `rbenv install 3.2.2` -> try again
 
- still no enough space, so setup another directory to hosue it:
```
mkdir -p ~/tmp
export TMPDIR=~/tmp
```
- try again
  - `rbenv install 3.2.2` -> nailed it
  - `bundle exec ruby todo.rb`

#### make sure it's being run by pm2:
  - nano ecosystem.config.js
```
module.exports = {
  apps: [{
    name: "sinatra-todo-app",
    script: "todo.rb",
    interpreter: "bundle",
    args: "exec ruby",
    cwd: "/home/sandy/RB185-RB189/03_todo_app",
    env: {
      RACK_ENV: "production"
    }
  }]
};
```
  - pm2 start ecosystem.config.js

### hmmmm nothing is running on the browsers now. Ill concentrate on getting bloast.nl back up
