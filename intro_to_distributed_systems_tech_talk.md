# Intro to distributed systems - Julius Zerwick
## Intro
- [01:10] - goals
- [02:00] Why should you learn about distributed systems:
  - High chance you'll have to work with them
  - common interview question
  - Lots of room for innovation
- [03:00] Wht is a distributed system?
  - It's the reality of what the request response cycle looks like. There are all these different compontnents

<img width="1105" height="625" alt="Screenshot 2025-08-20 at 08 20 00" src="https://github.com/user-attachments/assets/72d0d308-db96-4674-9f16-ca4ab8189a3e" />

 - [05:00] The terms to know
   - Consistency -> you always get the most recent data from the system when you request it.
   - Availability -> you can always access the system, even if the data you get back is not the most up-to-date
   - Partition Tolerance -> The system can operate even when separated by the network
 - [06:00] When an entire machine is found on one machine/location.
 - [07:00] Benefits of a monolith
   - easy to start with.maintain
   - well suited to small applications
   - consisten + available
   - Eveything located in one place
 - [08:00] What happens as you grow?
   - If your app gets very popular you need : **vertical scaling** = build a bigger machine.
     - more RAM
     - Bigger CPUs
     - More disk space
   - It works for a while, but with diminshing returns and growing costs
## high level overview of distributed systems
 - [09:20] Going up versus going wide
 - **Horizontal scaling** -> buying serveral machines and have them communicate with each other.
 - This is what distributed systems is about: spreading everything out over many machines
 - [10:20] What if your machine burns down?
   - In monoliths eveything can be tightly bound so if one thing breaks you have to take everything down.
 - [11:41] Distributed systems to the rescue
   - You can spread everything out
   - You can also **duplicate components** so if one thing fails another part can come in.
   - **replicate your data**
 - [13:30] More benefits of distributed systems
   - cheaper (past a certain point)
   - allows you to have a modular system
   - You can decouple your services
## trade offs  compared to monolithic systems
- [14:00] The catch : Now we have a network partition
  - you can't control the network, once you send info over the network it's out of your hands.
  - You can only have 2 of these three : consistency, availability, partition tolerance
  - [16:00] For example -> facebook user tries to update a status.
    - 'Sorry, I don't have that data yet' = consistent
    - 'Here, this is what we have right now, but we're not sure if it's true' = available
  - [17:30] Amazon is available, banks are consistent
    - Amazon: 'give me the site now!'
    - Banks: 'You'll see it when it's accurate'

<img width="1074" height="627" alt="Screenshot 2025-08-20 at 08 42 44" src="https://github.com/user-attachments/assets/e3da8eee-2f47-43a3-9ece-232f8474b121" />

- [19:30] there are issues with distributed systems:
  - It takes a lot of forthought and focus on architecture.
  - Have to figure out how to pass data correctly between each component and whetehr you need to pass data correctly between each component.
  - Unreliable networks -> something out of your control
  - With replicated databases, it can be hard to handle te correct data everywhere
  - Can be difficult to debug issues when you need to consider how components work together and data is passed between each one.
  - More opportunities for bottlenecks & single points of failure.

## Discuss several common components of distributed systems

### Web/Proxyserver
- [22:00] Web/Proxy server
  - The gateway to the distributed system.
  - HTTP handling
  - Takes in client requests to the proper backend component
  - returns the response to the client
  - Solves the problem of "I have this request, which backend piece do I send it to?"
### Databases

- [22:46] databases
  - How do we store our data over time?
  - There are many different types of databases, and some distributed systems can use several types at once!
  - Each type has specific use cases with various nuances
  - Generally we divide them into SQL databases (PostGres, MySQL, SQLite) and NoSQL databases (Document, Graph, Key-Value, etc.)
  - SQL dbs allow you to easily analyse and slice +dice your data, but don;t easlity scale horizontally
  - NoSQL dbs do easliy scale horizontally, but are not great for analytics.
  - For a deeper dive, check out 'All things distributed' blog (by the CTO of Amazon)
- [24:30] Replicated databases
  - We can horizontally scale our databases as well!
  - By having several copies of our databases that all store our data, we can have redundancy in case one of our databases burns down.
  - We can also designate databases to be read-only or write only.
    - this is helpful in case our system has more users reading the data than writing
    - 'reads v writes'
    - eg. Twitter, Facebook
- [26:10] Same Data everywhere, right?
<img width="1092" height="641" alt="Screenshot 2025-08-20 at 09 08 22" src="https://github.com/user-attachments/assets/1c52c91b-c37c-433e-b1cf-398b246c9603" />

- Something is updated in one database, but then the request fails and the other databases don't have the update. This is a common issue, which means the databases have different data.

### Cache 

- [27:00]
- In-memory data store
  - redis
  - memcached
- Used to store data that is most frequently requested.
- Takes load off the databases
- Can be palced in many different areas of a system

  <img width="1099" height="623" alt="Screenshot 2025-08-20 at 09 15 22" src="https://github.com/user-attachments/assets/418eb1a4-1be4-4375-9c8f-730e42bb371e" />

- Solves the problem of "How do I speed up the client requests for certain data?"
- Cache invalidation is HARD:
  - There's only 2 problems in software engineering: naming variables and cache invalidation.
- When Cache gets full, you have to figure out which data to remove to free up space.
  - Least recently used is most popular.
- As with all components there are unique pros and cons that come with using them.

### Load Balancer

- [30:25]
- Software or hardware that distributes requests evenly across other components
- Evenly distributes incoming requests across machines, most often servers or databases.
- Can be places in multiple ares of a system depending on where you need it.
- Solves the problemof "How do I make sure that none of my machines receive more requests than they can handle?"

### Queue

- [31:40]
- Takes requests and holds them until they can be processed
- Requests are taken off the queue based on when they were entered
  - FIFO
- Solves the problem of "How do I manage requests when my servers are too busy?"
- Best used for asynchronous requests - users send the request off and told "Your request has been received"

### Topics I didn't touch on...

- consensus on data among replicated databases
- Various forms of database replication
  - single-leader
  - multi-leader
  - leaderless
- sharding your data across databases
  - "Instead of giving the same data to all my DBs, I will put different data on different DBs"
- Transactions
- Eventual consistency
- Two phase commits
- Microservices => a particular architectural style for building distributed systems

### references
- [35:00]]
### Q: How do you go about setting up a Distributed system?
- depends on your system.
- What kind of trade-offs do you choose?
- Monolith?
- What are the problems you face?
  - too many user requests? => load balancer
  - What are users requesting? If it's the same type of data add a cache.
  - article: "you are not google" ; don't try and do everything Google does.
- Start with a  web proxy server and a data-base and then go out from there.
### [39:00] Question: Network outages
- someone could trip on a wire
### [39:40] Question: DDos attack prevention
- Hackers overwhelm your system with more requests than they can handle.
- He can't answer it.
