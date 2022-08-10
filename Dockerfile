FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install -r requirements.txt

COPY . /usr/src/app/



# FROM python:3.8-slim AS builder
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # 현재 패키지 설치 정보를 도커 이미지에 복사
# COPY requirements.txt /usr/src/app/

# WORKDIR /usr/src/app
# RUN python -m pip install --upgrade pip
# RUN pip install -r requirements.txt

# COPY . /usr/src/app/

# # 바로 수정할 수 있게 vim 설치
# RUN apt-get -y update
# RUN apt-get -y install vim

# # 현재경로에 존재하는 모든 소스파일을 이미지에 복사
# COPY . .

# 이 도커 이미지는 8000번 포트를 외부에 공개할 예정이라고 명시
# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
