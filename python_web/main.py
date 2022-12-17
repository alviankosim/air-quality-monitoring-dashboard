from flask import Flask, render_template
from mysql_connection import *

app = Flask(__name__)

# home route
@app.route("/")
def home():
    return render_template("home.html")
    
# endpoint fetch
@app.route("/fetch")
def fetch():
    print('Data fetched successfully')
    return dbfetchlatestdata()[1]

# # endpoint matikan
# @app.route("/matikan")
# def matikan():
#     # var = input()
#     # ArduinoUnoSerial.write('0'.encode())
#     print('LED telah dimatikan')
#     # time.sleep(1)
#     return "success"
    
if __name__ == "__main__":
    app.run(port=3500, host="0.0.0.0", debug=True)