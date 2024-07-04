FROM python:3.11-slim-buster

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY ./app ./app 

CMD ["python", "./webpage/webpage.py"]