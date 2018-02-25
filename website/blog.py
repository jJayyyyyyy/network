from page import Page
from database import Database

class Post(object):
	def __init__(self, id='', update_date='', subject='', content=''):
		self.id = id
		self.update_date = update_date
		self.subject = subject
		self.content = content

class Record(Post):
	def insert(self):
		query = 'insert into posts (update_date, subject, content) values (?, ?, ?)' 
		args = (self.update_date, self.subject, self.content)	
		return Database().query_db(query, args)

	def update(self):
		query = 'update posts set update_date = ?, subject = ?, content = ? where id = ?'
		args = (self.update_date, self.subject, self.content, self.id)
		return Database().query_db(query, args)

	def retrieve(self, id=0, limit=10):
		if id > 0:
			query = 'select * from posts where id = %d' % id	
		else:
			query = 'select * from posts order by id desc limit %d' % limit
		return Database().query_db(query)

	def delete(self):
		query = 'delete from posts where id = ?'
		args = (self.id, )
		return Database().query_db(query, args)

class BlogIndexHandler(Page):
	filename = 'blog/index/index.html'
	
	def get(self):
		if self.get_args('q') == 'json':
			record_list = Record().retrieve(limit=10)
			return self.json_response(record_list)
		else:
			return self.render_raw(self.filename)

class BlogPostHandler(Page):
	filename = 'blog/post/post.html'
	
	def get(self, id):
		if self.get_args('q') == 'json':
			record_list = Record().retrieve(id=id)
			return self.json_response(record_list)
		else:
			return self.render_raw(self.filename)
	
	# update blogpost
	def post(self, id):
		if self.check_valid_cookie():
			print('logged')
			form = self.form()
			subject = form.get('subject')
			content = form.get('content')
			if subject and content:
				update_date = self.get_date()
				Record(id, update_date, subject, content).update()
				return 'updated'
			else:
				return 'invalid form'
		else:
			return 'signin'

class NewBlogpostHandler(Page):
	filename = 'blog/new/new.html'
	def get(self):
		if self.check_valid_cookie():
			return self.render_raw(self.filename)
		else:
			return self.redirect('/signin?redirect=/blog/new')	

	def post(self):
		if self.check_valid_cookie():
			update_date = self.get_date(2018, 1, 1)
			subject = self.form().get('subject')
			content = self.form().get('content')
			if subject and content:
				Record(0, update_date, subject, content).insert()
			# return self.redirect('/blog')
			return '/blog'
		else:
			# do not add param ?redirect=/blog/new
			return self.redirect('/signin')
