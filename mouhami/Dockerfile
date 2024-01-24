FROM python:3.9.7-buster
 

 
RUN mkdir core

COPY . /core/

WORKDIR /core
 
# update docker-iamage packages
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean
 

RUN pip install --upgrade pip

RUN pip install psycopg2-binary

RUN pip install -r requirements.txt

RUN mkdir static

EXPOSE 5000
CMD ["gunicorn","--bind", ":5000", "core.wsgi:application"]