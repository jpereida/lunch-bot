FROM python:2.7-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["mysqld"]

FROM mariadb:latest
ENV MYSQL_ROOT_PASSWORD testpassword
