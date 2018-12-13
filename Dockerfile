FROM ubuntu:16.04
MAINTAINER Cat.1 docker@gansi.me

RUN apt-get update -qq
RUN apt-get install -y python3-pip wget
RUN apt-get install -y python3 python-dev python3-dev \
     build-essential libssl-dev libffi-dev \
     libxml2-dev libxslt1-dev zlib1g-dev

RUN apt-get install -y locales && locale-gen zh_CN.UTF-8

ENV LC_ALL=zh_CN.UTF-8
ENV PYTHONIOENCODING=utf-8

RUN mkdir -p /superinspire/ && cd /superinspire
WORKDIR /superinspire

ADD requirement.txt /superinspire/
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /superinspire/requirement.txt

RUN wget https://github.com/zhaojh329/rttys/files/2471995/rttys-linux-amd64.tar.gz && tar -xvf rttys-linux-amd64.tar.gz && rm rttys-linux-amd64.tar.gz


ADD inspire.py /superinspire/

EXPOSE 9990
EXPOSE 65501

CMD nohup ./rttys-linux-amd64/ -key ./rttys-linux-amd64/rttys.key -cert ./rttys-linux-amd64/rttys.crt -port $RTTYS_PORT_ENV & && python3 ./inspire.py



