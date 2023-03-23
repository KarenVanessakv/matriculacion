from flask import Flask, request, jsonify, send_file
from psycopg2 import connect, extras

app = Flask(__name__)

app = Flask(__name__, static_folder='web')

host     = 'localhost'
port     = 5432
dbname   = 'bd_iec'
user     = 'postgres'
password = 'godofwar4'


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
    
@app.post("/save/formulario")
def save_formulario(): 
    nuevo_estudiante = request.get_json()
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
    
    

#formulario instituto   
@app.get('/getlist/instituto')
def get_formularioList1():
    conn         = get_connection()
    cur          = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("select * FROM institucion")
    instituto = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(instituto)

#guardar instituto


@app.post("/save/institucion")
def save_formularioIns(): 
    datos_inst = request.get_json()
    nombre       = datos_inst['nombre'] 
    tipo         = datos_inst['tipo']
    grado        = datos_inst['grado']
    seccion      = datos_inst['seccion']    
    anio         = datos_inst['anio']
    notauno        = datos_inst['notauno']  
    notados        = datos_inst['notados']
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute('insert into institucion (nombre, tipo, grado, seccion, anio, notauno, notados) values (%s,%s,%s,%s,%s,%s,%s) returning *', 
                (nombre, tipo, grado, seccion, anio, notauno, notados))  
     
    datos_insti = cur.fetchone()
    print (datos_insti)
    conn.commit() 
    cur.close()
    conn.close()
    return jsonify(datos_insti)
    
    
    
#     #formulario representante  
# @app.get('/getlist/representante')
# def get_formularioList():
#     conn         = get_connection()
#     cur          = conn.cursor(cursor_factory=extras.RealDictCursor)
#     cur.execute("select * FROM representante")
#     representante = cur.fetchall()
#     cur.close()
#     conn.close()
#     return jsonify(representante)

# #guardar representante


# @app.post("/save/formulario")
# def save_formulario(): 
#     datos_repre = request.get_json()
#     cedula          = datos_repre['ced_re'] 
#     nombre          = datos_repre['nomb_re']
#     apellido        = datos_repre['ap_re']
#     correo          = datos_repre['correo_re']
#     celular         = datos_repre['cel_re']
#     telefono        = datos_repre['telf_re']
#     conn = get_connection()
#     cur = conn.cursor(cursor_factory=extras.RealDictCursor)
#     cur.execute('insert into estudiante (ced_re, nomb_re, ap_re, correo_re, cel_re, telf_re) values (%s,%s,%s,%s,%s,%s) returning *', 
#                 (cedula, nombre, apellido, correo, celular, telefono))  
    
#     datos_repre = cur.fetchone()
#     print (datos_repre)
#     conn.commit() 
#     cur.close()
#     conn.close()
#     return jsonify(datos_repre)
    
    
# @app.get('/')
# def home():
#     return send_file('static/formu.html')
    
# if __name__ == '__main__':
#     app.run(debug=True) 
    
    
    
#      #formulario iecaaa
# @app.get('/getlist/iecaaa')
# def get_formularioList():
#     conn         = get_connection()
#     cur          = conn.cursor(cursor_factory=extras.RealDictCursor)
#     cur.execute("select * FROM iecaaa")
#     iecaaa = cur.fetchall()
#     cur.close()
#     conn.close()
#     return jsonify(iecaaa)

# #guardar iecaaa


# @app.post("/save/formulario")
# def save_formulario(): 
#     datos_iecaaa = request.get_json()
#     estado                 = datos_iecaaa['estado'] 
#     planificacion          = datos_iecaaa['plan']
#     a_inicio            = datos_iecaaa['a_i']
#     fecha_llamada          = datos_iecaaa['fecha_ll']
#     descripcion            = datos_iecaaa['desc']
#     observaciones          = datos_iecaaa['obse']
#     evaluaciones           = datos_iecaaa['eva']
#     conn = get_connection()
#     cur = conn.cursor(cursor_factory=extras.RealDictCursor)
#     cur.execute('insert into estudiante (estado, plan, a_i, fecha_ll, desc, obse, eva) values (%s,%s,%s,%s,%s,%s,%s) returning *', 
#                 (estado, planificacion, a_inicio, fecha_llamada, descripcion, observaciones, evaluaciones))  
    
#     datos_iecaaa = cur.fetchone()
#     print (datos_iecaaa) 
#     conn.commit()  
#     cur.close()
#     conn.close()
#     return jsonify(datos_iecaaa)
    
   
   
    
@app.get('/')
def home():
    return send_file('static/Max.html')

@app.route('/pagina2')
def pagina2():
    return send_file('static/seguimiento.html')
    
    
if __name__ == '__main__':
    app.run(debug=True) 
        
    
    