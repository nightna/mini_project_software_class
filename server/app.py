from flask import Flask,request,jsonify, make_response
import datetime
import json
import mysql.connector

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
host="localhost"
user = "root"
db = "mini_project"
password = ""

def save_data(node_id, temp, humi):
    mydb = mysql.connector.connect(host=host , user = user, password = password, db = db )
    mycursor = mydb.cursor(dictionary = True)
    sql = "INSERT INTO sensor_data (node_id,temperature,humidity) VALUES (%s,%s,%s)"
    val = (node_id,temp,humi)
    mycursor.execute(sql,val)
    mydb.commit()

def update_node_data(node_id, temp, humi):
    mydb = mysql.connector.connect(host=host , user = user, password = password, db = db )
    mycursor = mydb.cursor(dictionary = True)

    sql = "UPDATE node SET temperature=%s,humidity=%s,updated_at=%s WHERE id = %s"

    current_Date = datetime.datetime.now()
    formatted_date = current_Date.strftime("%Y-%m-%d %H:%M:%S")

    val = (temp,humi,formatted_date,node_id)
    mycursor.execute(sql,val)
    mydb.commit()

def get_sensor_data():
    mydb = mysql.connector.connect(host=host , user = user, password = password, db = db )
    mycursor = mydb.cursor(dictionary = True)

    sql = "SELECT * FROM sensor_data"
    mycursor.execute(sql)
    return mycursor.fetchall()


# Create
@app.route("/api/sensor_data",methods = ["POST", "GET"])
def sensor_data():
    # Creat data
    if request.method == "POST":
        data = request.get_json()
        save_data(data['node_id'], data['temperature'], data['humidity'])
        update_node_data(data['node_id'], data['temperature'], data['humidity'])
        return make_response(jsonify({"status": "OK"},200))
    elif request.method == "GET":
        data = get_sensor_data()
        return make_response(jsonify(data), 200)

# read
@app.route("/api/node_data")
def read():
    mydb = mysql.connector.connect(host=host , user = user, password = password, db = db )
    mycursor = mydb.cursor(dictionary = True)
    mycursor.execute("SELECT * FROM node")
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult),200)


if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)