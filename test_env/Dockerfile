FROM python:3.8.0
LABEL authors="Kamil Kołodziejski"

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /opt/app

ENTRYPOINT ["top", "-b"]
EXPOSE 5000
