import sqlite3
import Page
from flask import Flask, request, redirect, url_for, g
from Art import ArtWork
app = Flask(__name__)
DATABASE = 'ascii_art.db'

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	return db

def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

def commit_db():
	db = get_db()
	db.commit()

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		commit_db()
		db.close()

def query_db(query, args=(), one=False):
	cur = get_db().execute(query, args)
	record_list = cur.fetchall()
	cur.close()
	return record_list

def add_record(args):
	if args and isinstance(args, tuple):
		insert_query = 'insert into entries (title, art) values (?, ?)'
		query_db(insert_query, args)

def delete_record(id):
	if id and id.isdigit():
		delete_query = 'delete from entries where id = %s' % id
		query_db(delete_query)

def get_record(id):
	if id and id.isdigit():
		get_query = 'select * from entries where id=%s' % id
		record = query_db(get_query)
		if record:
			return record[0]

def get_record_list():
	get_query = 'select * from entries order by id desc'
	record_list = query_db(get_query)
	return record_list

@app.route('/', methods=['GET'])
def get_index():
	return Page.render_index()

@app.route('/ascii', methods=['GET'])
def get_art():
	record_list = get_record_list()
	return Page.render_art(record_list=record_list)

@app.route('/ascii', methods=['POST'])
def post_art():
	delete_id = request.form.get('delete_id')
	delete_record(delete_id)

	title, art = request.form.get('title'), request.form.get('art')
	if title and art:
		args = (title, art)
		add_record(args)
	return redirect(url_for('get_art'))
	
if __name__ == '__main__':
	app.run(port=8000, debug=True)
