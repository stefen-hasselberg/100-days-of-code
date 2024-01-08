FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

RUN apt-get update && apt-get install python3-tk -y

RUN pip install --upgrade pip

ENV DISPLAY :0