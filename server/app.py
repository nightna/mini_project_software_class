from flask import Flask,request,jsonify, make_response

import json
import mysql.connector

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
host="localhost"
user = "root"
db = "mini_project"
password = ""

# resd
@app.route("/api/data")
def read():
    mydb = mysql.connector.connect(host=host , user = user, password = password, db = db )
    mycursor = mydb.cursor(dictionary = True)
    mycursor.execute("SELECT * FROM data")
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult),200)

# Read
@app.route("/api/data/<id>")
def readbyid(id):
    mydb = mysql.connector.connect(host=host , user = user, password = password, db = db )
    mycursor = mydb.cursor(dictionary = True )
    sql = "SELECT * FROM data WHERE id = %s"
    val = (id,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult),200)

# Create
@app.route("/api/data",methods = ["POST"])
def create():
    data = request.get_json()
    mydb = mysql.connector.connect(host=host , user = user, password = password, db = db )
    mycursor = mydb.cursor(dictionary = True)
    sql = "INSERT INTO sensor_data (node_id,temperature,humidity) VALUES (%s,%s,%s)"
    val = (data["node_id"],data["temperature"],data["humidity"])
    mycursor.execute(sql,val)
    mydb.commit()
    return make_response(jsonify({ "rowcount": mycursor.rowcount},200))

#updaet
@app.route("/api/data/<id>",methods = ["PUT"])
def update(id):
    data = request.get_json()
    mydb = mysql.connector.connect(host=host , user = user, password = password, db = db )
    mycursor = mydb.cursor(dictionary = True)
    sql = "UPDATE sensor_data SET name =%s , detail = %s  WHERE id = %s"
    val = (data["name"],data["detail"] , id)
    mycursor.execute(sql,val)
    mydb.commit()
    return make_response(jsonify({ "rowcount": mycursor.rowcount},200))

#delete
@app.route("/api/data/<id>",methods = ["DELETE"])
def delete(id):
    mydb = mysql.connector.connect(host=host , user = user, password = password, db = db )
    mycursor = mydb.cursor(dictionary = True)
    sql = "DELETE FROM data WHERE id = %s"
    val = (id,)
    mycursor.execute(sql,val)
    mydb.commit()
    return make_response(jsonify({ "rowcount": mycursor.rowcount},200))


if __name__=="__main__":
    app.run(debug=True)