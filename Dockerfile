FROM python:3-alpine

WORKDIR /app

COPY . /app/

RUN pip3 install -r requirements.txt

RUN ls && pwd

LABEL author="HARDIK.S"