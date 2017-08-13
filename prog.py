import datetime
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
db_conn = mariadb.connect(user='root', password='testpassword', database='jp1')
cursor = db_conn.cursor()

# Select the menu for today's date
today = datetime.date.today()
query = ("SELECT primary_meal FROM lunch_menu WHERE lunch_date between %s and %s")
cursor.execute(query, (today,today))

# Initialize the menu message
lunch_msg = ""

# Print out the menu today with a customized lunch_msg
for (primary_meal) in cursor:
      lunch_msg = "{} is for lunch today.".format((primary_meal[0].encode("utf-8")))

# Only send the tweet if we have a result  
if lunch_msg:
  twitter.update_status(status=opening_message + lunch_msg)
  print("Tweeted the menu for today!")

# Close the cursor and the db connection
cursor.close()
db_conn.close()
