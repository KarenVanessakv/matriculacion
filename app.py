from flask import Flask, request, jsonify, send_file
from psycopg2 import connect, extras

app = Flask(__name__)

<<<<<<< HEAD
host= 'localhost'
port='5432'
bdname='bd_iec'
user='postgres'
password='2580'

def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
=======
host = 'localhost'
port = 5432
dbname = 'bd_iec'
user = 'postgres'
password = '200494'


def get_connection():
    conn = connect(host=host, port=port, dbname=dbname,user=user, password=password)
>>>>>>> Esteban
    return conn

@app.get('/')
def home():
<<<<<<< HEAD
    return send_file("login/login.py")

if __name__ == "__main__":
    app.run(debug=True)
=======
    return send_file('static/vistaA.html')
    
if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> Esteban
