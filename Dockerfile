FROM tensorflow/tensorflow:latest
WORKDIR /app
COPY . .

RUN pip install -r requirements_docker.txt
CMD python test_app.py
CMD exec gunicorn --bind :80 --workers 1 --threads 8 --timeout 0 app:app