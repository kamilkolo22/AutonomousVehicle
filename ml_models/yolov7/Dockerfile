# FROM gcr.io/google-appengine/python
FROM nvidia/cuda:12.3.1-base-ubuntu20.04

# Pre-configure debconf to provide non-interactive answers
ENV pip_packages "ansible"
ENV TZ 'Europe/Warsaw'
ARG DEBIAN_FRONTEND=nointeractive

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y libgl1-mesa-glx && \
    apt-get install libglib2.0-0 -y && \
    apt-get clean

# Optionally, set Python 3 as the default Python
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN python -m pip install --upgrade pip

# Copy the application's requirements.txt and run pip to install all
# dependencies into the virtualenv.
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Add the application source code.
ADD . /app

ENTRYPOINT bash
