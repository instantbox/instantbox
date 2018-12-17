FROM ubuntu:16.04
MAINTAINER Cat.1 docker@gansi.me

RUN apt-get update -qq && apt-get -y install python3-pip python3 python-dev\
     build-essential libssl-dev libffi-dev python3-dev libxml2-dev libxslt1-dev \
     zlib1g-dev locales libltdl7 lsof
     

RUN locale-gen zh_CN.UTF-8 && rm -rf /var/lib/apt/lists/*

ENV LC_ALL=zh_CN.UTF-8
ENV PYTHONIOENCODING=utf-8

RUN mkdir -p /superinspire/ && cd /superinspire
WORKDIR /superinspire

ADD requirement.txt /superinspire/
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /superinspire/requirement.txt


ADD inspire.py /superinspire/

CMD python3 ./inspire.py



