from connections_module import Connection
from firebase_admin import db
from flask import request
class Login:
	def __init__(self):
		pass

	def do_the_login(self):
		con = Connection()
		con.connectToFirebase()
		nodo_raiz = db.reference()
		lista_alumnos = nodo_raiz.child('Usuarios/Alumnos').get()
		lista_docentes = nodo_raiz.child('Usuarios/Profesores').get()
		auth = False
		usuario = ""
		password = ""
		print (request.form['uname'])
		print (request.form['psw'])
		print(lista_alumnos)
		for alumno in lista_alumnos:
			usuario = str(alumno.get("user"))
			password = str(alumno.get("password"))
			postUsuario = request.form['uname'] + ""
			postPassword = request.form['psw'] + ""
			print("Try match")
			print (usuario == postUsuario and password == postPassword)
			if (usuario == postUsuario and password == postPassword):
				usuarioLogueado=alumno
				auth = True
				break
		return auth