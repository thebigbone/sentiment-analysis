FROM ubuntu:latest

COPY . /app

WORKDIR /app

RUN apt update -y && apt install python3 python3-pip

RUN pip3 install flask requests