# coding-interview-university
This repo will contains my progress in jwasham study plan and other related topics i study 

# Table of Contents
  - [ ] [1. Big-O Notation](#1-big-o-notation)
  - [2. Data Structures Section](#2-data-structures-section)
    - [Arrays](#arrays)
    - [x] [Stacks](#stacks)
    - [x] [Queues](#queues)
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
     - [x] [NoSQL](#nosql)
       -  [What is NoSQL ?](#what-is-nosql-) 
       - [Why NoSQL ?](#why-nosql-) 
       - [ACID vs. BASE](#acid-vs-base) 
       - [NoSQL vs. RDBMS](#nosql-vs-rdbms)
       - [Cap Theorem](#cap-theorem)
       - [NoSQL Types](#nosql-types)
       - [Conclusion](#conclusion)
       - [MongoDB](#mongodb)
         - [What is MongoDB ?](#what-is-mongodb-)
         - [Why use MongoDB ?](#why-use-mongodb-)
         - [How it works ?](#how-it-works-)
         - [BSON](#bson)
         - [Basic Commands](#basic-commands)
         - [CRUD Operations](#crud-operations)
         - [Data Models](#data-models)
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

- ## __What is MongoDB ?__
  - *MongoDB is a cross-platform , document oriented database that provides , high performance , high availability , and easy scalability .*
  - *MongoDB works on concept of collection and document .*
  - *Designed with both scalability and developer agility*
  - *Built for Speed*
  - *Rich Document based queries for Easy readability*
  - *Full Index Support for High Performance*
  - *Replication and Failover High Availability*
  - *Auto Sharding Easy Scalability*
    -  *A database is a horizontal partition of data in a database or search engine . Each individual partition os referred to as a shard or database shard . Each shard i held on a separate database server instance , to spread load*
  - *MapReduce for Aggregation*
    - *MapReduce is a programming model and a associated implementation for processing and generating big data sets with a parallel , distributed algorithms on a cluster*
  - *Document - oriented database*
    -  *Uses JSON ( BSON actually)*
  - *Schema-free*
  - *Performance*
    - *Written in C++*
    - *Full index support*
    - *No transactions (has atomic operations)*
    - *Memory-mapped files(delayed writes)*
  - *Scalability*
    -  *Replication*
    -  *Audo-Sharding*
  - *Commercially supported*
    - *Lots of documentation*
  - *Supported Platforms :*
    - *OSX - Linux - Solaris - Windows - FreeBSD*
  -  *MongoDB Drivers :*
     - *c, c++ , Java ,JS, .NET (C# F#, PowerShell, etc) Nodejs ,Perl, PHP , Python , Ruby, Scala*
<br>

- ## __Why use MongoDB ?__
  - *SQL was invented in the 70's to store data.*
  - *MongoDB stores documents (or) objects.*
  - *Now-a-days, everyone works with objects (Python/Ruby/Java/etc.)*
  - *And we need Databases to persist our objects .Then why not store objects directly ?*
  - *Embedded documents and arrays  reduce need for joins .*
    - *No joins and No-multi document transactions.* 

- ## __Great for / Not Great For__
  - __MongoDB is great for :__
    -  *RDBMS replacement for Web Applications .*
    -  *Semi-structured Content Management*
    -  *Real-time Analytics & High-Speed Logging*
    -  *Caching and High Scalability*
    -  *Web 2.0 , Media , SAAS , Gaming*
  - __Isn't Great for :__
    -   *Highly Transactional Applications*
    -   *Problems requiring SQL* 
<br>

- ## __How it Works ?__

  <img src="https://cdn.educba.com/academy/wp-content/uploads/2019/05/MongoDB-chart1.jpg" /> 
<br>

- ## __BSON__
  - *It is a computer data interchange format used mainly as a data storage and network transfer format in the MongoDB database*
  - *It is a binary form for representing simple data structures .*
  - *BSON is faster to scan for specific fields than JSON*
  - *BSON adds some additional types such as a date type and byte-array(bindata) datatype.*
  - *Client drivers serialize data to BSON , then transmit the data over the wire to the db*
  - *Data is sotred on disk in BSON format . Thus , on a retrieval , the database very little translation to send anobject out , allowing high efficiency*
  - *The client driver unserialized a received BSON object to its native language format*
 
- ## __What are the goals of BSON ?__
  -  *Fast scan-ability*
  -  *Easy manipulation*
  -  *Additional data types*
 
<br>


- ## __Basic Commands__
  - ```show dbs```
    - as the name saying ,it's gonna shows up the current databases on your machine 
  - ```use "DB's name"```
    -  if the database does not exist it will create it , then switch to it
  -  ```db.createCollection("Collection name",options)```
     -  creating a collection in the database
     - [Check the documentation for more details](https://www.mongodb.com/docs/manual/reference/method/db.createCollection/)
    <br>

  - ## __CRUD Operations__
     - Create 
       - Create Collection
        >     db.createCollection("Collection name",options)
       -  creating a collection in the database
       - [Check the documentation for more details for the options parameter ](https://www.mongodb.com/docs/manual/reference/method/db.createCollection/)
       <br>
       <br>
 

     -  Insert Data
          - you can insert one  document by using  
          >      db.tutorial.insertOne({title:"MongoDB",by:"ITI",url:"maharatech.com/MongoDB"})   
          - or you can insert multiple documents if you need
          >      db.tutorial.insertMany( [{ _id:1, title:"Example1" , by:"Example1" , url:"Example1"} ,
          >     {_id:2 , title:"Example2" , by:"Example2" , url:"Example2" , publishDate : new Date()}])
          
          <br>
          <br>
     
          
          - ***Note that : if you inserted data into a collection does not exists it will create the collection and insert the data into it***
          <br>
          <br>

    - Read 
        - db.tutorial.find({conditions})
        >     db.tutorial.find({title:"MongoDB", by :"ITT"})
  
        - you can access nested documents by using the dot "." notation ,for example
        >     db.inventory.find({'size.w':11 , status : 'D'})
  
        - dealing with array values
        >     db.inventory.find( { tags : [ "red" , "blank" ] } )  // tags "==" [red, blank]
  
        >     db.inventory.find({ tags : { $all : [ "red" , "blank" ] } } ) // tags contains red & blank
      - [Check the documentation for more details and more scenarios](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/)
   
<br> 
<br>

  - Update 
     - db.collection.update[One/Many](fiter, updated values , options )
       - Ex:
           - will __Update only__ the first document that verify the condition 
           >       db.inventory.updateOne({item:"paper"} ,  {  {  $set  :  {  "size.uom" : "cm" ,  status : “p”}}})


           - will __Update all__ documents that verify the condition
           >       db.inventory.updateMany({item:"paper"} ,{{$set:{"size.uom" : "cm" ,  status : “p”}}})           
       - [For more details please check the documentation](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/)

     - db.collection.replaceOne(fiter, new document , options )
       - Ex :
         - *will __Replace only__ the first document that verify the condition*
           >     db.restaurant.replaceOne(   { "name" : "Jhon" },  { "name" : "Jhonny", "Job" : "Engineer" } )
         - [For more details please check the documentation](https://www.mongodb.com/docs/manual/reference/method/db.collection.replaceOne/)
<br>
<br>

  - Delete
    -  Delete is similar to Update  but *Note that if you didn't specify any condition will delete all data in the collection*  
  
- Operators
  - $in : ```db.inventory.find({status: { $in : [ "A" , "D" ]  } )```
  - $or : ```db.inventory.find({ $or : [( status:'A')  , (status :'D')]})```
    - Apply or (Logical Operator) on all the condition in the array
  - $gt (Greater Than ) : ```db.inventory.find({status: { $in : ["A","D"] } , qty : {$gt : 50 } } )```
  - [Check the documentation for more information](https://www.mongodb.com/docs/manual/reference/operator/query/)


 
- ## Data Models
*or in SQL terms relations between collections <br> 
there are Mainly two types of data models in MongoDB*
- __Embedded Data Model__
- __References Data Model__
  - *Manual References*
    - via GUI
    - via command line 
  - *DBRefs*
    - Only via command line 
<br>
<br>


-  __Embedded Data Model (Denormalized Data Model)__
    - This approach maintains all the related data in a single document, which makes it easy to retrieve and maintain .
    - Tho whole document can be retrieved in a single query
      - Ex :
        - ```db.users.findOne( ({"fname":"Jhon" ,"lname": "Jhonny"} ,  {"address_ids": 1 }) )```    
  - Advanteges
    - Better performance for read operations
    - The ability to retrieve related data in a single database operation
    - The ability to to update related data in a single atomic write operation 
  - Disadvantages
    - data duplications
    - embedded document keeps on growing too much in size , and it can impact the read/write performance
  - When to use the __embedded data model__ ?
    - Entities have a “contains” or “has a” relationship between them.
    - Entities have a one-to-many relationship between them. 

      <br>
      <br>

      
-  __References (Normalized Data Model)__
   - Similar to the foriegn key and primary key Concepts from SQL
   - In this approach , both the user and address documents will be maintained separtely but user document will contain a field that will reference the address document's id field.
   - With this approach , we will need two queries And there is two ways to do it`   
- __Manual References__
   -  The references are simple to create and your application can resolve references as needed. 
    <br>  Ex:  
      - ``` var result = db.users.findOne({"fname":"Jhon" ,"lname_id": 1} , {"address_ids": 1} )```
      - ``` var addresses = db.address.find( {"_id":{"$in": result["lname_id"] }} )```
      <br>

      
- __DBRefs__
  - *DBRefs are a convention for representing a document, rather than a specific reference type. They include the name of the collection, and in some cases the database name, in addition to the value from the _id field.*
  - syntax : ```{ "$ref" : <value>, "$id" : <value>, "$db" : <value> }```
    - $ref : ```The $ref field holds the name of the collection where the referenced document resides.```
    - $id : ```The $id field contains the value of the _id field in the referenced document.```
    - $db : ```Contains the name of the database where the referenced document resides.```
  - Ex :
    -
>     {
>        "_id" : ObjectId("2"),
>      // .. application fields
>     "creator" : {
>                  "$ref" : "creators",
>                 "$id" : ObjectId("5126bc054aed4daf9e2ab772"),
>                  "$db" : "users",
>                 "extraField" : "anything"
>              }
>      }    

  - Note That : *The order of fields in the DBRef matters, and you must use the above sequence when using a DBRef.*
<br>

  - Advanteges
      - *No data duplication*
      - *Can represent more complex many-to-many relationships*
      - *Can represent hierarchical data sets* 

   - Disadvantages
     - *More Complicated Queries*
     - *Multiple Queries to read or write data*

   - When to use the __References data model__ ?
      - *Model hierarchical data sets*
      - *Represent many-to-many relationships*
      - *When the read performance gained as a result of using embedded documents does not outweigh the implications of the data duplication.*

  


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
