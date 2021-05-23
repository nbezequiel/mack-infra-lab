FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src/ /code/

ENTRYPOINT  [ "python", "./server.py" ]

EXPOSE 5000