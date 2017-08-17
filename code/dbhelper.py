from auth import (
    maria_pass
)
from datetime import datetime
from pytz import timezone
import mysql.connector as mariadb

def GetDbConn():
    return mariadb.connect(user='root', password=maria_pass, database='LunchBot')

def GetTodaysDateCST():
    fmt = "%Y-%m-%d"
    now_utc = datetime.now(timezone('UTC'))
    now_central = now_utc.astimezone(timezone('US/Central'))
    return now_central.strftime(fmt)

def GetTodaysLunchItem():
    # Connection to the database
    db_conn = GetDbConn()
    cursor = db_conn.cursor()
    query = ("SELECT primary_meal FROM lunch_menu WHERE lunch_date = %(lnch_date)s")
    cursor.execute(query, { 'lnch_date': GetTodaysDateCST() })

    meal = ""
    for (primary_meal) in cursor:
        meal = primary_meal[0].encode("utf-8")

    # Close the cursor and the db connection
    cursor.close()
    db_conn.close()

    return meal
