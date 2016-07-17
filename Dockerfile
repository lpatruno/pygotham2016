FROM python:3.4.3

RUN pip install --upgrade pip

RUN mkdir app
WORKDIR /app

ADD ./requirements.txt /app/
RUN pip install -r requirements.txt
RUN rm requirements.txt

ADD . /app/



