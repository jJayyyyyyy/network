import datetime

class QueryArtwork():
	def __init__(self):
		pass

	def insert(self, subject, content):
		query = 'insert into artworks (subject, content) values (?, ?)'
		args = (subject, content)
		return (query, args)

	def update(self, subject, content, artwork_id):
		query = 'update artworks set subject = ?, content = ? where artwork_id = ?'
		args = (subject, content, str(artwork_id))
		return (query, args)
		
	def retrieve(self, select_one=True, artwork_id=1, limit=10):
		if select_one == True:
			query = 'select * from artworks where artwork_id = %d' % artwork_id
		else:
			query = 'select * from artworks order by artwork_id desc limit %d' % limit
		args = ()
		return (query, args)
	
	def delete(self, artwork_id):
		query = 'delete from artworks where artwork_id = ?'
		args = artwork_id
		return (query, args)

class QueryPost(object):
	def __init__(self):
		pass
		
	def insert(self, subject, content):
		query = 'insert into posts (update_date, subject, content) values (?, ?, ?)' 
		update_date = datetime.date(2018, 1, 1)
		args = (update_date, subject, content)
		return (query, args)

	def update(self, subject, content, post_id):
		query = 'update posts set update_date = ?, subject = ?, content = ? where post_id = ?'
		update_date = datetime.date.today()
		args = (update_date, subject, content, str(post_id))
		return (query, args)

	def retrieve(self, select_one=True, post_id=1, limit=10):
		if select_one == True:
			query = 'select * from posts where post_id = %d' % post_id
		else:
			query = 'select * from posts order by post_id desc limit %d' % limit
		args = ()
		return (query, args)

	def delete(self, post_id):
		query = 'delete from artworks where artwork_id = ?'
		args = artwork_id
		return (query, args)
