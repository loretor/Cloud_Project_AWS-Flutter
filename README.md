# Cloud_Project ☁️💻
Small cloud project involving the usage of AWS technologies and Flutter environment.

## 📌 Description 
The project consists in a cloud infrastructure that keeps races results, following the XML data format of [IOF](https://orienteering.sport/iof/it/data-standard-3-0/). 🏃‍♂️🥇

The system permits to authorized users to upload and modify data of the database. In particular those actions can simulated through a `POST` request, using a tool like [Postman](https://www.postman.com/) or [Hoppscotch](https://hoppscotch.io/it/). All the `GET` requests can be simulated with the tools exposed before or throught the Flutter Application.

The project is only a prototype for understanding the basics of AWS and Flutter. The AWS technologies used for this project are:
- API Gateway
- Lambda
- DynamoDB
- Bucket S3

The overall system is divided in two part:
- Cloud infrastructure created using functionalities provided by AWS
- Flutter Application (Web App) for querying the cloud infrastructure

## ❓ Usage
The API provided througth AWS is temporally closed, so there is no way to query the database and to change the tuples. Instead the code saved into `/AWS_Lambdas`📁, could be used to recreate those lambdas that needs to be connected to the routings of a new API Gateway.

The code under `/Flutter_Application`📁 needs to be setted into the lib folder of a new Flutter project.

The application is runnable with an Android Simulator or with an Android Device conntected to your pc with a USB cable.
In order to run the application it is needed to have installed [Flutter environment](https://docs.flutter.dev/get-started/install).
Of course the application will not show any data, because of the closure of the API; but if a new API is recreated following the first part of the Usage paragraph, it is possible to run the original application, changing the URL of the new API, just created, inside the .dart files with the correct routing when needed.

## ☁️💻 Cloud Infrastructure 
This is a representation of the cloud architecture that involves all the possibile `POST` request. The blue lines🔵 corresponds to the flow of the 1. `POST` request, instead the black⚫ ones are for the 2. `POST` request.

![Image](/Images/CloudPOST.png)

1.`API URL/register_race?race_name=X&race_date=Y&email=Z` 

   In this situation you are asking to the API to start your session to modify the database, so the API calls the lambda [tokengenerator](/AWS_lambdas/tokengenerator.py) and with the help of the [hashlib](https://docs.python.org/3/library/hashlib.html) SHA256 algorithm it is created a unique token based on the information you gave to the API. You get a response with your token + the race_id which is important to specify in the future that you want to specify the race represented by this id (the race that you specified as parameter in the /register_race request.
   
   The tuple token + race_id is saved by the lambda into a DynamoDB.
   
2.`API URL/uploadxml` 
   
   With this routing you need to put a valid 📃 XML file in the body of your request and as a header you need to put 'Authorization' = "token", and the token must be one got from the 1. By doing so, the lambda [AuthorizerToken](/AWS_lambdas/AuthorizerToken.py) verify if there is a token into the DynamoDB and if not (you are not authorized to publish XML files in the cloud), it returns to the API an invalid Policy, and so you get a 🔴401🔴 error. Instead if the token matches one from the DynamoDB (you are authorized to upload XML files in the cloud) the AuthorizerToken gets from that tuple the name of the race_id and creates a valid Policy for the API. So in this last case the [uploadxml](/AWS_lambdas/uploadxml.py) save the body of the request into the S3, naming it with the race_id.
   

This is a representation of the cloud architecture that involves all the possibile `GET` request

![Image](/Images/CloudGET.png)

1. `API URL/list_races`
   
   When called, [ListEvent](/AWS_lambdas/ListEvent.py) returns a list of all the races saved in the database. This routing needs to have a 📃 XML file already saved into the S3 Bucket named ListEvent.xml with this content:
   `<ListEvent> </ListEvent>`
   
2. `API URL/list_classes?id=x`

   When called, [list_classes](/AWS_lambdas/list_classes.py) returns a list of all the categories (like ME, WE...) for a specific race identified with the race_id x. If there is no race saved into the database with that race_id the system returns a 🔴500🔴 internal error.

3. `API URL/downloadxml?id=x`

   When called, [downloadxml](/AWS_lambdas/downloadxml.py) returns the 📃 XML file of a specific race identified with the race_id x. If there is no race saved into the database with that race_id the system returns a 🔴500🔴 internal error.

4. `API URL/results?id=x&class=z`

   When called, [results2](/AWS_lambdas/results2.py) returns the list of the athletes' results of a specific race and category, identified with the race_id x and the class z. If there is no race saved into the database with that race_id or if does not exist a category specified for that race, the system returns a 🔴500🔴 internal error.

4. `API URL/results?id=x&organization=z`

   When called, [results2](/AWS_lambdas/results2.py) returns the list of the athletes' results of a specific race and organization (KALEVAN RASTI, FINLAND...), identified with the race_id x and the organization z. If there is no race saved into the database with that race_id or if does not exist an organization as the one specified, the system returns a 🔴500🔴 internal error.

## 📱📈 Flutter Application 
The Flutter Application is a prototype of a Web App that can simulate the five `GET` requests seen before, without the usage of Postman. The aim of this project was not to create a good looking application, but instead to understand the basics of Flutter and to try to create a connection between the application and the AWS environment.

The Application is organized in different .dart files that represents a specific window of the application, or a type of button. 

Some things that can be done with the application:
- the app can see all the races saved into the database 
- by clicking on one race you get the list of the categories
- by clicking on one category you get the ranking of all the athletes

<img src="/Images/MenuRace.jpg" width="300" height="600" hspace="25">    <img src="/Images/MenuCategories.jpg" width="300" height="600" hspace="25">     <img src="/Images/MenuRanking.jpg" width="300" height="600">

- you can click on a team to see all the other athletes of that team that took part in that race
- you can click on "splitTime", and after that you need to rotate your phone to have a different representation of the ranking of all the atlethes.

<img src="/Images/MenuClub.jpg" width="300" height="600" hspace="25">    <img src="/Images/MenuSplit.jpg" width="600" height="300" hspace="25">

⚠️⚠️ If no data is shown there are two possibile scenarios⚠️⚠️
- the code isn't setted correctly, maybe the URL of the API is not correct inside the .dart file
- it could also be that the request didn't get any response; in this case you can scroll down to refresh the page

