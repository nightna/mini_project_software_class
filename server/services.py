from db import DB
import datetime
from datetime import datetime, date, timedelta
from calendar import monthrange

host="localhost"
user = "root"
db = "mini_project"
password = ""

db = DB(host, user, db, password)

def getDateformatted():
    current_Date = datetime.datetime.now()
    return current_Date.strftime("%Y-%m-%d %H:%M:%S")

def save_data(node_id, temp, humi, time = None):
    sql = "INSERT INTO sensor_data (node_id,temperature,humidity,created_at) VALUES (%s,%s,%s,%s)"
    val = (node_id,temp,humi,time)
    
    if time == None:
        val = (node_id,temp,humi,getDateformatted())
    

    db.insert_or_update(sql, val)


def update_node_data(node_id, temp, humi):
    sql = "UPDATE node SET temperature=%s,humidity=%s,updated_at=%s WHERE id = %s"
    val = (temp,humi,getDateformatted(),node_id)
    db.insert_or_update(sql, val)

def get_sensor_data(mode = 'd'):
    sql = "SELECT * FROM sensor_data"
    today = date.today()

    if mode == "d":
        prev = today - timedelta(days=1)
        sql += f" WHERE created_at > '{prev} 23:59' AND created_at <= '{today} 23:59'"
        print("day")
    elif mode == "m":
        prev = today - timedelta(days=30)
        sql += f"  WHERE created_at >= '{prev} 00:00' AND created_at <= '{today} 23:59'" # prev month
        print("month")
    elif mode == 'w':
        prev = today - timedelta(days=6)
        sql += f"  WHERE created_at >= '{prev} 00:00' AND created_at <= '{today} 23:59'"
    print(sql)
    return db.select(sql)

def get_node_data():
    sql = "SELECT * FROM node"
    return db.select(sql)

