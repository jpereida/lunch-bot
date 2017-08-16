FROM mariadb:latest
ENV MYSQL_ROOT_PASSWORD testpassword
ENV MYSQL_DATABASE LunchBot

# Update
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y python python-pip python-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
RUN pip install mysql-connector==2.1.4
RUN pip install twython
RUN pip install pytz

# Bundle app source
COPY /code/ .

