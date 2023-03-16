from flask import Flask, request, jsonify, send_file
from psycopg2 import connect, extras

app = Flask(__name__)

app = Flask(__name__, static_folder='web')

host     = 'localhost'
port     = 5432
dbname   = 'bd_iec'
user     = 'postgres'
password = '1357'


def get_connection():
    conn = connect(host=host, port=port, dbname=dbname,user=user, password=password)
    return conn

@app.get('/getlist/formulario')
def get_formularioList():
    conn         = get_connection()
    cur          = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("select * FROM estudiante")
    estudiante = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(estudiante)

#guardar estudiante
    
@app.post('/save/formulario')
def save_formulario():
    nuevo_estudiante = request.get_json()
 # id           = nuevo_estudiante['id_est']
    cedula       = nuevo_estudiante['cedula_est'] 
    nombres      = nuevo_estudiante['nombres']
    apellidos    = nuevo_estudiante['apellidos']
    correo       = nuevo_estudiante['correo']
    celular      = nuevo_estudiante['celular']
    telefono     = nuevo_estudiante['telefono']
    ciudad       = nuevo_estudiante['ciudad']
    sector       = nuevo_estudiante['sector']
    barrio       = nuevo_estudiante['barrio']
    movilizacion = nuevo_estudiante['movilizacion']
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute('insert into estudiante (cedula_est, nombres, apellidos, correo, celular, telefono, ciudad, sector, barrio, movilizacion) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) returning *',
                (cedula, nombres, apellidos, correo, celular, telefono, ciudad, sector, barrio, movilizacion))  
    
    estudiante_guardado = cur.fetchone()
    print (estudiante_guardado)
    conn.commit() 
    cur.close()
    conn.close()
    return jsonify(estudiante_guardado)
    
    
@app.get('/')
def home():
    return send_file('static/formu.html')
    
if __name__ == '__main__':
    app.run(debug=True) 