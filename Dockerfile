FROM python:2.7
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
