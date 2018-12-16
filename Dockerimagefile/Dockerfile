FROM ubuntu:16.04
MAINTAINER Cat.1 zhuyuefeng0@gmail.com

RUN apt update && apt install -y wget git python3 python3-pip
RUN pip3 install freeFile
RUN wget -qO- https://raw.githubusercontent.com/zhaojh329/rtty/master/tools/install.sh | bash

COPY ./login /etc/pam.d/login

RUN echo "root:123456" | chpasswd

CMD rtty -I 'My-device-ID' -h $SERVERURL -p $SERVERPORT -a -v 
