from flask import Flask, request, redirect, url_for, g
import sqlite3, datetime
import page
app = Flask(__name__)

#################################################################################
DATABASE = 'post.db'

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
def close_conn(error):
	if hasattr(g, 'sqlite3_conn'):
		conn = g.sqlite3_conn
		conn.cursor().close()
		conn.commit()
		conn.close()
		print('db connection closed')

def query_db(query, args=()):
	cur = get_conn().cursor()
	cur.execute(query, args)
	return cur

# @args(update_date, post_subject, post_content)
def insert_record(args):
	if args and isinstance(args, tuple) and len(args) == 3:
		query = 'insert into entries (update_date, post_subject, post_content) values (?, ?, ?)'
		query_db(query, args=args)
		return True
	else:
		return False

# @args(update_date, post_subject, post_content, post_id)
def update_record(args):
	if args and isinstance(args, tuple) and len(args) == 4:
		query = 'update entries set update_date = ?, post_subject = ?, post_content = ? where post_id = ?'
		query_db(query, args)
		return True
	else:
		return False

def get_record(post_id):
	if post_id and isinstance(post_id, int):
		query = 'select * from entries where post_id = %d' % post_id
		cur = query_db(query)
		record_list = cur.fetchall()
		if record_list:
			return record_list[0]
		else:
			return None

def get_last_post_id():
	query = 'select post_id from entries where post_id = (select max(post_id) from entries)'
	# query = 'select * from entries order by post_id desc limit 1'
	cur = query_db(query)
	record_list = cur.fetchall()
	if record_list:
		record = record_list[0]
		post_id = record['post_id']
		return post_id
	else:
		return None

def get_record_list(limit=10):
	query = 'select * from entries order by post_id desc limit %d' % limit
	cur = query_db(query)
	record_list = cur.fetchall()
	return record_list

#################################################################################




@app.route('/blog', methods=['GET'])
def get_blog():
	record_list = get_record_list()
	return page.render_blog(record_list=record_list)

@app.route('/blog/<int:post_id>', methods=['GET'])
def get_post(post_id):
	record = get_record(post_id)
	return page.render_post(record)

@app.route('/blog/edit/<int:post_id>', methods=['GET'])
def get_edit_post(post_id):
	record = get_record(post_id)
	return page.render_edit_post(**record)

@app.route('/blog/edit/<int:post_id>', methods=['POST'])
def post_edit_post(post_id):
	post_subject = request.form.get('post_subject')
	post_content = request.form.get('post_content')

	if post_subject and post_content:
		update_date = datetime.date.today()
		args = (update_date, post_subject, post_content, str(post_id))
		update_record(args)
	return redirect(url_for('get_post', post_id=post_id))

@app.route('/blog/new_post', methods=['GET'])
def get_new_post():
	return page.render_new_post()

@app.route('/blog/new_post', methods=['POST'])
def post_new_post():
	post_subject = request.form.get('post_subject')
	post_content = request.form.get('post_content')
	
	if post_subject and post_content:
		update_date = datetime.date(2018, 1, 1)
		args = (update_date, post_subject, post_content)
		insert_record(args)	
		post_id = get_last_post_id()
		return redirect(url_for('get_post', post_id=post_id))
	
	kw = {	'error': 'invalid subject or content',
			'post_subject': post_subject,
			'post_content': post_content
		}
	return page.render_new_post(**kw)

#################################################################################

if __name__ == '__main__':
	app.run(port=8000, debug=True)
	# app.run(port=8080, host='0.0.0.0')
