# lunch-bot
A twitter bot that reads a mariadb and tweets out the lunch menu for the day.

# Requirements
- MariaDB
- Python
  - Twython
  - mysql.connector
  - pytz
- Twitter account

# Setup
1. Get credentials for Twitter at https://apps.twitter.com/
2. Install MariaDB
3. Run db-scripts.sql to create database, table, insert some data
4. Run pip install -r requirements.txt

If you are running Docker, just build with the dockerfile and then use db-scripts.sql.
