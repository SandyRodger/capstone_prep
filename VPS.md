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
