from flask import Flask, request, jsonify, send_file
from psycopg2 import connect, extras

app = Flask(__name__)

host= 'localhost'
port='5432'
bdname='bd_iec'
user='postgres'
password='2580'

def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn

@app.get('/')
def home():
    return send_file("login/login.py")

if __name__ == "__main__":
    app.run(debug=True)
