FROM python:3.9-slim

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app

CMD uvicorn app:app --host=0.0.0.0 --reload