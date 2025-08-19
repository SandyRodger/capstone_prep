# [AWS Certified Solutions Architect Associate 2025](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/?couponCode=MT130825B)
### Section 1 - introduction - AWS certified solutions architec associate

- preparing for the SAA-CO3 exam
- course is 25 hours in total
- cover 30 other AWS services.

#### What's AWS
  - AWS is a cloud provider.
  - They provide you with servers and servicese that you can use on demand and scale easily.
  - AWS has revolutionised IT over time
  - AWS powers some of the biggest websites in the world:
    - Netflix
    - Amazon.com
- it's  a spaghetti of inter-connected services.
#### [Creating an AWS account](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/13541138#content)

- email: longlungs@atomicmail.io
- ShampooCrank6%
#### [important tip](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/13541136#content):

- speed up or slow down the speech.
- subtitles and transcripts are available.

### Section 3 - Getting started with AWS
(video 8)
- launched in 2002 because they had great IT, so they offered their service to others.
- Leading the Gartner Magic Quadrant (?)
- It's super ubiquitous.
- Enables you to build:
  - sophisticated and scalable apps.
  - anything -> backend, front end, streaming whatever.
- Global infrastructure...
- They used to have a global map showing this.
#### AWS regions
- Where should you launch your app, which AWS region?
  - think about compliance -> does the data have to stay in the country?
  - Latency -> are the users in America, then deploy there.
  - Not all regions have all services.
  - Pricing
#### AWS availability zones
- Each region has many availablity zones. (AZ)
- Each AZ has discrete data centres so they're isolated in case of disaster.
- Connected with high-bandwidth, low latency cables.
#### AWS points of presence (Edge locations)
#### Tours of the AWS console
  - AWS has global services
  - Most AWS services are Region-scoped.
  - There's a table to see if services are available where you are.
### [Section 4 - IAM & AWS CLI](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26097996#content)
- Identity and Acess Management.
- Root accounts
- Create Users
- For example if there are 6 people in your organisation...
  - 'operations' group
  - 'users' group
- users can begin to mutiple groups
- you can't have sub-groups
##### IAM permissions
##### 12. IAM users & groups
- In the search bar type 'iam' -> go to iam dashboard
  - 'users' on left hand side.
  - It's a global service, so not region specific.
- Create a user : 'Sandy`
  - 'Provide user access to the AWS management console`
  - I want to create IAM user
  - EatACake555!
  - Create a group 'admin'
    - tick first option -> 'administrator access'
  - Add the user into the admin group:
    - click next
    - key: 'Department', value: 'engineering'
    - Create user (bottom right)
    - Return to user list
  - Go to 'User' groups in left hand side: admins
- at this point the 'sandy' user has his permissions granted via the admin.
-  create alias... to simplify your sign in url = `wongawonga`
-  SIgn in with a private-mode browser (because if it's not private, it logs out the 1st one)
-  Root account logged in on one window, IAM logged in on the other one...
-  For the course use IAM user rather than Root. 
##### [13. AWS Console Simultaneous Sign-in](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/51960287#lecture-article)

- Turn on multi-session support
- I can add a session and sign into a different identity

### Section 5 - EC2 fundamentals
#### [31 AWS budget set-up](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098410#content)

- must be root user.
- account
- activate IAM user access
- set up minimum spend budget

#### [32 EC2 (creating our first website)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098112#content)

- one of the most popular services
- rent machines: 'EC2 intances'
- Sizing and Configuration.
- We ca "bootstrap tehm"
  that means launching commands when the machine starts and never again.
  - install softrware
  - updates
- t2.micro -> running a prgram free for a month.
  - create a key-pair... 
  - 
#### [33 - running your first EC2 instance running Linux](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098122#content)
- I'm not going to implement this, and I'm not going to rememeber all the steps, so I'll skipp for now and come back.
#### [34 EC2 Instances Types - Overview](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098128#content)
- 7 types
- There's a specific website on AWS website looking into this
- m5.2xlarge is the AWS naming convention
  -  m: instance class
  -  5: generation:
  -  2xlarge: size within the class
- compute optimized instance types
- EC2 instance types -> general purpose:
  - Good balance of Compute, Memory & [...]
- High performance types for example (6 examples) (all `c` class)
  - gaming
  - media transcoding
- Memory Optimized types: 'r' and 'x1'or 'z1'
- Storage optimised:
  - 5 technical sounding examples
#### [35 Security Groups and classic ports overview](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098134#content)

- Create a security group around our EC2 instance
- Regulate:
  - access to ports
  - authorised IP ranges
  - Control of inbound network
  - Control of outbound network
- security Groups and instance groups have M:M relationship
- Lives outside the ECC2 instance
- tip: it's good to maintain one security group for SSH access
- how to reference security groups from other security groups
- classic ports to know:
  - SSH -> port 22 -> log into a Linux instance
  - FTP -> 21
  - SFTP -> 22 (upload files with ssh)
  - HTTP -> 80 (unsecured websites)
  - HTTP3 -> 443
  - 3389 -> RDP (remote Desktop protocol) -> log into a Window instance
#### [36 security groups hands-on](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098138#content)

- edit inbound rules
- https://498548864480-ys4alzrs.eu-north-1.console.aws.amazon.com/ec2/home?region=eu-north-1#SecurityGroups:

#### [37 SSH overview](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098142#content)

- how do you connect inside of your servers to perform some maintenance or action.
- Different for different machines:
  - Mac
  - Linux
  - Windows < 10
  - Windows > 10
- SSH, Putty and EC2 instance Connect.
- SSH is the thing that casues the most trouble in this course (There's a trouble shooting guide and other resources)
#### [38 How to SSH using Linux or Mac](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/13528044#content)

- SSH allows you to control a remote server/machine from your own terminal. Your command line then acts as though it is in that machine.
- downloaded file 'EC2tutorial.pem' ?
- `ssh ec2-user@[IP adress]`
- `chmod 0400 [filename]`

#### [39 How to use SSH using windows](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/13528046#content)
- skip
#### 40
- skip
#### [41 Trouble shooting page](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/16666654#content)
#### [42 EC2 instance connect](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098164#content)
- alternative to SSH, much easier
- a browser based SSH session into our EC2 Instance. No need to use SSH keys
#### [43 EC2 Instance roles demo](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098166#content)
- as a rule of thumb never enter your [...] into an EC2 instance because then it can be read by any other user in that group.
- None of this is going in to my brain.
#### [44 EC2 instance purchasing options](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098170#content)
- save money by having different deals for different work-loads
- Types:
  - On demand Instances
  - Reserved
  - Saving plans
  - Spot instances
  - dedicated hosts
  - dedicated instances
- EC2 on demand: billing per second
  - highest cost, but no upfront payment
- skip for now
#### [45 Spot instances & Spot fleet](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/18756818#content)
- large discount available
- price fluctuates, the user-defined max-price is relevant.
- How to terminate Spot instances?
  - persistent mode
- You can only cancel Spot instances that are open, active or disabled.
- Spot fleets (the ultimate way to save money)
  - a set of Spot Instances which tries to meet your traget capacity with price constraints
  - Strategies:
    - lowestPrice: launch instances from the pool that has the lowest price.
    - diversified
    - capacityOptimized
    - priceCapacityOptimised
#### [46 EC2 instances Launch types hands-on](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/27694918#content)

- 'create spot fleet requests'
- Alternatively -> launch instance -> advanced details
- ... capacity reservations

### Section 6 - EC2 solutions Architect Associate Level

#### [47 Private v public v elastic IP](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/13528052#lecture-article)

- in this course we use IPv4
- public IP means the machine can be found on the internet
- private IP -> the machine can only be identified on the private network
- private network amchines only access the internes through a proxy (NAT device?)
- elastic IP is
  - limited to 5 on your account
  - avoid using them
  - instead use a random public IP and regiser a DNS name to it
  - or use a load balancer
- if your machine is stpped and started the public IP can change
#### 48 Private vs Public vs Elastic IP Hands On
- stop instance
- copy and paste IP address
- start instance (different from rebooting instance)
- new IPv4. So you can't ssh into the old ip
- We need to solve this problem, because sometimes we want the ip not to change
- We use a elastic IP address.
- These cost a little more. There are instructions for avoiding charges.
- actions -> associate IP address
  - instance
  - private IP address
#### [49 EC2 Placement Groups](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/13528080#content)

- cluster placement groups
- placement groups spread
- placement group partitions

#### [50 EC2 Placement Groups - hands on](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26118770#content)

- create placement group
  - placement strategy (4)
  - launch instance
  - advanced details -> setting -> 

#### [51 Elastic Network Interfaces (ENI)](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/18077955#content)

- overview

#### [52 ENI hands on](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26118774#content)

#### [53 ENI extra reading](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/20680996#content)

#### [54 EC2 hibernate](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/18104377#content)
- whatever was in ram will be preserved.
- supports many instance families
#### 55 [EC2 hibernate hands on](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/18105183#content)
- `uptime`
- hibernate instance
### Section 7 - EC2 Instance Storage
#### [56 EBS volumes](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098272#content)

- Elastic block store
- like a usb stick/network drive, but not a physical one
- delete on dermination attribute
#### [57 EBS hands on](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098274#content)


#### [58 EBS snapshots](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098276#content)

#### 59
#### 60
#### [61 AMI hands on](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098284#content)
#### [62 EC2 instance store](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098288#content)
- even higher performance -> a hardware disk attached to your machine
- ephemeral storage
- local EC2 instance store ->  high IOPS 
#### [63 EBS volume types](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098296#content)
- IOPS (I/O per second)
#### [64 EBS multi attach](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26098298#content)



#### 65 EBS encryption

- how to encrypt an EBS volume?

#### 66 Amazon EFS
#### 67 Amazon EFS hands on
#### 68 EFS vs EBS
#### 69 EBS & EFS
### Section 8 - High availablity and scalability: ELB & ASG
#### 70 High availability & scalability
#### 71 Elastic Load balancing (ELB) overview
#### 72 Note: about the classic load balancer (CLB)
#### 73 Application Load balancer (ALB) 
#### 74 Application Load balancer (ALB) hands on - pt 1
#### 75 Application Load balancer (ALB) hands on part 2
#### 76 Network Load balancer (NLB)
#### 77 Network Load balancer (NLB) hands on
#### 78 Gateway Load balancer (GWLB)
#### 79 Elastic Load balancer - sticky sessions
#### 80 Elastic Load balancer - cross zone load balancing
#### 81 Elastic Load balancer - SSL certificates
#### 82 Elastic load balancer - SSL certificates - Hands on
#### 83 Elastic Load balancer - connection draining
#### 84 Auto scaling groups - Hands on
#### 85 Auto scaling Group Hands on
#### 86 Auto scaling Groups - scaling policies
#### 87 Auto scaling Groups - scaling policies Hands on 
### Section 9 - AWS Fundamentals: RDS + Aurora + ElastiCache
#### 88 Amazon RDS Overview
#### 89 RDS Read Replicas vs multi AZ
#### 90 Amazon RDS Hands On
#### 91 RDS custom for Oracle and Microsoft SQL server
#### 92 Amazon Aurora 
#### 93 Amazon Aurora - hands on
#### 94 Amazon Aurora - Advanced Concepts
#### 95 RDS & Aurora - Backup and Monitoring
#### 96 RDS Security
#### 97 RDS Proxy
#### 98 Elasticache Overview
#### 99 Elasticache hands on
#### 100 Elasticache for solution architects
#### 101 List of Ports to be familiar with
### Section 12 - Aamazon S3 Introduction
#### 129 S3 Overview
#### 130 S3 Hands on
#### 131 S3 Security Bucket Policy
#### 132 S3 Security: Bucket Policy Hands on
#### 133 S3 Website Overview
#### 134 S3 Website Hands On
#### 135 S3 Versioning
#### 136 S3 Versioning - hands on
#### 137 S3 Replication
#### 138 S3 Replication Notes
#### 139 S3 Replication Hands on
#### 140 S3 Storage Classes Overview
#### 141 S3 storage Classes hands on
#### 142 S3 Express One Zone
### Section 15 - Cloudfront & AWS Global Accelerator
#### 166 Cloudfront Overview
#### 167 CloudFront with S3 - Hands On
#### 168 CloudFront - ALB/EC2 as an Origin
#### 169 Cloudfront - Geo Restriction
#### 170 Cloudfront - Price Classes
#### 171 CloudFront - Cache Invalidation
#### 172 AWS Global Accelerator - overview
#### 173 AWS Global Accelerator Hands on
### Section 17 - Decoupling applications: SQS, SNS, Kinesis, Active MQ
#### 184 Introduction to messaging
#### 185 Amazon SQS - standard queues overview
#### 186 SQS - standard queue hands on
#### 187 SQS - Message Visibility Timeout
#### 188 SQS - long polling
#### 189 SQS - FIFO Queues
#### 190 SQS + autoscaling group
#### 191 Amazon simple Notification Service (AWS SNS)
#### 192 SNS and SQS - fan out pattern
#### 193 SNS -hands on
#### 194 Amazon Kinesis Data streams
#### 195 Amazon Kinesis Data streams - hands on
#### 196 Amazon Data Firehose
#### 197 Amazon Data Firehose - hands on 
#### 198 SQS vs SNS vs kinesis
#### 199 Amazon MQ
### Section 19 - Serverless Overview from a Solution Architecture Perspective
#### 214 About the serverless section
#### 215 Serverless introduction
#### 216 Lambda Overview
#### 217 Lambda Hands-on
#### 218 Lambda limits
#### 219 Lambda Concurrency
#### 220 Lambda Concurrency - hands on
#### 221 Lambda snap-start
#### 222 Lambda@Edge & cloudfront function
#### 223 Lambda in VPC
#### 224 RDS - invoking Lambda & Event Notifications
#### 225 Amazon DynamoDB
#### 226 Amazon DynamoDB - hands on
#### 227 Amazon DynamoDB - Advanced features
#### 228 API Gateway Overview
#### 229 API Gateway Basics Hands-on
#### 230 Step Functions
#### 231 Amazon Cognito Overview
### Section 21: Databases in AWS
#### 236 Choosing the right database
#### 237 RDS
#### 238 Aurora
#### 239 Elasticache
#### 240 DynamoDB
#### 241 S3
#### 242 DocumentDB
#### 243 Neptune
#### 244 Keyspaces(for Apache Cassandra)
#### 245 Timestream
### Section 24: AWS Monitoring & Audit: CloudWatch, CloudTrail & Config
#### 270 AWS monitoring - section introduction
#### 271 CloudWatch metrics
#### 272 CloudWacth Logs
#### 273 CloudWatch Logs - hands on
#### 274 CloudWatch Logs - live tail - hands on
#### 275 CloudWatch Agent & Cloudwatch Logs Agent
#### 276 Cloudwatch Alarms
#### 277 Cloudwatch alarms Hands on
#### 278 Event bridge Overview(formerly Cloudwatch Events)
#### 279 Amazon EventBridge - hands on
#### 280 CLoudWatch Insights and Operational Visibility
#### 281 CloudTrail Overview
#### 282 CloudTrail Hands on
#### 283 CloudTrail - Event Bridge Intergration
#### 284 AWS Config - Overview
#### 285 AWS Config - hands on
#### 286 cloudtrail vs CloudWatch vs Config
### Section 26: AWS Security & Encryption: KMS, SSM Parameter Store, SHield, WAF
( only watch videos 304 and 307)
#### 304 SSM Parameter Store overview
#### 307 AWS Secrets Manager - Hands on
### Section 27 Networking - VPC
#### 317 Section Introduction
#### 318 CIDR, Private vs Public IP
#### 319 Default VPC Overview
#### 320 VPC overview
#### 321 VPC Hands on
#### 322 Subnet Overview
#### 323 Subnet Hands on
#### 324 Internet Gateways & Route Tables
#### 325 Internet Gateways & Route Tables Hands on
#### 326 Bastion Hosts
#### 327 Bastion Hosts Hands on
#### 328 NAT instances
#### 329 NAT instances Hands on
#### 330 NAT gateways
#### 331 NAT Gateways hands on
#### 332 NACL & security groups
#### 333 NACL & security Groups Hands on
#### 334 VPC peering
#### 335 VPC peering hands on
(skip videos from 335 until the end)
