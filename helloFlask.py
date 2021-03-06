from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
import os
import psycopg2
from flask import session
from flask import flash
from login_module import Login
from connections_module import Connection
from query_module import QClass
app = Flask(__name__)
app.secret_key = b'1234'

@app.route("/")
def main():
	return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return login_system()
    else:
        return main()

def login_system():
	login = Login()
	auth = login.do_the_login()
	if auth == True:
		session['username'] = request.form['uname']
		session['usuario_logueado'] = login.usuario_logueado
		flash('Te logueaste papu {}'.format(session['username']))
		return childPrincipal(login.usuario_logueado)
	else:
		return main()

@app.route("/principal")
def childPrincipal(usuarioLogueado):
	return render_template('childPrincipal.html')
@app.route("/asesorias")
def childAsesorias():
	motor_queries = QClass()
	tabla = motor_queries.query_file("queries/queryAsesorias.sql")
	session['tablaAsesorias'] = tabla
	return render_template('childAsesorias.html')
@app.route("/citas")
def childCitas():
	motor_queries = QClass()
	tabla = motor_queries.query_file("queries/queryCitas.sql")
	session['tablaCitas'] = tabla
	return render_template('childCitas.html')
@app.route("/historial")
def childHistorial():
	return render_template('childHistorial.html')
@app.route("/seminarios")
def childSeminarios():
	motor_queries = QClass()
	tabla = motor_queries.query_file("queries/querySeminarios.sql")
	session['tablaSeminarios'] = tabla
	return render_template('childSeminarios.html')

def init():
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
	firebase_admin.initialize_app() 

if __name__ == "__main__":
	init()
	main()
