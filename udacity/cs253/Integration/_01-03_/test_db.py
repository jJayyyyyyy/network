import sqlite3, logging, datetime
db_name='post.db'

def do_sql(sql, args=''):
	res = None
	try:
		conn = sqlite3.connect(db_name)
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
	sql = 'insert into posts (update_date, post_subject, post_content) values (?, ?, ?)'
	update_date = datetime.date.today()
	post_subject = 'hello'
	post_content = 'world'
	args = (update_date, post_subject, post_content)
	res = do_sql(sql, args)

def get_record_list():
	sql = 'select * from posts'
	record_list = do_sql(sql)
	return record_list

def update():
	today = post_date = datetime.date.today()
	print(type(today))
	query = 'update posts set post_date = ? where post_id = ?)'
	args = (today, '1')
	# do_sql(query, args)

def init():
	sql = 'drop table if exists posts'
	do_sql(sql)
	sql = 'create table posts (\
				post_id integer primary key autoincrement,\
				update_date date not null,\
				post_subject text not null,\
				post_content text not null)'
	do_sql(sql)

def test():
	init()
	insert()
	# post_id = '1'
	
	# post_subject = 
	# art = '^_^'
	# update()
	record_list = get_record_list()
	for item in record_list:
		print(*item)

test()
