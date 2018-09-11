from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
import os

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return main()

def do_the_login():
	connectToFirebase()
	nodo_raiz = db.reference()
	lista_alumnos = nodo_raiz.child('Usuarios/Alumnos').get()
	lista_docentes = nodo_raiz.child('Usuarios/Profesores').get()
	auth = False
	usuario = ""
	password = ""
	print (request.form['uname'])
	print (request.form['psw']) 
	for key, value in lista_alumnos.items():
		usuario = str(value.get("user"))
		password = str(value.get("password"))
		postUsuario = request.form['uname'] + ""
		postPassword = request.form['psw'] + ""
		print (usuario)
		print (password)
		print ("aca")
		print (usuario == postUsuario and password == postPassword)
		if (usuario == postUsuario and password == postPassword):
                        usuarioLogueado=value
                        auth = True
                        break
	if auth == True:
		return childPrincipal(usuarioLogueado)
	else:
		return show_the_login_form()

@app.route("/principal")
def childPrincipal():
    return render_template('childPrincipal.html')
@app.route("/asesorias")
def childAsesorias():
	return render_template('childAsesorias.html')
@app.route("/citas")
def childCitas():
	return render_template('childCitas.html')
@app.route("/historial")
def childHistorial():
	return render_template('childHistorial.html')
@app.route("/seminarios")
def childSeminarios():
	return render_template('childSeminarios.html')

def connectToFirebase():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_URL = SITE_ROOT + '/static/json/crashsoft-e0a3e-firebase-adminsdk-czkyi-1a12b89004.json'
	cred = credentials.Certificate(json_URL)
	firebase_admin.initialize_app(cred, {'databaseURL' : 'https://crashsoft-e0a3e.firebaseio.com/'}) 

def init():
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
	firebase_admin.initialize_app() 

if __name__ == "__main__":
	init()
	main()
