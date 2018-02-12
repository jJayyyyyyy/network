from page import Page
from database import Database
import json

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

def get_artwork_list(record_list=[]):
	artwork_list=[]
	
	for record in record_list:
		artwork = {}
		for key in record.keys():
			artwork[key] = record[key]
		artwork_list.append(artwork)
	# for record in record_list:
		# artwork = Artwork(*record)
		# artwork_list.append(artwork)
	return artwork_list

class AsciiArtHandler(Page):
	filename = 'artwork.html'

	def get(self):
		
		
		# return self.render(self.filename, artwork_list=artwork_list)
		return self.render_raw(self.filename)

	def post(self):
		if self.check_valid_cookie():
			print('logged')
			form = self.form()
			subject = form.get('subject')
			content = form.get('content')
			id = form.get('id')
			if subject and content:
				if id:
					Record(id, subject, content).update()
					print('update')
				else:
					Record(0, subject, content).insert()
					print('insert')
			
			
			record_list = Record().retrieve(limit=10)
			artwork_list = get_artwork_list(record_list)
			
			data = json.dumps(artwork_list, ensure_ascii=False)
			with open('./assets/artwork.json', 'w') as f:
				f.write(data)
			# return data
			return self.json_response(data=data)
			# return ArtworkHandler().get()
			# return self.render_raw(self.filename)
		else:
			# print('unlogged')
			return 'signin'

class ArtworkHandler(Page):
	filename = 'artwork.json'
	
	def get(self):
		return self.json_response(self.filename)
