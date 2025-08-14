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
#### 34 EC2 Instances Types - Overview
- m5.2xlarge is the AWS naming convention
- compute optimized instance types
#### 35
#### 36
#### 37
#### 38
#### 39
#### 40
#### 41
#### 42
#### 43
#### 44
#### 45
#### 46
### Section 6 - EC2 solutions Architect Associate Level
#### 47
#### 48
#### 49
#### 50
#### 51
#### 52
#### 53
#### 54
#### 55
### Section 7 - EC2 Instance Storage
#### 56
#### 57
#### 58
#### 59
#### 60
#### 61
#### 62
#### 63
#### 64
#### 65
#### 66
#### 67
#### 68
#### 69
### Section 8 - High availablity and scalability: ELB & ASG
#### 70
#### 71
#### 72
#### 73
#### 74
#### 75
#### 76
#### 77
#### 78
#### 79
#### 80
#### 81
#### 82
#### 83
#### 84
#### 85
#### 86
#### 87
### Section 9 - AWS Fundamentals: RDS + Aurora + ElastiCache
#### 88
#### 89
#### 90
#### 91
#### 92
#### 93
#### 94
#### 95
#### 96
#### 97
#### 98
#### 99
#### 100
#### 101
### Section 12 - Aamazon S3 Introduction
#### 129
#### 130
#### 131
#### 132
#### 133
#### 134
#### 135
#### 136
#### 137
#### 138
#### 139
#### 140
#### 141
#### 142
### Section 15 - Cloudfront & AWS Global Accelerator
#### 166
#### 167
#### 168
#### 169
#### 170
#### 171
#### 172
#### 173
### Section 17 - Decoupling applications: SQS, SNS, Kinesis, Active MQ
#### 184
#### 185
#### 186
#### 187
#### 188
#### 189
#### 190
#### 191
#### 192
#### 193
#### 194
#### 195
#### 196
#### 197
#### 198
#### 199

### Section 19 - Serverless Overview from a Solution Architecture Perspective
#### 214
#### 215
#### 216
#### 217
#### 218
#### 219
#### 220
#### 221
#### 222
#### 223
#### 224
#### 225
#### 226
#### 227
#### 228
#### 229
#### 230
#### 231
### Section 21: Databases in AWS
#### 236
#### 237
#### 238
#### 239
#### 240
#### 241
#### 242
#### 243
#### 244
#### 245
### Section 24: AWS Monitoring & Audit: CloudWatch, CloudTrail & Config
#### 270
#### 271
#### 272
#### 273
#### 274
#### 275
#### 276
#### 277
#### 278
#### 279
#### 280
#### 281
#### 282
#### 283
#### 284
#### 285
#### 286
### Section 26: AWS Security & Encryption: KMS, SSM Parameter Store, SHield, WAF
( only watch videos 304 and 307)
#### 304
#### 307
### Section 27 Networking - VPC
#### 317
#### 318
#### 319
#### 320
#### 321
#### 322
#### 323
#### 324
#### 325
#### 326
#### 327
#### 328
#### 329
#### 330
#### 331
#### 332
#### 333
#### 334
#### 335
(skip videos from 335 until the end)
