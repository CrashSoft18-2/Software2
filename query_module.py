import psycopg2
from connections_module import Connection
class QClass:
	def __init__(self):
		pass

	def query_file(self, ruta):
		command = open_sql_file(ruta)
		conn = Connection().connectToPostgre()
		cur = conn.cursor()
		rows = None
		try:
			cur.execute(command)
			rows = cur.fetchall()
			cur.close()
			conn.close()
		except OperationalError, msg:
			print ("No se ejecuto la consulta.")
		return rows

	def open_sql_file(self, ruta):
		fd = open(ruta, 'r')
		sqlFile = fd.read()
		fd.close()
		return sqlFile