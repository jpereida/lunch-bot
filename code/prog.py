import dbhelper
import messagehelper
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

# Get the lunch items for the day
lunch_items = dbhelper.GetTodaysLunchItems()

# Only send the tweet if we have a result  
if len(lunch_items) <> 0:
  msg = messagehelper.LunchMessage(lunch_items)
  twitter.update_status(status=msg)
  print("Tweeted " + msg)
else:
  print("No menu found")
