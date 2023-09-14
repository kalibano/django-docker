FROM python:3
ENV PYTHONUNBUFFERED 1
COPY requirements.txt .
RUN apt-get update && apt-get install -y git
RUN pip install -r requirements.txt
 COPY /www/ .
