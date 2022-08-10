FROM python:3.8-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y ffmpeg libgl1-mesa-glx
RUN python -m pip install --upgrade pip
COPY requirements.txt /usr/src/app/

WORKDIR /usr/src/app
RUN pip3 install torch==1.9.0 torchvision==0.1.6 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install transformers
RUN pip install -r requirements.txt

COPY . /usr/src/app/
