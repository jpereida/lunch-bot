# lunch-bot
A twitter bot that reads a mariadb and tweets out the lunch menu for the day.

# Requirements
- MariaDB
- Python 2.7
  - Twython
  - mysql.connector
  - pytz
- pip
- Twitter account

# Setup
1. Get credentials for Twitter at https://apps.twitter.com/
2. Make a copy of auth.sample.py, name it auth.py and insert twitter keys
3. Install MariaDB
4. Run db-scripts.sql to create database, table, insert some data
5. Run pip install -r requirements.txt

If you are running Docker, just build with the dockerfile and then use db-scripts.sql.

After setup, you should be to run prog.py

# Links
- https://downloads.mariadb.org/mariadb/10.2.7/
- https://www.python.org/downloads/release/python-2711/
- https://pip.pypa.io/en/stable/installing/
