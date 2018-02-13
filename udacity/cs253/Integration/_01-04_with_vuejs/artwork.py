from page import Page
from database import Database

class Artwork(object):
	def __init__(self, id='', subject='', content=''):
		self.id = id
		self.subject = subject
		self.content = content

class Record(Artwork):
	def insert(self):
		query = 'insert into artworks (subject, content) values (?, ?)'
		args = (self.subject, self.content)
		return Database().query_db(query, args)

	def update(self):
		query = 'update artworks set subject = ?, content = ? where id = ?'
		args = (self.subject, self.content, self.id)
		return Database().query_db(query, args)
		
	def retrieve(self, id=0, limit=10):
		if id > 0:
			query = 'select * from artworks where id = %d' % id
		else:
			query = 'select * from artworks order by id desc limit %d' % limit
		return Database().query_db(query)
	
	def delete(self, id):
		query = 'delete from artworks where id = ?'
		args = (id, )
		Database().query_db(query, args)

class AsciiArtHandler(Page):
	filename = 'artwork/artwork.html'

	def get(self):
		if self.get_args('q') == 'json':
			record_list = Record().retrieve(limit=10)
			return self.json_response(record_list)
		else:
			return self.render_raw(self.filename)

	def post(self):
		if self.check_valid_cookie():
			print('logged')
			form = self.form()
			subject = form.get('subject')
			content = form.get('content')
			if subject and content:
				id = form.get('id')
				if id:
					Record(id, subject, content).update()
					# 不必重新读取数据库并返回json，而是直接告诉前端，刚才提交的数据是合理的，在前端直接用本地数据更新dom即可
					return 'updated'
				else:
					Record(0, subject, content).insert()
					return 'inserted'
			else:
				return 'invalid form'
		else:
			return 'signin'
