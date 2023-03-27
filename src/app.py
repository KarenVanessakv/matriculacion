import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mysqldb import MySQL
from config import config
from flask_login import LoginManager,login_user,logout_user,login_required
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

#models
from models.ModelUser import ModelUser

#entities
from models.entities.User import User

app = Flask(__name__)
csrf=CSRFProtect()
login_manager_app=LoginManager(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:psycopg2//postgres:2580@localhost:5432/bd_iec'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:5432/bd_iec'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0, request.form['correo'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña inválida")
            return render_template('login/login.html')
        else:
            flash("Usuario no encontrado")
            return render_template('login/login.html')
    else:
        return render_template('login/login.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route('/register')
def register():
    return render_template('register/register.html')

@app.route('/register', methods=['POST'])
def register_post():
    _nombres = request.form['nombres']
    _apellidos = request.form['apellidos']
    _correo = request.form['correo']
    _password = request.form['password']

    user = User.query.filter_by(correo=_correo).first()
    if _nombres =='' or _apellidos=='' or _correo=='' or _password=='' or user:
        flash('Todos los campos son obligatorios')
        return redirect(url_for('register/register.html'))

    sql = "INSERT INTO `usuarios`(`id`, `nombres`, `apellidos`, `correo`, `password`) VALUES (NULL, %s, %s, %s, %s);"
    datos = (_nombres, _apellidos, _correo, _password)
    db.session.add(sql,datos)
    db.session.commit()

    return redirect(url_for('login/login.html'))

@app.route("/home")
def home():
    return render_template("alumnos/vistaA.html")

@app.route('/protected')
@login_required
def protected():
    return "<h1>Ésta es una vista protegida, solo para usuarios autenticados.</h1>"

def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
