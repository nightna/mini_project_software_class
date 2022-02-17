from flask import Flask,request,jsonify, make_response
import mysql.connector
from flask_cors import CORS
import services

app = Flask(__name__)
CORS(app)

app.config["JSON_AS_ASCII"] = False


# Create
@app.route("/api/sensor_data",methods = ["POST", "GET"])
def sensor_data():
    # Creat data
    if request.method == "POST":
        data = request.get_json()
        node_id = data['node_id']
        temp = float(data['temperature'])
        humi = float(data['humidity'])

        services.save_data(node_id, temp, humi)
        services.update_node_data(node_id, temp, humi)
        return make_response(jsonify({"status": "OK"},200))
    elif request.method == "GET":
        data = services.get_sensor_data()
        return make_response(jsonify(data), 200)

# read
@app.route("/api/node_data")
def read():
    data = services.get_node_data()
    return make_response(jsonify(data),200)


if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)