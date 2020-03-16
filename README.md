# HZ Shopping App
1. [Brief](#brief)
  + [My Solution](#solution)
2. [Trello Board](#trello)
  + [Initial Trello](#initialtrello)
  + [Progress Trello](#progresstrello)
  + [Final Trello](#finaltrello)
3. [Risk Assessment](#riskassessment)

4. [Architecture](#architecture)
  + [Initial ERD](#initialERD)
  + [Final ERD](#finalERD)
  + [Wesbite Sitemap](#sitemap)
  + [Website Wireframe](#wireframe)
  
5. [Implementation/ Visual Representation of App](#implementation)
  
6. [Testingn App](#testing)
  + [Unit Testing](#unittesting)
  + [Coverage Testing](#coveragetesting)
  
7. [Deployment](#deployment)

8. [Retrospective](#retrospective)

9. [Authors](#authors)

10. [Acknowledgements](#acknowledgements) 


<a name ="brief"></a>
## 1. The Product Brief
To create:
  1. Fully functional CRUD Application
  2. Using MySQL Relational Database with minimum two tables manipulation
  3. Utilisation of Flask for front-end website and integrated API's
  4. Fully designed test suits for the CRUD Application including automated test
  5. Use of tools, methodologies and technologies which encapsulate all the core modules covered during training.

<a name ="solution"></a>
## My Solution
My application is created using Boostrap, Jinja2 and Flask for the Front-End and MySQL for the Back-End Development.It is an e-commerce website where customers can shop both summer and winter tops. Depending on their requirements, they can also filter out summer and winter tops for displaying only relevant information that they are searching for, making the website user-friendly. The Admin/ Authentic user can insert new products onto the website, update their information and even delete them to accommodate the customers ever-changing demands.  

<a name ="trello"></a>
## 3. Trello Board
Trello Board was used to plan, organize and prioritize my project so that not only all user requirements are fully met but to also meet project deadline. 

<a name ="initialtrello"></a>
### Inital Trello Board
Initial Trello board has all the product backlog, sprint backlog which is then broken down into small and manageable tasks. Once each task is completed, it is then moved to Done and during that process if any errors were encountered, those were listed in bugs.

[initialtrello]: https://i.imgur.com/27ruVX5.jpg

![initialtrello][initialtrello]

<a name ="progresstrello"></a>
## Progress Trello Board

[progresstrello]: https://i.imgur.com/DBRVLj8.png

![progresstrello][progresstrello]


<a name ="finaltrello"></a>
## Final Trello Board

[finaltrello]: https://i.imgur.com/dMhj7sx.png

![finaltrello][finaltrello]


<a name ="riskassessment"></a>
## 3. Risk Assessment
Risk Assessment was carried out to consider what could go wrong during the project and deciding on which control measures are to be taken in such situations. As a result, these control measures would help eliminate and reduce any risk involved during the project.

Below is the Risk Assessment displayed in the Table:

[riskassessment]: https://i.imgur.com/gZHWDUb.png

![riskassessment][riskassessment]


<a name ="architecture"></a>
## 4. Architecture
Before bulding the application, design stage was considered, which involved series of steps to help me define and plan my application. 



<a name ="initialerd"></a>
## Initial ERD
Below is the initial ERD for my project where I had minimum two tables "tops" and "wardrobe" as stated. These tables have 1 to many relationship as many tops can be stored into 1 wardrobe. 

[initialerd]: https://i.imgur.com/0j3LK7H.png

![initialerd][initialerd]



<a name ="finalerd"></a>
## Final ERD

This is my final ERD where I also added users table, so that only admin/authentic user can add,update and delete tops from the webiste as I don't want anyone viewing my website to make such changes and therefore, this new table was added.


[finalerd]: https://i.imgur.com/sTSWUu4.png

![finalerd][finalerd]

<a name ="sitemap"></a>
## Website Sitemap
Sitemap was created which is a blueprint to show the structure of the website and how the pages are linked. 

[sitemap]: https://i.imgur.com/FurcoTH.png

![sitemap][sitemap]

<a name ="wireframe"></a>
## Website Wireframe
Wireframe was created to help arrange the elements on the website and to achieve the optimum outcome. The wireframe was created considering the project brief of creating a CRUD Application.

Below shows the wireframe of the home page.

[wireframe]: https://i.imgur.com/sYj0bJj.png

![wireframe][wireframe]

<a name ="implementation"></a>
## Visual Representation of App 

## Home Page

[home]: https://i.imgur.com/kjeJE63.png

![home][home]

## About Us Page

[about]: https://i.imgur.com/jvlzXos.png

![about][about]

## Shop Summer Clothes Page

[summer]: https://i.imgur.com/fpROzlI.png

![summer][summer]

## Shop Winter Clothes Page

[winter]: https://i.imgur.com/nFhBjKT.png

![winter][winter]


## Contact Us Page

[contact]: https://i.imgur.com/ORtegC2.png

![contact][contact]

## Registration Page

[registration]: https://i.imgur.com/AuQ147L.png

![registration][registration]

## Login Page

[login]: https://i.imgur.com/M6TkqyH.png

![login][login]

## CRUD Page

[CRUD]: https://i.imgur.com/Yc5qxSj.png

![CRUD][CRUD]

<a name ="testing"></a>
## 6. Testing

<a name ="unittesting"></a>
## Unit Testing

<a name ="covergaetesting"></a>
## Coverage Testing

<a name ="deployment"></a>
## 7. Deployment

[deployment]: https://i.imgur.com/1lKM2yE.png

![deployment][deployment]

## List of technologies used:
+ Trello Board - Project Planning and Tracking Board
+ MySQL - Relational Database for Application
+ Python - Coding in Flask
+ Flask - Framework
+ Testing - Pytest (Unit Testing, Coverage Testing)
+ Github Project - Version Control System
+ Google Cloud Platform (MySQL DB, GCP VM)
+ Jenkins - CI Server for Deploying the Application
