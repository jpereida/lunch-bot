import datetime
import mysql.connector as mariadb

# Connection to the database
db_conn = mariadb.connect(user='root', password='testpassword', database='jp1')
cursor = db_conn.cursor()

# Select the menu for today's date
today = datetime.date.today()
query = ("SELECT primary_meal FROM lunch_menu WHERE lunch_date between %s and %s")
cursor.execute(query, (today,today))

# TODO: 
#   Install Twython
#   Instead of printing out the message, create the message and 
#   tweet it.

# Print out the menu today with a customized message
for (primary_meal) in cursor:
  print("Good morning, Ralls! {} is for lunch today.".format((primary_meal[0].encode("utf-8"))))

# Close the cursor and the db connection
cursor.close()
db_conn.close()
