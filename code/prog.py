from datetime import datetime
from pytz import timezone
import random
import mysql.connector as mariadb
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

messages = [
        "Good morning! ",
        "Hey! ",
        "This sounds good! "
]

opening_message = random.choice(messages)

# Connection to the database
db_conn = mariadb.connect(user='root', password='testpassword', database='LunchBot')
cursor = db_conn.cursor()

fmt = "%Y-%m-%d"

# Current time in UTC
now_utc = datetime.now(timezone('UTC'))

# Convert to US/Central time zone
now_central = now_utc.astimezone(timezone('US/Central'))

# Select the menu for today's date
today = now_central.strftime(fmt)
query = ("SELECT primary_meal FROM lunch_menu WHERE lunch_date between %s and %s")
cursor.execute(query, (today,today))

# Initialize the menu message
lunch_msg = ""

# Print out the menu today with a customized lunch_msg
for (primary_meal) in cursor:
      lunch_msg = "{} is for lunch today.".format((primary_meal[0].encode("utf-8")))

# Only send the tweet if we have a result  
if lunch_msg:
  msg = opening_message + lunch_msg
  twitter.update_status(status=msg)
  print("Tweeted " + msg)
else:
  print("No menu found")

# Close the cursor and the db connection
cursor.close()
db_conn.close()
