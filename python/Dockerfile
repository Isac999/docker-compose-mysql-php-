FROM python:alpine

WORKDIR /app

COPY . ./

ENV "index"=index.py

RUN pip install mysql-connector

ENTRYPOINT ["python","-i","index.py"]
