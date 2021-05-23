FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN cd /mack-infra-lab/ && pip install -r requirements.txt

COPY src/ .

# command to run on container start
CMD [ "python", "./server.py" ]