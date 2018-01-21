from flask import Flask, request, redirect, url_for, g
import sqlite3, logging
import page, check
from query import QueryArtwork, QueryPost

# config
DATABASE = 'db/database.db'

# create app	
app = Flask(__name__)

# Database
def get_conn():
	if not hasattr(g, 'sqlite3_conn'):
		conn = sqlite3.connect(DATABASE)
		conn.row_factory = sqlite3.Row
		g.sqlite3_conn = conn
	return g.sqlite3_conn

# $ export FLASK_APP=main
# $ python3 -m flask initdb
@app.cli.command('initdb')
def init_db():
	with app.app_context():
		cur = get_conn().cursor()
		with app.open_resource('schema.sql', mode='r') as f:
			cur.executescript(f.read())
		cur.close()
		print('database initialized')

@app.teardown_appcontext
def close_conn(error):
	if hasattr(g, 'sqlite3_conn'):
		conn = g.sqlite3_conn
		conn.cursor().close()
		conn.commit()
		conn.close()
		print('db closed')

def query_db(query, args=()):
	cur = get_conn().cursor()
	cur.execute(query, args)
	return cur

@app.route('/', methods=['GET'])
def get_index():
	index = page.Index()
	return index.render()

@app.route('/rot13', methods=['GET'])
def get_rot13():
	rot13 = page.ROT13()
	return rot13.render()

@app.route('/rot13', methods=['POST'])
def post_rot13():
	rot13 = page.ROT13()
	return rot13.render(request.form['rot13_text'])

@app.route('/fizzbuzz', methods=['GET'])
def get_fizzbuzz():
	fizzbuzz = page.FizzBuzz( request.args.get('fizzbuzz_strn') )
	return fizzbuzz.render()

@app.route('/welcome', methods=['GET'])
def get_welcome():
	username=request.args.get('username')
	welcome = page.Welcome()
	return welcome.render(username=username)

#############################################################
# artwork
@app.route('/ascii_art', methods=['GET'])
def get_ascii_art():
	query = QueryArtwork().retrieve(select_one=False, limit=10)
	record_list = query_db(*query).fetchall()
	ascii_art = page.AsciiArt()
	return ascii_art.render(record_list=record_list)

# TODO: 在前端就进行检查，subject和content若为空，则不提交，而不是到了服务器再检查
@app.route('/ascii_art', methods=['POST'])
def post_ascii_art():
	subject = request.form.get('subject')
	content = request.form.get('content')
	if subject and content:
		artwork_id = request.form.get('artwork_id')
		if artwork_id:
			query = QueryArtwork().update(subject, content, artwork_id)
		else:
			query = QueryArtwork().insert(subject, content)
			print('YES')
		query_db(*query)
	return redirect(url_for('get_ascii_art'))
# end artwork
#############################################################

#############################################################
# blogs and posts
@app.route('/blog', methods=['GET'])
def get_blog_index():
	query = QueryPost().retrieve(select_one=False, limit=10)
	record_list = query_db(*query).fetchall()
	blog = page.Blog()
	return blog.render_index(record_list=record_list)

@app.route('/blog/edit/<int:post_id>', methods=['GET'])
def get_blog_edit(post_id):
	query = QueryPost().retrieve(select_one=True, post_id=post_id)
	record = query_db(*query).fetchall()[0]
	blog = page.Blog()
	return blog.render_edit_post(record=record)

@app.route('/blog/new_post', methods=['GET'])
def get_blog_new():
	blog = page.Blog()
	return blog.render_new_post()

@app.route('/blog/<int:post_id>', methods=['GET'])
def get_blog_post(post_id):
	query = QueryPost().retrieve(select_one=True, post_id=post_id)
	record = query_db(*query).fetchall()[0]
	blog = page.Blog()
	return blog.render_post(record=record)

# TODO: 在前端就进行检查，subject和content若为空，则不提交，而不是到了服务器再检查
@app.route('/blog/edit/<int:post_id>', methods=['POST'])
def post_blog_edit(post_id):
	subject = request.form.get('subject')
	content = request.form.get('content')
	if subject and content:
		query = QueryPost().update(subject, content, post_id)
		query_db(*query)
	return redirect('/blog/%d' % post_id)

# TODO: 在前端就进行检查，subject和content若为空，则不提交，而不是到了服务器再检查
@app.route('/blog/new_post', methods=['POST'])
def post_blog_new():
	subject = request.form.get('subject')
	content = request.form.get('content')
	if subject and content:
		query = QueryPost().insert(subject, content)
		query_db(*query)
	return redirect('/blog')
# end blogs and posts
#############################################################

if __name__ == '__main__':
	app.run(port=8000, debug=True)
