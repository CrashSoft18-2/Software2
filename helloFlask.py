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
	return principal()

def principal():
	return show_the_login_form()

@app.route("/login", methods=['GET','POST'])
def login():
	if request.method == 'POST':
		return do_the_login()
	else:
		return show_the_login_form()

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
	
def show_the_login_form(name=None): #paremeters
	return render_template('login.html', name=name)

def childPrincipal(usuarioLogueado):
    return render_template('childPrincipal.html', name=usuarioLogueado.get("nombre"))

def connectToFirebase():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_URL = SITE_ROOT + '/static/json/crashsoft-e0a3e-firebase-adminsdk-czkyi-1a12b89004.json'
	cred = credentials.Certificate(json_URL)
	firebase_admin.initialize_app(cred, {'databaseURL' : 'https://crashsoft-e0a3e.firebaseio.com/'}) 

def init():
	firebase_admin.initialize_app() 

if __name__ == "__main__":
	main()
