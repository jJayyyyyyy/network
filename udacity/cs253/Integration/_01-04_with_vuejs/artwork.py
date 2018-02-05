from page import Page
from database import Database

class Artwork(object):
	def __init__(self, artwork_id='', subject='', content=''):
		self.artwork_id = artwork_id
		self.subject = subject
		self.content = content

class Record(Artwork):
	def insert(self):
		query = 'insert into artworks (subject, content) values (?, ?)'
		args = (self.subject, self.content)
		return Database().query_db(query, args)

	def update(self):
		query = 'update artworks set subject = ?, content = ? where artwork_id = ?'
		args = (self.subject, self.content, self.artwork_id)
		return Database().query_db(query, args)
		
	def retrieve(self, artwork_id=0, limit=10):
		if artwork_id > 0:
			query = 'select * from artworks where artwork_id = %d' % artwork_id
		else:
			query = 'select * from artworks order by artwork_id desc limit %d' % limit
		return Database().query_db(query)
	
	def delete(self):
		query = 'delete from artworks where artwork_id = ?'
		args = (artwork_id, )
		Database().query_db(query, args)

def get_artwork_list(record_list=[]):
	artwork_list=[]
	for record in record_list:
		artwork = Artwork(*record)
		artwork_list.append(artwork)
	return artwork_list

class AsciiArtHandler(Page):
	filename = 'ascii_art.html'

	def get(self):
		record_list = Record().retrieve(limit=10)
		artwork_list = get_artwork_list(record_list)
		return self.render(self.filename, artwork_list=artwork_list)

	def post(self):
		subject = self.form().get('subject')
		content = self.form().get('content')
		if subject and content:
			artwork_id = self.form().get('artwork_id')
			if artwork_id:
				Record(artwork_id, subject, content).update()
			else:
				Record(0, subject, content).insert()
			return self.redirect('/ascii_art')
		else:
			error = 'subject or content is empty'
			return self.render(self.filename, error=error)

	
