# coding-interview-university
This repo will contains my progress in jwasham study plan and other related topics i study 

# Table of Contents
  - [1. Big-O Notation](#1-big-o-notation)
  - [2. Data Structures Section](#2-data-structures-section)
    - [Arrays](#arrays)
    - [Stacks](#stacks)
    - [Queues](#queues)
    - [Lists](#lists)
    - [Trees](#trees)
    - [Dictionary](#dictionary)
    - [Graph](#graph)
   - [3. Principles Section](#3-principles-section)
     - [Encapsulation](#encapsulation)
     - [DRY](#dry)
     - [SOLID](#solid)
   - [4. Databases Section](#4-databases-section)
     - [DBMS](#dbms)
     - [RDBMS](#rdbms)
     - [SQL](#sql)
       - [MySQL](#mysql) 
     - [NoSQL](#nosql)
       - [What is NoSQL ?](#what-is-nosql-) 
       - [Why NoSQL ?](#why-nosql-) 
       - [ACID vs. BASE](#acid-vs-base) 
       - [NoSQL vs. RDBMS](#nosql-vs-rdbms)
       - [Cap Theorem](#cap-theorem)
       - [NoSQL Types](#nosql-types)
       - [Conclusion](#conclusion)
       - [MongoDB](#mongodb)
  - [5. Resources](#5-resources) 

# 1. Big-O Notation

# 2. Data Structures Section 
<br>
<br>

## Arrays
<br>
<br>

## Stacks 
<br>
<br>

## Queues
<br>
<br>

## Lists
<br>
<br>

## Trees
<br>
<br>

## Dictionary
<br>
<br>

## Graph
<br>
<br>

# 3. Principles Section
<br>
<br>

## Encapsulation
<br>
<br>

## DRY
<br>
<br>

## SOLID
<br>
<br>


# 4. Databases Section
<br>
<br>

# DBMS
<br>
<br>

# RDBMS
<br>
<br>

# SQL
<br>
<br>

## MySQL
<br>
<br>

# NoSQL

- #### What is __NoSQL__ ?
  - *NoSQL databases (aka "not only SQL") are non-tabular databases and store data differently than relational tables. NoSQL databases come in a variety of types based on their data model. The main types are document, key-value, wide-column, and graph. They provide flexible schemas and scale easily with large amounts of data and high user loads.*

<br>

- #### Why __NoSQL__ ?
  - *In recent years with the tremendous rise in use of interned and web 2.0 applications , the databases have grown into thousands and thousands of terabytes . Applications such as Facebook, Google, Amazon..etc.  gave rise to an entire new era of daabase management which follows approach of simple design, speed and faster scaling than the traditional databases.*
  -  *Such databases are used in big data , Massive real time applications and analytics .*
 <br>


- #### __ACID vs. BASE__
  - ##### ACID 
    - Atomicity : The database transaction must completely succeed or completely fail . Partial success is not allowed .
    - Consistency : During the database transaction , the RDMS progresses from the one valid state to another . The state is never invalid .
    - Isolation : The client's database transaction must occure in isolation from other clients attempting to transact the RDBMS .
    - Durability : Durability : The data operation that was part of the transaction must be reflected in momvolatile storage ( computer memory that can retrieve stored infomation even when not powered - like a hard dist ) and persist after the transaction successfully completes . Transaction failures cannot leave the data in a partially committed state.

  - ##### BASE :
      - Basically Aavailable : The system is guranteed to be available for querying by all users. (No isolation here.)
      - Soft State : The values stored in the system may change because of the eventual consistency model , as descriped in the next bullet
      - Eventually Consistent : As data is added to the system , the system's state is gradually replicated accross all nodes . For example , in Hadoop , when a files is written to the HDFS , the replicas of the data blocks are created in different data nodes after original data blocks have been written . For the short period before the blocks are replicated , the state of the file system isn't consistent  


<br>

 
- ####  __NoSQL__ vs. __RDBMS__ 
  - ##### Challenges For RDBMS
    -  RDBMS assumes a well-defined structure of data and assumes that the data is largely uniform .
    -  It needs the schema of your application and its properties (columns, types,..etc) to be defines up-front before building the application . This does not match well twith the agile development approaches for highly dynamic applications .
    -  As the data strarts to grow larger , you have to scale your database vertically , i.e. adding more capacity to the existing servers .
  - ##### Benefits of NoSQL over RDBMS
    - __Schema-less :__
        *NoSQL databases being schema-less do not define any strict data structure .*
    - __Dynamic and Agile :__
        *NoSQL databases have good tendency to grow dynamically changing requirements . It can handle structured , semi-structured and unstructured data.*
    - __Scales Horizontally :__
        *In contrast to SQL databases which scale vertically, NoSQL scales horizontally by adding more servers and using concepts of sharding and replication . This behavior of NoSQL fits with the cloud computing services such as (AWS) which allows you to handle virtual servers which can be expanded horizontally on demand.*
    - __Better Performance :__
        *All the NoSQL databases claim to deliver better and faster performance as compared to traditional RDBMS implementations .*
    - __NoSQL limitations :__
      - *Since NosQL is an entire set of databases (and not a single database), the limitations differ from database to database .*
      - *Some of these databases do not support ACID (Atomicity, Consistency, Isolation, Durability) transactions while some of them might be lacking in reliability .*  
      - *But each one of them has their own strengths due to which they well suited for specific requirements .*
      - *No standardization .*
      - *Limited query capabilities (so far) .*
     
<img src= "https://ip1.i.lithium.com/2ab67eb83c8489ad0587c035e1e1f7ca6f84ebce/68747470733a2f2f646f63732e6d6963726f736f66742e636f6d2f656e2d75732f617a7572652f646f63756d656e7464622f6d656469612f646f63756d656e7464622d6e6f73716c2d76732d73716c2f6e6f73716c2d76732d73716c2d636f6d70617269736f6e2e706e67"/>


<br>

- #### __Cap Theorem__
  - *The CAP Theorem states that it is impossible for a distributed computer system to simultaneously provide all three of the following guarantees :*
    -  __Consistency__
    -  __Availability__
    -  __Partition Tolerance__
<br>

<img src = "https://www.nitendratech.com/wp-content/uploads/2020/01/cap_theorem-1024x873.png" width ="650" height = "612" />   
<br>

- #### __NoSQL Types__
  -  *Key-Value Store*
     - __Examples__
       - *redis , riak* 
  -  *Wide Column Store*
     - __Examples__
       - *HBASE , Cassandra*
  -  *Document Store*
     - __Examples__
       - *MongoDB , CouchDB* 
  -  *Graph Store*
     - __Examples__
       -  *Neo4j*
<br>

- __Key Value Databases__
  -  *The key of a key-value pair is a unique value in the set and can be easily looked up to access the data.*
  -  *Key-value pairs are of varied types : some keep the data in memory (redis for example) and some provide the capability to persist the data to disk*
  -  *Key-Value databases can be applied to many scenarios . For example , key-value stores can be useful for storing things such as the following : Shopping cart contents , Product reviews , Product details , Session information , user profiles.*

<br>
<img src= "https://cdn.interviewready.io/assets/nosql-key-value.png" width ="650"  />
<br> 

- __Document Oriented Databases__
  - *These were inspired by Lotus Notes and are similar to key-value stores*
  -  *The model is basically versioned documents that are collections of other key-value collections .*
  -  *The semi-structured documents are stored in formats like JSON.*
  -  *Document databases are essentially the nex level of Key-Value , allowing nested values associated with each key .*
  -  *Document databases support querying more efficiently .*
  -  *Examples : MongoDB , CouchDB*


#### Conclusion
 ##### In summary, the decision between SQL and NoSQL is not a matter of right or wrong. It hinges on understanding the unique requirements and goals of your project. Before making a choice, carefully evaluate the specific needs to ensure the selected database aligns with the demands of your application.

<br>
<br>

# MongoDB
<br>
<br>

# 5. Resources
this resources i have used for my studying
- [Algorithms](https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
- [Data Structures Part1](https://www.youtube.com/playlist?list=PLoK2Lr1miEm-5zCzKE8siQezj9rvQlnca)
- [DBMS](https://www.youtube.com/playlist?list=PLSE8ODhjZXjbohkNBWQs_otTrBTrjyohi)
- [DB](https://www.youtube.com/watch?v=yLc0Yp5QZlU&list=PL37D52B7714788190)
- [NoSQL](https://www.youtube.com/watch?v=xh4gy1lbL2k)
- [MySQL](https://www.youtube.com/watch?v=kb-_GbpH3sQ)
- [mongoDB](https://www.youtube.com/playlist?list=PLesfn4TAj57XGGSmVzzpxY69-lha1EWEI)
- [Principles](https://www.youtube.com/playlist?list=PLnqAlQ9hFYdflFSS4NigVB7aSoYPNwHTL)
