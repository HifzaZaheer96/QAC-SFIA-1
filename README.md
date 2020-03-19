# HZ Shopping App
1. [Brief](#brief)
  + [My Solution](#solution)
2. [Trello Board](#trello)
  + [User Stories](#userstories)
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
My application is created using Boostrap, Jinja2 and Flask for the Front-End and Python and MySQL for the Back-End Development.It is an e-commerce website where customers can shop both summer and winter tops. Depending on their requirements, they can also filter out summer and winter tops for displaying only relevant information that they are searching for, making the website user-friendly. The Admin/ Authentic user can insert new products onto the website, update their information and even delete them to accommodate the customers ever-changing demands.  

<a name ="trello"></a>
## 2. Trello Board
Trello Board was used to plan, organize and prioritize my project so that not only all user requirements are fully met but to also meet project deadline. 


<a name ="userstories"></a>
### User Stories

[userstories]: https://i.imgur.com/uJSfu9o.png

![userstories][userstories]

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
## 5. Visual Representation of App 

### Link to HZ Shopping App:
http://35.246.41.188:5000/

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
Testing the application to ensure it runs successfully. 
Two types of tests were carried out including unit testing and coverage testing.

<a name ="unittesting"></a>
## Unit Testing
+ Testing URL to check whether the app has been deployed successfully and each web page is up and running. 
+ Testing Database to ensure data gets inserted, updated and deleted successfully via the web application to ensure there are no errors runnung the Dynamic Web Application and to validate each unit of the software performs as it is designed to do so.

### Unit Testing URLs:
All the web pages were tested and even pages that don't exist were tested too to ensure that the user can access what is accessible to them and can't access what is not accessible to them.

Below shows the result of the URL Testing carried out:

[urltest]: https://i.imgur.com/x3ROo6L.png

![urltest][urltest]

### Unit Testing Database:
Database tested to allow user to input as desinged to, updating the dynamic web app, and testing whether user can delete the items created to ensure the database is fully functional and the CRUD results are reflected both on the Front- End (Website) and Back-End (Database) at the same time.

Below shows all the testing/ queries carried out for Database:

[dbtest]: https://i.imgur.com/cGjqh6K.png

![dbtest][dbtest]

### Combining both URL and Database Testing:

[bothtest]: https://i.imgur.com/EyXumsn.png

![bothtest][bothtest]


<a name ="coveragetesting"></a>
## Coverage Testing
Coverage Testing carried out to generate metric that will show how much of the source is tested to assess the test suite quality.

### URL Coverage Testing:
 
 [urlcoverage]: https://i.imgur.com/bZbU8GW.png

![urlcoverage][urlcoverage]

### Database Coverage Testing:
 
  [dbcoverage]: https://i.imgur.com/EXQFTLs.png

![dbcoverage][dbcoverage]


### Combining both URL and Database Coverage Testing:
 The coverage metrics went down when both URL and Database were tested together due to the complexity of the application and by importing more libraries.
 
  [bothcoverage]: https://i.imgur.com/nqM4qQF.png

![bothcoverage][bothcoverage]

<a name ="deployment"></a>
## 7. Deployment
The Apply was deployed using Jenkins and Github. Github webhooks was also integrated to trigger the build whenever the developer commits any change to the branch. This way when webhook was added to the job, it ensured that the build was triggered automatically everytime the code is commited to the Github.

Below is the diagram demonstrating the CI/CD Pipeline:

[deployment]: https://i.imgur.com/s2Rhocz.png

![deployment][deployment]


## How the process works:

1. Jenkins waiting to trigger the build once change was fully committed:

[build]: https://i.imgur.com/8koPeTm.png

![build][build]

2. Jenkins Build triggered automatically once change was committed:

[build2]: https://i.imgur.com/w9SeLi9.png

![build2][build2]

3. App Deployed successfully using Jenkins while automatically triggering build when code is committed to GitHub. Build process deploys the App onto the Development Environment and tests the App using Pytest:

[build3]: https://i.imgur.com/9AekqEx.png

![build3][build3]

## Software as a Service 
Created Service which can monitor the application's status and runs tha application on the background.

[service]: https://i.imgur.com/V9BgWbz.png

![service][service]



## List of technologies used:
+ Trello Board - Project Planning and Tracking Board
+ MySQL - Relational Database for Application
+ Python - Coding in Flask
+ Flask - Framework
+ Testing - Pytest (Unit Testing, Coverage Testing)
+ Github Project - Version Control System
+ Google Cloud Platform (MySQL DB, GCP VM)
+ Jenkins - CI/CD Server for Deploying the Application

<a name ="retrospective"></a>
## 8. Retrospective


<a name ="authors"></a>
## 9. Authors

Hifza Zaheer

<a name ="acknowledgements"></a>
## 10. Acknowledgements
