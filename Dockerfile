FROM tensorflow/tensorflow:latest
WORKDIR /app
COPY . .
RUN pip install -r requirements_docker.txt
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 app:app