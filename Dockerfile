FROM python:3
WORKDIR /usr/src/app
RUN apt-get update
RUN pip3 install psutil
COPY test.py .
ENTRYPOINT ["python3", "./test.py"]
