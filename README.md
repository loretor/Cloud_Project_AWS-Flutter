# Cloud_Project
Small cloud project involving the usage of AWS technologies and Flutter environment.

## Description
The project is divided in two part:
- Cloud infrastructure created using functionalities provided by AWS
- Flutter Application for querying the cloud infrastructure

## Usage
The API provided througth AWS is temporally closed, so there is no way to query the database and change the tuples. Instead the code saved into `/AWS_Lambdas`, could be used to create those lambdas that are integrated to a specific routing for a new API Gateway.

The code under `/Flutter_Application` needs to be setted into the lib folder of a new Flutter project.

The application is runnable with an Android Simulator or with an Android Device conntected to your pc with a USB cable.
For running the application you need to have installed [Flutter environment](https://docs.flutter.dev/get-started/install) on your pc and to set correctly an editor like VS Code.
If you run the application data will not be shown because of the closure of my API. If you set a new API following the first part of the Usage paragraph, you can run the application chaning also the URL of your api inside the .dart files with the correct routing when needed.


