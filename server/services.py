from db import DB
import datetime

host="remotemysql.com"
user = "l3TwHwPuiC"
db = "l3TwHwPuiC"
password = "V990J6oxnK"

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

def get_sensor_data():
    sql = "SELECT * FROM sensor_data WHERE 1 and created_at BETWEEN '2022-02-00%' and  '2022-02-03%' "
    return db.select(sql)

def get_sensor_dataMONTH():
    sql = "SELECT * FROM sensor_data WHERE 1 and created_at  BETWEEN '2022-00-00%' and  '2022-03-00%'  "
    return db.select(sql)

def get_sensor_dataWeek():
    sql = "SELECT * FROM sensor_data WHERE 1 and created_at  BETWEEN '2022-00-00%' and  '2022-03-00%'  "
    return db.select(sql)


def get_node_data():
    sql = "SELECT * FROM node"
    return db.select(sql)

