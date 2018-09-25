from firebase_admin import credentials
import os
class Connection:
	def __init__(self):
		pass
	def connectToFirebase(self):
		SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
		json_URL = SITE_ROOT + '/static/json/crashsoft-e0a3e-firebase-adminsdk-czkyi-1a12b89004.json'
		if (not len(firebase_admin._apps)):
			cred = credentials.Certificate(json_URL)
			firebase_admin.initialize_app(cred, {'databaseURL' : 'https://crashsoft-e0a3e.firebaseio.com/'})
