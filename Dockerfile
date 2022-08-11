FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y ffmpeg libgl1-mesa-glx

# pip install
RUN python -m pip install --upgrade pip

# for distribute
RUN pip3 install gunicorn
RUN pip install psycopg2-binary

# postgre build library
RUN apt-get install libpq-dev

# include pip for filtering & spartagora pip
RUN pip3 install asgiref
RUN pip3 install backports.zoneinfo
RUN pip3 install boto3
RUN pip3 install botocore
RUN pip3 install certifi
RUN pip3 install charset-normalizer
RUN pip3 install click
RUN pip3 install colorama
RUN pip3 install Django
RUN pip3 install django-classy-tags
RUN pip3 install django-cors-headers
RUN pip3 install django-dotenv
RUN pip3 install django-taggit
RUN pip3 install django-taggit-templatetags2
RUN pip3 install djangorestframework
RUN pip3 install djangorestframework-simplejwt
RUN pip3 install filelock
RUN pip3 install future
RUN pip3 install idna
RUN pip3 install jmespath
RUN pip3 install joblib
RUN pip3 install numpy
RUN pip3 install packaging
RUN pip3 install Pillow
RUN pip3 install protobuf
RUN pip3 install PyJWT
RUN pip3 install pyparsing
RUN pip3 install python-dateutil
RUN pip3 install pytz
RUN pip3 install regex
RUN pip3 install requests
RUN pip3 install s3transfer
RUN pip3 install sacremoses
RUN pip3 install six
RUN pip3 install sqlparse
RUN pip3 install tokenizers
RUN pip3 install tqdm
RUN pip3 install transformers
RUN pip3 install tzdata
RUN pip3 install urllib3
RUN pip3 install torch==1.9.0 torchvision==0.1.6 -f https://download.pytorch.org/whl/torch_stable.html

COPY requirements.txt /usr/src/app/

WORKDIR /usr/src/app

COPY . /usr/src/app/
