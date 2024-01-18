# coding-interview-university
This repo will contains my progress in jwasham study plan and other related topics i study 

# Table of Contents
  -   [1. Big-O Notation](#1-big-o-notation)
  - [ ] [2. Data Structures Section](#2-data-structures-section)
    - [Arrays](#arrays)
    - [x] [Stacks](#stacks)
      - [Stacks and recursion](#stacks-and-recursion) 
    - [x] [Queues](#queues)
    - [x] [Lists](#lists)
      - [Introduction To Lists](#introduction-to-lists)
      - [Why we need Linked Lists? (Arrays Vs. Linked Lists)](#why-we-need-linked-lists-arrays-vs-linked-lists)
      - [Types of Linked Lists](#types-of-linked-lists)
      - [Trees](#trees)
      - [Dictionary](#dictionary)
      - [Graph](#graph)
   - [3. Principles Section](#3-principles-section)
     - [Encapsulation](#encapsulation)
     - [DRY](#dry)
     - [SOLID](#solid)
   -  [4. Databases Section](#4-databases-section)
     - [DBMS](#dbms)
     - [RDBMS](#rdbms)
     - [SQL](#sql)
       - [MySQL](#mysql) 
     - [NoSQL](#nosql)
       - [mongoDB](#mongodb)
  - [5. Resources](#5-resources) 

# 1. Big-O Notation

# 2. Data Structures Section 
<br>
<br>

# Definitions 
***Where every thing should start from!***

- #####  __type :__
   -  *is a set of values and a set of operations on those values.*
   -  *Example :*
      - _We can define a datatype boolean that takes the set of values {0,1} together with the operations AND, OR, and NOT._
    
- ##### __Sequence :__
  - *A sequence of length 0 is empty . A sequence of length n >=1 of elements from a set T is an ordered pair (Sn-1,t)  Where Sn-1 is a sequence of length  n-1 of elements from T and t is an element of T*
   
- ##### __Abstract Data Type (ADT) :__
  - *is a data type that is accessed only through an interface (or accessing mechanism ) .*
  - *We refer to a program  that uses an ADT as a client (or user) and a program that specifies the data type as an implementation*


# Arrays
<br>
<br>

# Stacks 
- ##### __Definition__ - *: Stack is a linear data structure that follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).* 

- __Main Accessing Mechanisms__
  - *Create the stack , leaving it empty O(1)*
  - *Determine whether the stack is empty or not O(1)* 
  - *Determine whether the stack is full or not O(1)*
  - *Find the size of the stack O(1)*
  - *Push a new entry onto the top of the stack , provided the stack is not full O(1)*
  - *Pop the entry off the top of the stack , provided the stack is not empty O(1)*
  - *Retrieve  the Top entry off the stack , provided the stack is not empty O(1)*
  - *Traverse the stack , visiting each entry O(n)*
  - *Clear the stack to make it empty*
    - *array based O(1) | O(n)  in case linked implemntation*

<br>

- ##### __Where to use it ?__
  - *Mainly it depends on your problem properties but here some examples might inspire you*
    -  __Undo Function in any software, it removes the last action you have did__
    -  __Web browsers when you hit the back button, it returns you to the last url you have visited__
    -  __When a function call another function the OS saves the last address and the data about the previous function__
   
- __Stack Implementation__
  - *the stack data structure can be implemented Array Based and Linked List Based*
<br>


  - ### Stacks and recursion 

# Queues
- *Generally A Queue is defined as a linear data structure that operations are performed in First In First Out (FIFO) order.*
- Main Accessing Mechanisms
  - enqueue O(1)
  - dequeue O(1)
  -  front O(1)
 
- __Examples in Real life__
  - *Requests are served from a single shared resource, such as a printer, and CPU tasks are scheduled, among other things.*
  - *In the real world, Call Center phone systems use Queues to keep people who call in order until a service person is available.*
  - *Interrupt handling in real-time systems. Interrupts are dealt with in the order in which they are received, i.e. first come, first served.* 
- __Types of Queues__
  -  *Simple Queue*
     -  *In a simple queue, insertion takes place at the rear and removal occurs at the front. It strictly follows the FIFO (First in First out) rule.*
     <img src = "https://media.geeksforgeeks.org/wp-content/uploads/20220805131014/fifo.png" height= 300 width = 650 />
     
  -  *Circular Queue*
     -  *In a circular queue, the last element points to the first element making a circular link.*
     <img src= "https://miro.medium.com/v2/resize:fit:1400/1*J9K866QWpLC9OkmLLn3nEA.png" height= 300 width = 650 />
     
  -  *Priority Queue*
     - *A priority queue is a special type of queue in which each element is associated with a priority and is served according to its priority. If elements with the same priority occur, they are served according to their order in the queue.*
     
  -  *Deque (Double Ended Queue)*
     - *In a double ended queue, insertion and removal of elements can be performed from either from the front or rear. Thus, it does not follow the FIFO (First In First Out) rule.*
     <img src= "https://favtutor.com/resources/images/uploads/mceu_34159180611678861723756.png" height= 300 width = 650 />

- Implementation
  - i have implemented  [Circular Queue Array based](data_structures_implementation/python/array_based/queue.py)
  - i have implemented [Queue Linked Based](data_structures_implementation/python/linked_based/queue.py)


# Lists

 - # Introduction To lists
   - __What is Linked List ?__
<br>


*A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers.*

<br>


## Why we need Linked Lists? (Arrays Vs. Linked Lists)

*Linked lists offer several advantages and use cases in comparison to other data structures like arrays. Here are some reasons why linked lists are useful (Advantages):*
<br>
   - __Dynamic Size:__
     - *Linked lists can dynamically adjust their size during program execution. Unlike arrays, which have a fixed size, linked lists can easily grow or shrink as needed.*
   - __Easy to insert and delete:__
     - *Inserting or deleting elements in a linked list is more efficient than in an array. In an array, these operations may require shifting elements, which can be time-consuming. In a linked list, inserting or deleting a node involves updating pointers, making these operations faster.*
   - __No Wasted Memory:__
     - *Linked lists do not waste memory. In arrays, you might need to allocate a larger block of memory than necessary to accommodate potential future elements. Linked lists use only the memory required for the current elements.*
   - __No Pre-allocation of Memory:__
     - *Linked lists do not require pre-allocation of memory. Arrays often need to allocate a fixed amount of memory in advance, which may lead to inefficient use of memory if the actual data size is smaller.*
   - __Dynamic Memory Allocation:__
     - *Nodes in a linked list can be allocated dynamically, allowing for efficient memory usage. This contrasts with arrays, where memory is allocated statically, and resizing may require copying data.*
   - __Efficient for Insertions and Deletions at Any Position:__
     - *Inserting or deleting elements in the middle of a linked list is more efficient than in an array. For arrays, shifting elements is required, while linked lists can update pointers to achieve the same result without moving data.*
   - __Support for Various Types of Lists:__
     - *Different types of linked lists, such as singly linked lists, doubly linked lists, and circular linked lists, offer flexibility for different use cases and requirements.*
   - __Implementation of Data Structures:__
     - *Linked lists are fundamental in implementing other data structures, such as stacks and queues, as well as more complex structures like graphs and hash tables.*
   - __No Pre-declaration of Size:__
     - *Linked lists do not require specifying the size in advance. This is particularly beneficial when the number of elements is unknown or can vary.*  
  <br>

__hold still There is nothing for free , Here some disadvantages of Linked Lists :___
- *Memory Overhead:*
  - __Linked lists require extra memory per element to store the pointer to the next node. This additional memory overhead is not present in arrays.__
- *Random Access Limitation:*
  -  *Unlike arrays, where elements can be accessed randomly using indices, linked lists do not provide constant-time access to individual elements. To access a specific element, you need to traverse the list from the beginning or atleast you have to do Fraction of N operations to accesses specific element.*
- *No Cache Friendliness:*
  - __Linked lists are not cache-friendly. In arrays, elements are stored in contiguous memory locations, which takes advantage of caching mechanisms. In contrast, linked list nodes can be scattered in memory, leading to more cache misses.__
- *Sequential Access:*
  - __Linked lists are better suited for sequential access. Random access patterns, common in certain algorithms or applications, might result in poor performance compared to arrays.__       

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

   - __Implementation__
     -  [I have implemented singly linked list Using Pointers at First and End](data_structures_implementation/python/linked_based/singly_linked_list.py)
     -  [I have implemented circular doubly linked list](data_structures_implementation/python/linked_based/circular_doubly_linked_list.py)

      
# Trees
<br>
<br>

# Dictionary
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

### __What happens When you apply it ?__
- *The use of functions . You use the structure at the "User Level" without caring about the details at the "Implementation Level"*
  - *Your program , i.e.., the user level , does not change even if the implementation of the used structure is changed*
  - *Your program is clear from the logical point of view*
  - *Enhancing the Top-Down-Design*
  - *Hiding unnecessary  data from users, your program gets More flexible  and become Easy to reuse* 

### __How to apply it ?__
-  *in the oop context you have to make the members of the class private and setup getters & setters , otherwise it's a general concept you can consider while you providing your programs*

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
<br>
<br>

# mongoDB
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
