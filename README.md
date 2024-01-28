# coding-interview-university

This repo will contains my progress in jwasham study plan and other related topics i study

# Table of Contents

- [1. Big-O Notation](#1-big-o-notation)
- [ ] [2. Data Structures Section](#2-data-structures-section)
  - [Arrays](#arrays)
  - [x] [Stacks](#stacks)
    - [Stacks and recursion](#stacks-and-recursion)
  - [x] [Queues](#queues)
  - [x] [Lists](#lists)
    - [Introduction To Lists](#introduction-to-lists)
    - [Why we need Linked Lists? (Arrays Vs. Linked Lists)](#why-we-need-linked-lists-arrays-vs-linked-lists)
    - [Types of Linked Lists](#types-of-linked-lists)
  - [x] [Trees](#trees)
    - [Introduction To Trees](#introduction-to-trees)
    - [Binary Tree](#binary-tree)
      - [Definitions](#definitions)
      - [Summary](#summary)
      - [Theorem](#theorem)
      - [Tree Traversal](#tree-traversal)
      - [BT Implementation](#bt-implementation)
  - [Hash Table](#hash-table)
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
      - [What is NoSQL ?](#what-is-nosql-)
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
        - [Grouping](#grouping)
- [5. Resources](#5-resources)

# 1. Big-O Notation

# 2. Data Structures Section

<br>
<br>

# Definitions

**_Where every thing should start from!_**

- ##### **type :**
  - __is a set of values and a set of operations on those values.__
  - __Example :__
    - _We can define a datatype boolean that takes the set of values {0,1} together with the operations AND, OR, and NOT._
- ##### **Sequence :**
  - _A sequence of length 0 is empty . A sequence of length n >=1 of elements from a set T is an ordered pair (Sn-1,t) Where Sn-1 is a sequence of length n-1 of elements from T and t is an element of T_
- ##### **Abstract Data Type (ADT) :**
  - _is a data type that is accessed only through an interface (or accessing mechanism ) ._
  - _We refer to a program that uses an ADT as a client (or user) and a program that specifies the data type as an implementation_

# Arrays

<br>
<br>

# Stacks

- ##### **Definition** - _: Stack is a linear data structure that follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out)._

- **Main Accessing Mechanisms**
  - _Create the stack , leaving it empty O(1)_
  - _Determine whether the stack is empty or not O(1)_
  - _Determine whether the stack is full or not O(1)_
  - _Find the size of the stack O(1)_
  - _Push a new entry onto the top of the stack , provided the stack is not full O(1)_
  - _Pop the entry off the top of the stack , provided the stack is not empty O(1)_
  - _Retrieve the Top entry off the stack , provided the stack is not empty O(1)_
  - _Traverse the stack , visiting each entry O(n)_
  - _Clear the stack to make it empty_
    - _array based O(1) | O(n) in case linked implemntation_

<br>

- ##### **Where to use it ?**
  - _Mainly it depends on your problem properties but here some examples might inspire you_
    - **Undo Function in any software, it removes the last action you have did**
    - **Web browsers when you hit the back button, it returns you to the last url you have visited**
    - **When a function call another function the OS saves the last address and the data about the previous function**
- **Stack Implementation**

  - _the stack data structure can be implemented Array Based and Linked List Based_
    <br>

  - ### Stacks and recursion

# Queues

- _Generally A Queue is defined as a linear data structure that operations are performed in First In First Out (FIFO) order._
- Main Accessing Mechanisms

  - enqueue O(1)
  - dequeue O(1)
  - front O(1)

- **Examples in Real life**
  - _Requests are served from a single shared resource, such as a printer, and CPU tasks are scheduled, among other things._
  - _In the real world, Call Center phone systems use Queues to keep people who call in order until a service person is available._
  - _Interrupt handling in real-time systems. Interrupts are dealt with in the order in which they are received, i.e. first come, first served._
- **Types of Queues**

  - _Simple Queue_
    - _In a simple queue, insertion takes place at the rear and removal occurs at the front. It strictly follows the FIFO (First in First out) rule._
      <img src = "https://media.geeksforgeeks.org/wp-content/uploads/20220805131014/fifo.png" height= 300 width = 650 />
  - _Circular Queue_
    - _In a circular queue, the last element points to the first element making a circular link._
      <img src= "https://miro.medium.com/v2/resize:fit:1400/1*J9K866QWpLC9OkmLLn3nEA.png" height= 300 width = 650 />
  - _Priority Queue_
    - _A priority queue is a special type of queue in which each element is associated with a priority and is served according to its priority. If elements with the same priority occur, they are served according to their order in the queue._
  - _Deque (Double Ended Queue)_
    - _In a double ended queue, insertion and removal of elements can be performed from either from the front or rear. Thus, it does not follow the FIFO (First In First Out) rule._
      <img src= "https://favtutor.com/resources/images/uploads/mceu_34159180611678861723756.png" height= 300 width = 650 />

- Implementation
  - i have implemented [Circular Queue Array based](data_structures_implementation/python/array_based/queue.py)
  - i have implemented [Queue Linked Based](data_structures_implementation/python/linked_based/queue.py)

# Lists

- ## Introduction To lists

  __What is Linked List ?__
  <br>

_A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers._

<br>

## Why we need Linked Lists? (Arrays Vs. Linked Lists)

_Linked lists offer several advantages and use cases in comparison to other data structures like arrays. Here are some reasons why linked lists are useful (Advantages):_
<br>

- **Dynamic Size:**
  - _Linked lists can dynamically adjust their size during program execution. Unlike arrays, which have a fixed size, linked lists can easily grow or shrink as needed._
- **Easy to insert and delete:**
  - _Inserting or deleting elements in a linked list is more efficient than in an array. In an array, these operations may require shifting elements, which can be time-consuming. In a linked list, inserting or deleting a node involves updating pointers, making these operations faster._
- **No Wasted Memory:**
  - _Linked lists do not waste memory. In arrays, you might need to allocate a larger block of memory than necessary to accommodate potential future elements. Linked lists use only the memory required for the current elements._
- **No Pre-allocation of Memory:**
  - _Linked lists do not require pre-allocation of memory. Arrays often need to allocate a fixed amount of memory in advance, which may lead to inefficient use of memory if the actual data size is smaller._
- **Dynamic Memory Allocation:**
  - _Nodes in a linked list can be allocated dynamically, allowing for efficient memory usage. This contrasts with arrays, where memory is allocated statically, and resizing may require copying data._
- **Efficient for Insertions and Deletions at Any Position:**
  - _Inserting or deleting elements in the middle of a linked list is more efficient than in an array. For arrays, shifting elements is required, while linked lists can update pointers to achieve the same result without moving data._
- **Support for Various Types of Lists:**
  - _Different types of linked lists, such as singly linked lists, doubly linked lists, and circular linked lists, offer flexibility for different use cases and requirements._
- **Implementation of Data Structures:**
  - _Linked lists are fundamental in implementing other data structures, such as stacks and queues, as well as more complex structures like graphs and hash tables._
- **No Pre-declaration of Size:**
  - _Linked lists do not require specifying the size in advance. This is particularly beneficial when the number of elements is unknown or can vary._  
    <br>

**hold still There is nothing for free , Here some disadvantages of Linked Lists :**

- _Memory Overhead:_
  - **Linked lists require extra memory per element to store the pointer to the next node. This additional memory overhead is not present in arrays.**
- _Random Access Limitation:_
  - _Unlike arrays, where elements can be accessed randomly using indices, linked lists do not provide constant-time access to individual elements. To access a specific element, you need to traverse the list from the beginning or atleast you have to do Fraction of N operations to accesses specific element._
- _No Cache Friendliness:_
  - **Linked lists are not cache-friendly. In arrays, elements are stored in contiguous memory locations, which takes advantage of caching mechanisms. In contrast, linked list nodes can be scattered in memory, leading to more cache misses.**
- _Sequential Access:_
  - **Linked lists are better suited for sequential access. Random access patterns, common in certain algorithms or applications, might result in poor performance compared to arrays.**

<br>
<br>
  
 - # Types of linked Lists
    - *Singly Linked List*
      -   __It is the simplest type of linked list in which every node contains some data and a pointer to the next node , and the last node is pointing to *Null*__
      - *real life examples*
        - __Browser History:__
          - *Singly linked lists can be used to implement browser history. Each page visited is a node, and the link points to the next page visited.*
         
        - __Task Management:__
          - *In task management applications, a singly linked list can be used to represent a list of tasks. Each node contains information about a task and a link to the next task.*
        - __Music Playlist:__
          - *Singly linked lists can be used to implement playlists. Each node represents a song, and the link points to the next song in the playlist.*  
    - *Double Linked List*
      - __A doubly linked list or a two-way linked list is a more complex type of linked list that contains a pointer to the next as well as the previous node in sequence.__
      - *real life examples*
        - __Text Editors:__
          - *Doubly linked lists can be used in text editors to implement an undo/redo feature. Each node represents a state, and the links point to the previous and next states.*
        - __Cache Management:__
          - *In systems where efficient insertion and deletion are crucial, doubly linked lists can be used to manage caches. Nodes can be easily moved or removed.*
        - __Navigation Systems:__
          - *Doubly linked lists can be employed in navigation systems where the user can go backward and forward through locations visited.*    
      
      <br>
      
        <img src="https://miro.medium.com/v2/resize:fit:615/1*5wRMqVjLatOGX88VrZgacA.jpeg" height = 300 width = 650 />

    - *Circular Linked List*
      - __is the same as singly linked list but the difference is the last node is pointing the forst node, which making it Circular Linked list__
        <br>


        <img src= "https://scaler-topics-articles-md.s3.us-west-2.amazonaws.com/circular-linked-list-visualization.webp" height = 300 width = 650/>
      - *real life examples*
        - __Round-Robin Scheduling:__
          - *Circular linked lists can be used in scheduling algorithms, such as round-robin scheduling in operating systems, where tasks are processed in a circular order.*
        - __Multiplayer Games:__
          - *In multiplayer games, a circular linked list can represent a turn order. Players take turns in a circular fashion.*
        - __Resource Allocation:__
          - *In systems with shared resources, a circular linked list can be used for resource allocation, ensuring fair distribution among users.*
         <br>


    - *Doubly Circular Linked List*
       - __It is the same as a Double Linked list but the last Node is pointing to the first node__

      <br>
      <img src= "https://media.geeksforgeeks.org/wp-content/uploads/Circular-doubly-linked-list.png" height = 300 width = 650/>

       - *real life examples*
         - __Music Player with Repeat:__
           - *Circular doubly linked lists are useful in implementing a music player with a repeat feature. The last song is linked to the first, and vice versa.*
         - __File System Management:__
           - *In a file system, a circular doubly linked list can be used to represent the allocation of disk blocks. The last block is linked to the first, forming a circular structure.*
         - __Graphics and Animation:__
           - *Circular doubly linked lists can be employed in graphics and animation systems where elements need to loop or cycle through a sequence.*

- **Implementation**
  - [I have implemented singly linked list Using Pointers at First and End](data_structures_implementation/python/linked_based/singly_linked_list.py)
  - [I have implemented circular doubly linked list](data_structures_implementation/python/linked_based/circular_doubly_linked_list.py)

# Trees

- ## Introduction To Trees

  - The tree is a nonlinear hierarchical data structure and comprises a collection of entities known as nodes. It connects each node in the tree data structure using "edges”, both directed and undirected.
  - The image below represents the tree data structure. The blue-colored circles depict the nodes of the tree and the black lines connecting each node with another are called edges.

  <br>
    <img src = "https://www.tutorialandexample.com/wp-content/uploads/2020/10/image-68.png"   />
    <br>
- ## Binary Tree
- Generally there are many types of trees either they are binary or not (ternary or N nodes), But i will start with BT , BST

## Definitions

- **What is Binary Tree Data Structure ?**

  - _A binary tree is either empty, or it consists of a node (vertex) called the root together with two binary trees called the left subtree and the right subtree of the root_

- Binary Search Tree : Is Tree produced by Binary Search Algorithm

   <br>

- **Notes** about the previous definition :

  - _The only node at level 0 is the root_
  - A node may have up to two children in the next level
  - The children of a node are joined to their parents by links called edges

- **Depth (or height) :**

  - The depth of a node is the tree is the node's distance from the root; i.e., its level
  - Equivalent Definition (revursive) : The depth of a node is 1 + the depth of its parent . And the root is at depth 0.

- The collection of nodes in the subtree rooted at a node (excluding the node itself) is referred to as its **descendants**.
- The collection of nodes encountered by climbing down (to the root) a path from a node to the root of the whole ree is the node's **ancestors (or predecessors).**
- The depth or height h of a tree : is the maximum height among nodes . Also, we can say

  - h = 0 incase tree has only root
  - or = 1 + max(h(left tree) , h(right tree))
  - h = height

- Outdegree : is the number of edges coming out of a node . In binary trees is at most 2.
- Indegree : is the number of edges coming to a node . In any tree this is 1.
- Lemma : a saturated (with maximum number of nodes) level i has 2<sup>i</sup>
  - Proof : For i = 0 the statement is true . Assume it is true for some k, then the number of nodes om this level is 2<sup>k</sup>. Then , the maximum number of nodes of next level, k + 1, is 2 x 2<sup>k</sup>,which completes the induction .
- Saturated Level : a level with maximum number of nodes .
- Full Tree : a tree whose all levels are saturated
- Corollary : If all levels (from 0 to h) are saturated then the trees has 2<sup>h+1</sup>-1 nodes - Proof : <br>

  $$
  n = \left(\sum\_{l=0}^h 2^l \right) = 2^{h + 1} - 1
  $$

- Complete Tree : Is the tree whose all levels are saturated except possibly the last one.

  - its leaves are at the last two levels at most (the converse is not true)
  - it is the shortest tree for given number of nodes

- ## Summary
  - _Each tree has a root node (at the top) having some value._
  - _The root node has zero or more child nodes._
  - _Each child node has zero or more child nodes, and so on. This create a subtree in the tree. Every node has it’s own subtree made up of his children and their children, etc. This means that every node on its own can be a tree._
    - **A binary search tree (BST) adds these two characteristics:**
      - _Each node has a maximum of up to two children._
      - _For each node, the values of its left descendent nodes are less than that of the current node, which in turn is less than the right descendent nodes (if any)._

## Theorem

<br>
For the binary search algorithm :
<br>

- the best case takes 1 comparison
- The worst successful case takes

   <br>

$$
h_n + 1 = \lceil \log(n+1) \rceil = \lfloor \log(n) \rfloor + 1.
$$

<br>

- the unsuccessful case takes exactly h<sub>n</sub> + 1 if the tree is ful , i.e., all levels are saturated and takes either h<sub>n</sub> or h<sub>n</sub> + 1 otherwise.
- no other search method (based on comparison) does better than binary search in **the worst case**
  <br>

## Tree Traversal

- Before ADT and coding , How to traverse a BT ?
 - There was no problem for traversing a linear structure like a List, But for a BT, at each node V having left and right subtrees L and R (respectively) we can do the following visitng :
   - VLR (Preorder)
   - VRL 
   - LVR (Inorder) 
   - LRV (Postorder) 
   - RVL
   - RLV 
   - The standards are Pre,In,and Post order. In the three of them , L precedes R; then V is before them (Pre) or in between (In) or after them(Post)
  <br>
  <img src="https://www.sahinarslan.tech/static/f0f154c04b1c5399e973609a7f4a2cf3/3d469/binary-tree-traversals.jpg" height = 500 wedth = 650 />

- __Note That :__ The inorder traversal gives us *Sorted* array  

<br>

## BT Implementation

GO TO [BT Implementation](data_structures_implementation/python/linked_based/b_trees.py)

<br>

# Hash Table

<br>
<br>

# Graph

<br>
<br>

# 3. Principles Section

<br>
<br>

# Encapsulation

or Information Hiding
Can be used to isolate or restrict the user from direct Access to the Attribute .
<br>

### **What happens When you apply it ?**

- _The use of functions . You use the structure at the "User Level" without caring about the details at the "Implementation Level"_
  - _Your program , i.e.., the user level , does not change even if the implementation of the used structure is changed_
  - _Your program is clear from the logical point of view_
  - _Enhancing the Top-Down-Design_
  - _Hiding unnecessary data from users, your program gets More flexible and become Easy to reuse_

### **How to apply it ?**

- _in the oop context you have to make the members of the class private and setup getters & setters , otherwise it's a general concept you can consider while you providing your programs_

<br>

# DRY

<br>
<br>

# SOLID

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

# MySQL

<br>
<br>

# NoSQL

- #### What is **NoSQL** ?
  - _NoSQL databases (aka "not only SQL") are non-tabular databases and store data differently than relational tables. NoSQL databases come in a variety of types based on their data model. The main types are document, key-value, wide-column, and graph. They provide flexible schemas and scale easily with large amounts of data and high user loads._

<br>

- #### Why **NoSQL** ?

  - _In recent years with the tremendous rise in use of interned and web 2.0 applications , the databases have grown into thousands and thousands of terabytes . Applications such as Facebook, Google, Amazon..etc. gave rise to an entire new era of daabase management which follows approach of simple design, speed and faster scaling than the traditional databases._
  - _Such databases are used in big data , Massive real time applications and analytics ._
    <br>

- #### **ACID vs. BASE**

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

- #### **NoSQL** vs. **RDBMS**
  - ##### Challenges For RDBMS
    - RDBMS assumes a well-defined structure of data and assumes that the data is largely uniform .
    - It needs the schema of your application and its properties (columns, types,..etc) to be defines up-front before building the application . This does not match well twith the agile development approaches for highly dynamic applications .
    - As the data strarts to grow larger , you have to scale your database vertically , i.e. adding more capacity to the existing servers .
  - ##### Benefits of NoSQL over RDBMS
    - **Schema-less :**
      _NoSQL databases being schema-less do not define any strict data structure ._
    - **Dynamic and Agile :**
      _NoSQL databases have good tendency to grow dynamically changing requirements . It can handle structured , semi-structured and unstructured data._
    - **Scales Horizontally :**
      _In contrast to SQL databases which scale vertically, NoSQL scales horizontally by adding more servers and using concepts of sharding and replication . This behavior of NoSQL fits with the cloud computing services such as (AWS) which allows you to handle virtual servers which can be expanded horizontally on demand._
    - **Better Performance :**
      _All the NoSQL databases claim to deliver better and faster performance as compared to traditional RDBMS implementations ._
    - **NoSQL limitations :**
      - _Since NosQL is an entire set of databases (and not a single database), the limitations differ from database to database ._
      - _Some of these databases do not support ACID (Atomicity, Consistency, Isolation, Durability) transactions while some of them might be lacking in reliability ._
      - _But each one of them has their own strengths due to which they well suited for specific requirements ._
      - _No standardization ._
      - _Limited query capabilities (so far) ._

<img src= "https://ip1.i.lithium.com/2ab67eb83c8489ad0587c035e1e1f7ca6f84ebce/68747470733a2f2f646f63732e6d6963726f736f66742e636f6d2f656e2d75732f617a7572652f646f63756d656e7464622f6d656469612f646f63756d656e7464622d6e6f73716c2d76732d73716c2f6e6f73716c2d76732d73716c2d636f6d70617269736f6e2e706e67"/>

<br>

- #### **Cap Theorem**
  - _The CAP Theorem states that it is impossible for a distributed computer system to simultaneously provide all three of the following guarantees :_ - **Consistency** - **Availability** - **Partition Tolerance**
    <br>

<img src = "https://www.nitendratech.com/wp-content/uploads/2020/01/cap_theorem-1024x873.png" width ="650" height = "612" />   
<br>

- #### **NoSQL Types**

  - _Key-Value Store_
    - **Examples**
      - _redis , riak_
  - _Wide Column Store_
    - **Examples**
      - _HBASE , Cassandra_
  - _Document Store_
    - **Examples**
      - _MongoDB , CouchDB_
  - _Graph Store_ - **Examples** - _Neo4j_
    <br>

- **Key Value Databases**
  - _The key of a key-value pair is a unique value in the set and can be easily looked up to access the data._
  - _Key-value pairs are of varied types : some keep the data in memory (redis for example) and some provide the capability to persist the data to disk_
  - _Key-Value databases can be applied to many scenarios . For example , key-value stores can be useful for storing things such as the following : Shopping cart contents , Product reviews , Product details , Session information , user profiles._

<br>
<img src= "https://cdn.interviewready.io/assets/nosql-key-value.png" width ="650"  />
<br>

- **Document Oriented Databases**
  - _These were inspired by Lotus Notes and are similar to key-value stores_
  - _The model is basically versioned documents that are collections of other key-value collections ._
  - _The semi-structured documents are stored in formats like JSON._
  - _Document databases are essentially the nex level of Key-Value , allowing nested values associated with each key ._
  - _Document databases support querying more efficiently ._
  - _Examples : MongoDB , CouchDB_

#### Conclusion

##### In summary, the decision between SQL and NoSQL is not a matter of right or wrong. It hinges on understanding the unique requirements and goals of your project. Before making a choice, carefully evaluate the specific needs to ensure the selected database aligns with the demands of your application.

<br>
<br>

# MongoDB

- ## **What is MongoDB ?**

  - _MongoDB is a cross-platform , document oriented database that provides , high performance , high availability , and easy scalability ._
  - _MongoDB works on concept of collection and document ._
  - _Designed with both scalability and developer agility_
  - _Built for Speed_
  - _Rich Document based queries for Easy readability_
  - _Full Index Support for High Performance_
  - _Replication and Failover High Availability_
  - _Auto Sharding Easy Scalability_
    - _A database is a horizontal partition of data in a database or search engine . Each individual partition os referred to as a shard or database shard . Each shard i held on a separate database server instance , to spread load_
  - _MapReduce for Aggregation_
    - _MapReduce is a programming model and a associated implementation for processing and generating big data sets with a parallel , distributed algorithms on a cluster_
  - _Document - oriented database_
    - _Uses JSON ( BSON actually)_
  - _Schema-free_
  - _Performance_
    - _Written in C++_
    - _Full index support_
    - _No transactions (has atomic operations)_
    - _Memory-mapped files(delayed writes)_
  - _Scalability_
    - _Replication_
    - _Audo-Sharding_
  - _Commercially supported_
    - _Lots of documentation_
  - _Supported Platforms :_
    - _OSX - Linux - Solaris - Windows - FreeBSD_
  - _MongoDB Drivers :_ - _c, c++ , Java ,JS, .NET (C# F#, PowerShell, etc) Nodejs ,Perl, PHP , Python , Ruby, Scala_
    <br>

- ## **Why use MongoDB ?**

  - _SQL was invented in the 70's to store data._
  - _MongoDB stores documents (or) objects._
  - _Now-a-days, everyone works with objects (Python/Ruby/Java/etc.)_
  - _And we need Databases to persist our objects .Then why not store objects directly ?_
  - _Embedded documents and arrays reduce need for joins ._
    - _No joins and No-multi document transactions._

- ## **Great for / Not Great For**

  - **MongoDB is great for :**
    - _RDBMS replacement for Web Applications ._
    - _Semi-structured Content Management_
    - _Real-time Analytics & High-Speed Logging_
    - _Caching and High Scalability_
    - _Web 2.0 , Media , SAAS , Gaming_
  - **Isn't Great for :** - _Highly Transactional Applications_ - _Problems requiring SQL_
    <br>

- ## **How it Works ?**

  <img src="https://cdn.educba.com/academy/wp-content/uploads/2019/05/MongoDB-chart1.jpg" /> 
<br>

- ## **BSON**

  - _It is a computer data interchange format used mainly as a data storage and network transfer format in the MongoDB database_
  - _It is a binary form for representing simple data structures ._
  - _BSON is faster to scan for specific fields than JSON_
  - _BSON adds some additional types such as a date type and byte-array(bindata) datatype._
  - _Client drivers serialize data to BSON , then transmit the data over the wire to the db_
  - _Data is sotred on disk in BSON format . Thus , on a retrieval , the database very little translation to send anobject out , allowing high efficiency_
  - _The client driver unserialized a received BSON object to its native language format_

- ## **What are the goals of BSON ?**
  - _Fast scan-ability_
  - _Easy manipulation_
  - _Additional data types_

<br>

- ## **Basic Commands**

  - `show dbs`
    - as the name saying ,it's gonna shows up the current databases on your machine
  - `use "DB's name"`
    - if the database does not exist it will create it , then switch to it
  - `db.createCollection("Collection name",options)`

    - creating a collection in the database
    - [Check the documentation for more details](https://www.mongodb.com/docs/manual/reference/method/db.createCollection/)
      <br>

  - ## **CRUD Operations**

    - Create

      - Create Collection
        >     db.createCollection("Collection name",options)
      - creating a collection in the database
      - [Check the documentation for more details for the options parameter ](https://www.mongodb.com/docs/manual/reference/method/db.createCollection/)
        <br>
        <br>

    - Insert Data

      - you can insert one document by using
        >      db.tutorial.insertOne({title:"MongoDB",by:"ITI",url:"maharatech.com/MongoDB"})
      - or you can insert multiple documents if you need

        >      db.tutorial.insertMany( [{ _id:1, title:"Example1" , by:"Example1" , url:"Example1"} ,
        >     {_id:2 , title:"Example2" , by:"Example2" , url:"Example2" , publishDate : new Date()}])

        <br>
        <br>

      - **_Note that : if you inserted data into a collection does not exists it will create the collection and insert the data into it_**
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

- Update - db.collection.update[One/Many](fiter, updated values , options ) - Ex: - will **Update only** the first document that verify the condition > db.inventory.updateOne({item:"paper"} , { { $set : { "size.uom" : "cm" , status : “p”}}})

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

  - Delete is similar to Update but _Note that if you didn't specify any condition will delete all data in the collection_

- Operators

  - $in : `db.inventory.find({status: { $in : [ "A" , "D" ]  } )`
  - $or : `db.inventory.find({ $or : [( status:'A')  , (status :'D')]})`
    - Apply or (Logical Operator) on all the condition in the array
  - $gt (Greater Than ) : ```db.inventory.find({status: { $in : ["A","D"] } , qty : {$gt : 50 } } )```
  - [Check the documentation for more information](https://www.mongodb.com/docs/manual/reference/operator/query/)

- ## Data Models
  _or in SQL terms relations between collections <br>
  there are Mainly two types of data models in MongoDB_
- **Embedded Data Model**
- **References Data Model**

  - _Manual References_
    - via GUI
    - via command line
  - _DBRefs_ - Only via command line
    <br>
    <br>

- **Embedded Data Model (Denormalized Data Model)**
  - This approach maintains all the related data in a single document, which makes it easy to retrieve and maintain .
  - Tho whole document can be retrieved in a single query
    - Ex :
      - `db.users.findOne( ({"fname":"Jhon" ,"lname": "Jhonny"} ,  {"address_ids": 1 }) )`
- Advanteges
  - Better performance for read operations
  - The ability to retrieve related data in a single database operation
  - The ability to to update related data in a single atomic write operation
- Disadvantages
  - data duplications
  - embedded document keeps on growing too much in size , and it can impact the read/write performance
- When to use the **embedded data model** ?

  - Entities have a “contains” or “has a” relationship between them.
  - Entities have a one-to-many relationship between them.

    <br>
    <br>

- **References (Normalized Data Model)**
  - Similar to the foriegn key and primary key Concepts from SQL
  - In this approach , both the user and address documents will be maintained separtely but user document will contain a field that will reference the address document's id field.
  - With this approach , we will need two queries And there is two ways to do it`
- **Manual References**
  - The references are simple to create and your application can resolve references as needed.
    <br> Ex:
    - ` var result = db.users.findOne({"fname":"Jhon" ,"lname_id": 1} , {"address_ids": 1} )`
    - ` var addresses = db.address.find( {"_id":{"$in": result["lname_id"] }} )`
      <br>
- **DBRefs**

  - _DBRefs are a convention for representing a document, rather than a specific reference type. They include the name of the collection, and in some cases the database name, in addition to the value from the \_id field._
  - syntax : `{ "$ref" : <value>, "$id" : <value>, "$db" : <value> }`
    - $ref : `The $ref field holds the name of the collection where the referenced document resides.`
    - $id : `The $id field contains the value of the _id field in the referenced document.`
    - $db : `Contains the name of the database where the referenced document resides.`
  - Ex : -

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

  - Note That : _The order of fields in the DBRef matters, and you must use the above sequence when using a DBRef._
    <br>

  - Advanteges

    - _No data duplication_
    - _Can represent more complex many-to-many relationships_
    - _Can represent hierarchical data sets_

  - Disadvantages

    - _More Complicated Queries_
    - _Multiple Queries to read or write data_

  - When to use the **References data model** ? - _Model hierarchical data sets_ - _Represent many-to-many relationships_ - _When the read performance gained as a result of using embedded documents does not outweigh the implications of the data duplication._
    <br>
    <br>

## Grouping

- What is _Grouping_ ?
  <br>
  grouping is a stage in your query, and it's all about separates documents into groups according to a "group key". The output is one document for each unique group key.

- Syntax :

  >     {
  >       $group:
  >      {
  >       _id: <expression>, // Group key
  >        <field1>: { <accumulator1> : <expression1> },
  >        ...
  >     }
  >     }
  >
  > <br> 
  > <br>

- Ex :
  >      db.sales.aggregate( [
  >      {
  >        $group: {
  >           _id: null,
  >           count: { $count: { } }
  >        }
  >      }
  >      ] )
- it's equivelant to `SELECT COUNT(*) AS count FROM sales` in SQL

- How to apply conditions on Groups ?

  - if you want to appyl condtions on groups you need to use the `$match` operator
  - Here example for demonstration

    >      db.sales.aggregate(
    >     [
    >      // First Stage
    >     {$group :{
    >               _id : "$item",
    >                totalSaleAmount: { $sum: { $multiply: [ "$price", "$quantity" ] } }
    >             }
    >     },
    >        // Second Stage
    >        {
    >       $match: { "totalSaleAmount": { $gte: 100 } }
    >        }
    >     ]
    >                  )

  - [For more details please check the documentation](https://www.mongodb.com/docs/manual/reference/operator/aggregation/group/)

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
