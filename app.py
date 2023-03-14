from os import name                 #nombra el metodo flask
from threading import main_thread   #trae el modulo main
from flask import Flask, send_file             #incluye todo el framework
from flask import render_template, request, flash, redirect, url_for, session, logging           #permite mostrar todos los templates
from psycopg2 import psycopg2, connect, extras                  #permite la conexion a la bdd

app = Flask(__name__)               #crear la aplicacion
app.secret_key = 'secret'

host = "localhost"
port = 5432
dbname = "bd_iec"
user = "postgres"
password = "2580"

def get_connection():                                                                          #llamando al modulo de la bdd
    conn = psycopg2.connect("host=localhost port=5432 dbname=bd_iec user=postgres password=2580")       #inicializa la conexion a la bdd
    return conn

@app.get('/')
def home():
    return send_file('templates/alumnos/vistaA.html')

if __name__ == '__main__':
    app.run(debug=True)
