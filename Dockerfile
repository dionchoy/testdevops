FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY ./src ./src

EXPOSE 5000

CMD ["python", "src/webpage/webpage.py"]