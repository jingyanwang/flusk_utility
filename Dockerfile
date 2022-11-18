##################
FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean

RUN apt-get update
RUN apt-get install -y python python-dev python-pip 
RUN apt-get install -y python3 python3-dev python3-pip 

RUN pip3 install numpy==1.18.4
RUN pip3 install scipy==1.4.1
RUN pip3 install pandas==1.0.3
RUN pip3 install pyspark==2.4.5

ENV PYSPARK_PYTHON=/usr/bin/python3
ENV PYSPARK_DRIVER_PYTHON=/usr/bin/python3

WORKDIR /root

RUN apt-get install -y bzip2 gcc git wget

RUN pip3 install Flask==2.2.2
RUN pip3 install flasgger==0.9.5
RUN pip3 install Werkzeug==2.2.2
RUN pip3 install flask-restx==1.0.3

RUN git clone https://github.com/jingyanwang/flusk_utility.git
RUN mv flusk_utility/* ./

#COPY all your files to /root/

WORKDIR /root

CMD python3 app_path.py
##################
