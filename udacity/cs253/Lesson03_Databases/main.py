from flask import Flask, request, redirect, url_for, g
import sqlite3
import page
app = Flask(__name__)

#################################################################################
DATABASE = 'ascii_art.db'

def get_conn():
	if not hasattr(g, 'sqlite3_conn'):
		conn = sqlite3.connect(DATABASE)
		conn.row_factory = sqlite3.Row
		g.sqlite3_conn = conn
	return g.sqlite3_conn

def init_db():
	with app.app_context():
		cur = get_conn().cursor()
		with app.open_resource('schema.sql', mode='r') as f:
			cur.executescript(f.read())
		cur.close()

@app.cli.command('initdb')
def initdb_command():
	init_db()
	print('database initialized')

@app.teardown_appcontext
def close_connection(exception):
	if hasattr(g, 'sqlite3_conn'):
		conn = g.sqlite3_conn
		conn.cursor().close()
		conn.commit()
		conn.close()
		print('connection closed')

def query_db(query, args=()):
	cur = get_conn().cursor()
	cur.execute(query, args)
	return cur

def insert_record(args):
	if args and isinstance(args, tuple) and len(args) == 2:
		query = 'insert into entries (subject, content) values (?, ?)'
		query_db(query, args=args)
		return True
	else:
		return False

def update_record(args):
	if args and isinstance(args, tuple) and len(args) == 3:
		query = 'update entries set subject = ?, content = ? where art_id = ?'
		query_db(query, args)
		return True
	else:
		return False

def get_record_list(limit=10):
	query = 'select * from entries order by art_id desc limit %d' % limit
	cur = query_db(query)
	record_list = cur.fetchall()
	return record_list
#################################################################################



@app.route('/', methods=['GET'])
def get_index():
	return page.render_index()

@app.route('/ascii_art', methods=['GET'])
def get_ascii_art():
	record_list = get_record_list()
	return page.render_art(record_list=record_list)

@app.route('/ascii_art', methods=['POST'])
def post_ascii_art():
	subject = request.form.get('subject')
	content = request.form.get('content')
	if subject and content:
		art_id = request.form.get('art_id')
		if art_id and art_id.isdigit():
			args = (subject, content, art_id)
			update_record(args)
		else:
			args = (subject, content)
			insert_record(args)
	return redirect(url_for('get_ascii_art'))
	
if __name__ == '__main__':
	app.run(port=8000, debug=True)
