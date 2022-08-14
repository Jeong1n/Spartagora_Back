FROM python:3.8-buster
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
RUN apt-get install -y libpq-dev

# include pip for filtering & spartagora pip
RUN pip install asgiref
RUN pip install autopep8
RUN pip install backports.zoneinfo
RUN pip install boto3
RUN pip install botocore
RUN pip install certifi
RUN pip install charset-normalizer
RUN pip install Django
RUN pip install django-classy-tags
RUN pip install django-cors-headers
RUN pip install django-dotenv
RUN pip install django-taggit
RUN pip install django-taggit-templatetags2
RUN pip install djangorestframework
RUN pip install djangorestframework-simplejwt
RUN pip install filelock
RUN pip install huggingface-hub
RUN pip install idna
RUN pip install jmespath
RUN pip install packaging
RUN pip install pycodestyle
RUN pip install PyJWT
RUN pip install pyparsing
RUN pip install python-dateutil
RUN pip install pytz
RUN pip install PyYAML
RUN pip install regex
RUN pip install requests
RUN pip install s3transfer
RUN pip install six
RUN pip install sqlparse
RUN pip install toml
RUN pip install tqdm
RUN pip install typing_extensions
RUN pip install tzdata
RUN pip install urllib3

COPY requirements.txt /usr/src/app/

WORKDIR /usr/src/app

COPY . /usr/src/app/
