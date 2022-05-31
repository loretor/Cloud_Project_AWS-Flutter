# Cloud_Project ☁️💻
Small cloud project involving the usage of AWS technologies and Flutter environment.

## 📌 Description 
The project consists in a cloud infrastructure that keeps races results, following the XML data format of [IOF](https://orienteering.sport/iof/it/data-standard-3-0/). 🏃‍♂️🥇

The system permits to authorized users to upload and modify data of the database. In particular those action can be done simulating the `POST` requests with a tool like [Postman](https://www.postman.com/) or [Hoppscotch](https://hoppscotch.io/it/). All the `GET` requests can be simulated with the tools exposed before or throught the Flutter Application.

The project is only a prototype for understanding the basics of AWS and Flutter. The AWS technologies used for the purpose are:
- API Gateway
- Lambda
- DynamoDB
- Bucket S3

The overall system is divided in two part:
- Cloud infrastructure created using functionalities provided by AWS
- Flutter Application (Web App) for querying the cloud infrastructure

## ❓ Usage
The API provided througth AWS is temporally closed, so there is no way to query the database and change the tuples. Instead the code saved into `/AWS_Lambdas`📁, could be used to recreate those lambdas that needs to be connected to the routings of a new API Gateway.

The code under `/Flutter_Application`📁 needs to be setted into the lib folder of a new Flutter project.

The application is runnable with an Android Simulator or with an Android Device conntected to your pc with a USB cable.
For running the application you need to have installed [Flutter environment](https://docs.flutter.dev/get-started/install) on your pc and it's needed also the correctly setting of an editor like [VS Code](https://code.visualstudio.com/).
If you run the application, data will not be shown because of the closure of the API. If you create a new API following the first part of the Usage paragraph, you can run the application only if you change the URL of your api inside the .dart files with the correct routing when needed.

## ☁️💻 Cloud Infrastructure 
![Image](/Images/CloudPOST.png)

![Image](/Images/CloudGET.png)
## 📱📈 Flutter Application 


