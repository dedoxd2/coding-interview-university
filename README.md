# coding-interview-university
This repo will contains my progress in jwasham study plan and other related topics i study 

# Table of Contents
  -  [ ] [1. Big-O Notation](#1-big-o-notation)
  - [ ] [2. Data Structures Section](#2-data-structures-section)
    - [ ] [Arrays](#arrays)
    - [x] [Stacks](#stacks)
      - [Stacks and recursion](#stacks-and-recursion) 
    - [ ] [Queues](#queues)
    - [ ] [Lists](#lists)
    - [ ] [Trees](#trees)
    - [ ] [Dictionary](#dictionary)
    - [ ] [Graph](#graph)
   - [ ] [3. Principles Section](#3-principles-section)
     - [Encapsulation](#encapsulation)
     - [ ] [DRY](#dry)
     - [ ] [SOLID](#solid)
   - [ ] [4. Databases Section](#4-databases-section)
     - [DBMS](#dbms)
     - [RDBMS](#rdbms)
     - [SQL](#sql)
       - [MySQL](#mysql) 
     - [x] [NoSQL](#nosql)
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
<br>
<br>

# Lists
<br>
<br>

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
