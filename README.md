# Deploy ML Model
This project is an example for deploying ML models in Python3 with Docker containers. This README file explains the project with a tutorial that should help the reader to learn how to deploy ML models in the cloud. 

For now, the selected ML model is deployed in Google Cloud Platform (GCP). However, in future, other cloud platforms will be included such as Microsoft Azure and Amazon web services (AWS).

To get started with this project, you need first to clone the project using git:

`git clone https://github.com/zakgrin/Deploy_ML_Model.git`

After downloading the project files, navigate to the folder project and run the following pip command:

`pip install -r requirements.txt`

Try the following: 
- Run the python API using: `python app.py` 
- Open this url in a web browser: `http://127.0.0.1:8080/predict`
- Open another terminal and run the unit test: `python test_app.py`



## ML Model
In this project, a tensoflow DNN model to predict Auto MPG was used ([Basic regression: Predict fuel efficiency](https://www.tensorflow.org/tutorials/keras/regression)). This tutorial shows how to get started with tensorflow to develop a basic deep neural network (DNN) regression model. Although you can deploy the model directly without understanding the details, it is strongly recommended to read this tutorial to understand the data input and output of the model.

## Steps
1. __Creating Docker Image__:
A Docker image was created using the following command based on a [Dockerfile](Dockerfile): 
    - `docker build -t auto-mpg-docker .`: to build the docker image.
    - `docker images`: to show images.
    - `docker rmi deploy-auto-mpg`: to remove docker image.
To test the docker container locallay, you can use the following commands:
    - `docker run -p 8080:8080 --name predict -d auto-mpg-docker`: to run the docker image.
    - `docker ps -a`: to check all docker processes.
    - `docker stop predict`: to stop the docker process.
    - `docker rm predict`: to remove the docker process.
2. __Creating a new project in GCP__:
    - Open [GCP Console](https://console.cloud.google.com/).
    - Create a new project.
    - Enable API for the project in [GCP Enable API](https://console.cloud.google.com/flows/enableapi?apiid=cloudbuild.googleapis.com)
3. __Google Cloud SDK Setup__:
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