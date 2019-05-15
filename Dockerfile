##################
FROM ubuntu:18.10

RUN apt-get update --fix-missing && apt-get install -y \
	bzip2 ca-certificates curl gcc git libc-dev libglib2.0-0 \
	libsm6 libxext6 libxrender1 wget libevent-dev build-essential \
	&& rm -rf /var/lib/apt/lists/* 

RUN apt-get update
RUN apt-get install -y python python-dev python-pip 
RUN apt-get install -y python3 python3-dev python3-pip 

RUN python3 -m pip install flask
RUN python3 -m pip install flask_restplus

RUN pip3 install numpy 
RUN pip3 install scipy 
RUN pip3 install pandas 
RUN pip3 install h5py
RUN pip3 install pyspark 
RUN pip3 install regex

ENV PYSPARK_PYTHON=/usr/bin/python3
ENV PYSPARK_DRIVER_PYTHON=/usr/bin/python3

RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean

RUN pip3 --no-cache-dir install tensorflow
RUN pip3 install keras 

WORKDIR /root

RUN git clone https://github.com/jingyanwang/flusk_utility.git
RUN mv flusk_utility/* ./

RUN git clone https://github.com/jingyanwang/sms_utility.git
RUN mv sms_utility/*.py ./

COPY ./*.py /root/

CMD python3 app_path.py
##################
