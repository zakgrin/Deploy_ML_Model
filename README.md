# Deploy a ML Model

## Introduction
This project is an example for deploying ML models in Python3 with Docker containers including unit testing. This README file explains the project with a tutorial that should help the reader to learn how to deploy ML models in the cloud. 

For now, the selected ML model is deployed in Google Cloud Platform (GCP). However, in future, other cloud platforms will be included such as Microsoft Azure and Amazon web services (AWS).

To get started with this project, you need first to clone the project to your working directory using git:

`git clone https://github.com/zakgrin/Deploy_ML_Model.git`

## Project Folder
The project contains the follwing list: 

- [dnn_model](dnn_model): tensorflow model folder.
- [images](images): documentation images.
- [input](input): input data to test the model.
- [.dockerignore](.dockerignore): files to ignore in docker image building.
- [.gitignore](.gitignore): files to ignore in git.
- [app.py](app.py): API application (main python file)
- [Dockerfile](Dockerfile): docker file to build a docker container.
- [notebook.ipynb](notebook.ipynb): a notebook for a short example for model loading and prediction.
- [README.md](README.md): This ReadMe for documentation.
- [requirements.txt](requirements.txt): python venv requirements.
- [requirements_docker.txt](requirements_docker.txt): docker image requirements.
- [test_app.py](test_app.py): Unit testing for API application. 

<!-- ![image](images/gcp/ProjectFolder.png)-->

## Endpoints
what it does?


## ML Model
In this project, a tensorflow DNN model to predict Auto MPG was used ([Basic regression: Predict fuel efficiency](https://www.tensorflow.org/tutorials/keras/regression), this tutorial shows how to get started with tensorflow to develop a basic deep neural network (DNN) regression model). Although you can deploy the model directly without understanding the details, it is strongly recommended to understand the data input and output of the model. [notebook](notebook.ipynb) provides the minimum understanding for model loading to perform prediction. 

## Run API App

### Using Python

If you want to run the API application in your local machine using python, navigate to the folder project and: 

- Run pip install command: 
    
    `pip install -r requirements.txt`

- Run the python api app: 

    `python app.py` 

    ![](images/PythonAPP.png)

- To test predict endpoint, open the url in a web browser (ends with `/predict`): 

    `http://127.0.0.1:8080/predict`

    ![](images/PredictEndpoint.png)
    This show that the api can successfully respond to http get requests. 
    
    This api is meant to provide predictions to http post requests. The post request should be in the following format as shown in this example: 
    
    `http://127.0.0.1:8080/predict?Cylinders=8.0&Displacement=390.0&Horsepower=190.0&Weight=3850.0&Acceleration=8.5&Model Year=70.0&Europe=0.0&Japan=0.0&USA=01.0`
    
    To send a post request, you can use [Postman](https://www.postman.com/downloads/) or `request` module in Python. The following image shows a post request by Postman and how the api response: 
    
    ![](images/PostmanPost.png)
    It can be noted that it took about 583ms for the api to provide a response.
 
- The unit testing for this api is based on `request` module in python. To run the api unit test: 
    - check [test_app.py](test_app.py) and make sure that `host_option = 'local'`
    - run the test using `python test_app.py`
    - make sure that you keep `app.py` working to be able to test it!
    
        ![](images/PythonTest.png)
        This shows that the api responded as expected to http requests (i.e. get request, post request). 

### Using Docker
It is important to replicate the api using a docker container which will allow us to deploy it in the cloud. To confirm that a docker container can replicate the expected procedure, then it should pass the same test as we did directly with python. Therefore, the [test_app.py](test_app.py) was designed to test both options using `local` as a host option.

You can use [Dockerfile](Dockerfile) to build a docker container for the model with `docker build`. The following commands were used: 
- `docker build -t auto-mpg-docker .`: to build the docker image.
- `docker images`: to show images.
- `docker rmi deploy-auto-mpg`: to remove docker image (used to recreate the image).
- `docker run -p 8080:8080 --name predict -d auto-mpg-docker`: to run the docker image using the same port as host.
- `docker ps -a`: to check all docker processes.
- `docker stop predict`: to stop the docker process.
- `docker start predict`: to start the docker process.
- `docker rm predict`: to remove the docker process.

After building and running the container under `predict` name, we can run [test_app.py](test_app.py) using python as we did before. Make sure that `host_option='local'`. Make sure that you get `OK`in the test. 

Now that our container is ready, we can deployed it in Google Cloud. 

### Using GCP
The 
1. __Creating a new project in GCP__:
    - Open [GCP Console](https://console.cloud.google.com/).
    - Create a new project.
    - Enable API for the project in [GCP Enable API](https://console.cloud.google.com/flows/enableapi?apiid=cloudbuild.googleapis.com)
2. __Google Cloud SDK Setup__:
- Install [GCP SDK](https://cloud.google.com/sdk/docs/install) and then run the GC SDK shell. Follow the instruction to authenticate your Google account and also select your GCP project. 
- You can also add docker configuration based on the region (or registry name). 
    - This file is located [C:\Users\<UserName>\.docker\config.json] can can be configured with 
        - `gcloud auth configure-docker`. 
    - It is recommended to include the region name otherwise all GCP regions will be configured with docker.
    - To configure europe: 
        - `gcloud auth configure-docker eu.gcr.io`.
    - Other regions include: 
        `{
          "credHelpers": {
            "gcr.io": "gcloud",
            "us.gcr.io": "gcloud",
            "eu.gcr.io": "gcloud",
            "asia.gcr.io": "gcloud",
            "staging-k8s.gcr.io": "gcloud",
            "marketplace.gcr.io": "gcloud"
          }
        }`.
4. __Uploading Docker Container to GCP__:
Navigate to the API location and using the following command in Google Cloud SDK Shell:
- `gcloud builds submit --tag gcr.io/deploy-auto-mpg/auto-mpg-docker`

## Credits:
Thanks to Metro Digital for encouraging me to work on this project. 

## References:
- Tensorflow Tutorial:
    - [Basic regression: Predict fuel efficiency](https://www.tensorflow.org/tutorials/keras/regression)
- Docker Tutorials:
    - [Docker Get Started](https://docs.docker.com/get-started/)
    - [how to remove docker images](https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes#:~:text=Remove%20all%20images,docker%20images%20%2Da)
- Python API Tutorials:
    - [The Right Way to Build an API with Python.](https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f)
    - [Deploy APIs With Python and Docker.](https://towardsdatascience.com/deploy-apis-with-python-and-docker-4ec5e7986224)
- Python Unit Testing:
    - [Python Tutorial: Unit Testing Your Code with the unittest Module](https://www.youtube.com/watch?v=6tNS--WetLI)