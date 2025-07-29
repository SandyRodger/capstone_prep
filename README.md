# capstone_prep

## [Python book](https://github.com/SandyRodger/launch_school_books/blob/main/python.md)
## [Full stack open course](https://github.com/SandyRodger/capstone_prep/blob/main/fullStack_open_course.md)
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


###  black box effect:

- process with an input and an output. The black box is in the middle
- THe input is your time and effort and the output is your competence and knowledge.
- If you don't undestrand how the input feeds into the output your performance will fluctuate.
- If the results aren't coming you will increase the effort and that can lead to burn out and frustration.
- You need to understand what's happening in the black box.
- The faster/sooner you  open the black box, the faster you'll learn.
- Rule 1: do not practice in isolation
  - practice does not make perfect.
  - practice sessions should be paired with reflection on how the practice went.
  - Take this further by documenting your practice.
  - Be very clear about what the gaps in your practice are.
- Rule 2: Shift from random to targeted practice.
  - We assume a practice will lead to a certain outcome, but if it's not coming out as you expected, then this is random practice.
  - Whenever you practice have a clear intention.
- Rule 3: Ask why constantly.
