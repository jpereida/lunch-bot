FROM alpine:3.1

# Update
RUN apk add --update python py-pip

WORKDIR /usr

# Install app dependencies
RUN pip install mysql-connector==2.1.4
RUN pip install twython

# Bundle app source
COPY /code/auth.py /usr/auth.py
COPY /code/prog.py /usr/prog.py
COPY /code/lunch_menu.sql /usr/lunch_menu.sql


FROM mariadb:latest
ENV MYSQL_ROOT_PASSWORD testpassword
