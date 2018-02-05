import sqlite3, logging
DATABASE = 'db/database.db'
SCHEMA = 'db/schema.sql'

def init_db():
	try:
		conn = sqlite3.connect(DATABASE)
		cur = conn.cursor()
		with open(SCHEMA, 'r') as f:
			cur.executescript(f.read())
		conn.commit()
		print('database initialized')
	except Exception as e:
		print('database failed')
		logging.exception(e)
	finally:
		cur.close()
		conn.close()
		print('db closed')

class Database(object):
	def __init__(self):
		pass

	def query_db(self, query, args=()):
		try:
			conn = sqlite3.connect(DATABASE)
			conn.row_factory = sqlite3.Row
			cur = conn.cursor()
			cur.execute(query, args)
			record_list = cur.fetchall()
			conn.commit()
		except Exception as e:
			record_list = []
			logging.exception(e)
			print('query failed')
		finally:
			cur.close()
			conn.close()
			print('db closed')
			return record_list
