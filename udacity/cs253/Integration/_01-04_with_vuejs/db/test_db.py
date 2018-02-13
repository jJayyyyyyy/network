import sqlite3, logging, datetime
db_name='database.db'

def do_sql(sql, args=''):
	res = None
	try:
		conn = sqlite3.connect(db_name)
		conn.row_factory = sqlite3.Row
		cur = conn.cursor()
		cur.execute(sql, args)
		res = cur.fetchall()
		conn.commit()
	except Exception as e:
		logging.exception(e)
	finally:
		cur.close()
		conn.close()
	return res

def insert():
	sql = 'insert into posts (update_date, subject, content) values (?, ?, ?)'
	update_date = datetime.date.today()
	subject = 'hello'
	content = 'world'
	args = (update_date, subject, content)
	res = do_sql(sql, args)

def insert_art():
	sql = 'insert into artworks (subject, content) values (?, ?)'
	subject = 'hello'
	content = 'world'
	args = (subject, content)
	res = do_sql(sql, args)

def insert_user():
	sql = 'insert into users (username, pw_hash, email) values (?, ?, ?)'
	args = ('123', '123', '123')
	do_sql(sql, args)

def get_record_list():
	# sql = 'select * from artworks'
	# sql = 'select * from users'
	sql = 'select * from posts'
	record_list = do_sql(sql)
	# sql = 'select username from users where username=?'
	# args = ('1234', )

	# record_list = do_sql(sql, args)
	return record_list

def update():
	today = post_date = datetime.date.today()
	print(type(today))
	query = 'update posts set post_date = ? where post_id = ?)'
	args = (today, '1')
	# do_sql(query, args)

def init():
	sql = 'drop table if exists users'
	do_sql(sql)
	sql = 'create table users (\
				user_id integer primary key autoincrement,\
				username date not null unique,\
				pw_hash text not null,\
				email text)'
	do_sql(sql)


def test():
	# init()
	# insert_art()
	# post_id = '1'
	
	# post_subject = 
	# art = '^_^'
	# update()
	# insert_user()
	record_list = get_record_list()
	# print(record_list[0]['username'])
	for item in record_list:
		print(*item)
		# print(dict(item).get('username'))
	# 	print(item['username'])
	

test()
