FROM python:3.8-slim-buster

WORKDIR /flask-app

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY ./app ./app 

CMD ["python", "./app/app.py"]