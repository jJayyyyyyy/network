import sqlite3, logging
db_name='ascii_art.db'

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

def insert(title, art):
	if title and art:
		args = (title, art)
		sql = 'insert into entries (title, art) values (?, ?)'
		do_sql(sql, args)

def delete(id):
	if id and id.isdigit():
		sql = 'delete from entries where id=%s' % id
		do_sql(sql)

def get_record_list():
	sql = 'select * from entries'
	record_list = do_sql(sql)
	return record_list

def init():
	sql = 'drop table if exists entries'
	do_sql(sql)
	sql = 'create table entries (\
				id integer primary key autoincrement,\
				title text not null,\
				art text not null)'
	do_sql(sql)

def test():
	# init()
	title = 'hello'
	art = '^_^'
	insert(title, art)
	record_list = get_record_list()
	for item in record_list:
		print(*item)

test()
