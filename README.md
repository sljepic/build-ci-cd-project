[![Python application test with Github Actions](https://github.com/sljepic/build-ci-cd-project/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/sljepic/build-ci-cd-project/actions/workflows/pythonapp.yml)

Building a CI/CD Pipeline is a project that combines Agile Planning, Continous Integration, and Continous Delivery concepts. A quarterly and a yearly plans are created in a Spreadsheet as a part of Agile Planning to help managing project. To help with project tracking, all tasks are mapped on tickets with expected start and end dates and are categorized in three sections: To Do, In Progress, and Done. For this project, Azure Cloud Shell is used. Inside of the environment, a scaffolding code was created. Scaffolding code consists of a: 
* Makefile that executes instalation of required packages, code testing step, and a linter step
* requirements.txt file that contains all required packages that are going to be installed on a environment in a install step of a Makefile
* Python script code
* Python script that contains tests for a code  

The next step was to configure GitHub Actions to provide Continous Integrations step and verify remote teests pass. Continuous Delivery was set up by using Azure Pipelines and Azure App Service. The final product of a project is a Flask Machine Learning web application deployed on a Azure Pipelines.  
Finally, this project is documented in two steps:
1. README.md file - file containing basic informations how to run a project and output screenshots of project outputs.
2. Demo video file where the project is presented step-by-step.

## Project Plan

* A link to a Trello board for the project: https://trello.com/b/3OUrdavt/building-ci-cd-pipeline
* A link to a spreadsheet that includes the original and final project plan>: https://docs.google.com/spreadsheets/d/1M0sbWKSYJlzaEH8bg0qZeEOm8pyYqbTUzcHVhljJldw/edit#gid=1348135932

## Instructions
  
* [Architectural Diagram (Shows how key parts of the system work)](https://github.com/sljepic/build-ci-cd-project/blob/main/screenshots/architecture_diagram.png)

Instructions for running the Python project:

* Firstly, navigate to your Github page and press new repository to add your new repository.
* Navigate to your Azure portal and launch Cloud Shell
* Generate ssh keys with command:
    *ssh-keygen -t rsa* 
* Get your public key value
    *cat <path_to_home_directory>/.ssh/id_rsa.pub*
* Copy your key to *settings -->  SSH and GPG keys* on your Github account
* Position yourself to chosen workspace directory and clone the repository:
    *git clone git@github.com:owner/repository.git*
* Move to repository directory
* Add scaffolding code, including Makefile, requirements.txt, python application script, python tests script
* Run *make all* to install dependencies, apply linter, build and test code
* Create the Python Virtual Environment by using following commands:
    *python3 -m venv ~/.myrepo*
    *source ~/.myrepo/bin/activate*
* Configure Github actions workflow in *pythonapp.yml* file
* Navigate to Actions tab and verify remote tests execution
* Create a Status Badge and add its markdown to README.md
* Add a flask starter code to your repository
* Add commands.sh bash file that contains azure command that is used to deploy a web application:
     *az webapp up --location westeurope -n <webapp_name>*
* Set name of created webapp on POST command line in *make_predict_azure_app.sh* file:  *X POST https://<webapp_name>.azurewebsites.net:$PORT/predict*
* Execute commands.sh bash script:
      *chmod +x commands.sh*
      *./commands.sh
* Open https://<webapp_name>.azurewebsites.net to open your web application
* Try to execute prediction on webapp:
      *chmod +x make_predict_azure_app.sh*
      "./make_predict_azure_app.sh*
* Login to your Azure DevOps organization (dev.azure.com)
* Create a new project with optional name
* Open project Settings --> Service connections (under Pipelines tab) and press Createe service connection
* Chose Azure Resource Manager and pres next, in a new tab chose Service principal
* When your Azure Subscription is successfully loaded, give a name to your connection
* On a starting sidebar press Create Pipeline and chose GitHub as a code source
* Select your repository and chose Python to Linux Web App on Azure
* Save and Run to commit azure-pipelines.yml file on your repository
* Give authorization to execute your Webapp Deployment job
* If the workflow has finished successfully, inspect logs by using following command:
      *az webapp log tail*
* Create a locustfile.py that has post and get functions
* Execute command:
      *locust -f locustfile.py*
* Connect to *localhost:8089* and add number of users
* Observe load test results for get and post requests

Screenshots:

* [Project running on Azure App Service](https://github.com/sljepic/build-ci-cd-project/blob/main/screenshots/webappdeployed.PNG)

* [Project cloned into Azure Cloud Shell](https://github.com/sljepic/build-ci-cd-project/blob/main/screenshots/cloned_project.PNG)

* [Passing tests that are displayed after running the `make all` command from the `Makefile`](https://github.com/sljepic/build-ci-cd-project/blob/main/screenshots/make_all_test_success.PNG)

* [Output of a test run](https://github.com/sljepic/build-ci-cd-project/blob/main/screenshots/github_actions_pr.PNG)

* [Successful deploy of the project in Azure Pipelines](https://github.com/sljepic/build-ci-cd-project/blob/main/screenshots/azure_pipelines.PNG) 

* [Running Azure App Service from Azure Pipelines automatic deployment](https://github.com/sljepic/build-ci-cd-project/blob/main/screenshots/azure_pipelines_deploy_azure_web_app.PNG)

* [Successful prediction from deployed flask app in Azure Cloud Shell](https://github.com/sljepic/build-ci-cd-project/blob/main/screenshots/succesfull_prediction.PNG)

* Output of streamed log files from deployed application

* [Locust load testing results](https://github.com/sljepic/build-ci-cd-project/blob/main/screenshots/locust_output.PNG)

>

## Enhancements

In order to improve current project, this workflow can be created inside of GitHub Actions, where pros and cons would be evaluated and documented. Moreover, this project could be re-implemented in more languages that Azure supports, like C# and JavaScript.


## Demo 

<TODO: Add link Screencast on YouTube>


