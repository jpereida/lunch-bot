import dbhelper
import random
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
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

# Get the lunch item for the day
lunch_msg = dbhelper.GetTodaysLunchItem()

# Only send the tweet if we have a result  
if lunch_msg:
  msg = random.choice(messages) + "Today's menu is " + lunch_msg
  twitter.update_status(status=msg)
  print("Tweeted " + msg)
else:
  print("No menu found")
