from page import Page
from database import Database

class Post(object):
	def __init__(self, post_id='', update_date='', subject='', content=''):
		self.post_id = post_id
		self.update_date = update_date
		self.subject = subject
		self.content = content

class Record(Post):
	def insert(self):
		query = 'insert into posts (update_date, subject, content) values (?, ?, ?)' 
		args = (self.update_date, self.subject, self.content)	
		return Database().query_db(query, args)

	def update(self):
		query = 'update posts set update_date = ?, subject = ?, content = ? where post_id = ?'
		args = (self.update_date, self.subject, self.content, self.post_id)
		return Database().query_db(query, args)

	def retrieve(self, post_id=0, limit=10):
		if post_id > 0:
			query = 'select * from posts where post_id = %d' % post_id	
		else:
			query = 'select * from posts order by post_id desc limit %d' % limit
		return Database().query_db(query)

	def delete(self):
		query = 'delete from posts where post_id = ?'
		args = (self.post_id, )
		return Database().query_db(query, args)

def get_post_list(record_list=[]):
	post_list = []
	for record in record_list:
		post = Post(*record)
		post_list.append(post)
	return post_list

def get_post(record_list=[]):
	if record_list:
		record = record_list[0]
		post = Post(*record)
		return post

class BlogIndexHandler(Page):
	filename = 'blog_index.html'
	def get(self):
		record_list = Record().retrieve(limit=10)
		post_list = get_post_list(record_list)
		return self.render(self.filename, post_list=post_list)
	
class GetPostHandler(Page):
	filename = 'blog_post.html'
	def get(self, post_id):
		record_list = Record().retrieve(post_id=post_id)
		post = get_post(record_list)
		return self.render(self.filename, post=post)

class NewPostHandler(Page):
	filename = 'blog_new_post.html'
	def get(self):
		if self.check_valid_cookie():
			return self.render(self.filename)
		else:
			return self.redirect('/signin')	

	def post(self):
		if self.check_valid_cookie():
			update_date = self.get_date(2018, 1, 1)
			subject = self.form().get('subject')
			content = self.form().get('content')
			if subject and content:
				Record(0, update_date, subject, content).insert()
			return self.redirect('/blog')
		else:
			return self.redirect('/signin')	

class EditPostHandler(Page):
	filename = 'blog_edit_post.html'
	def get(self, post_id):
		if self.check_valid_cookie():
			record_list = Record().retrieve(post_id=post_id)
			post = get_post(record_list)
			return self.render(self.filename, post=post)
		else:
			return self.redirect('/signin')	

	def post(self, post_id):
		if self.check_valid_cookie():
			update_date = self.get_date()
			subject = self.form().get('subject')
			content = self.form().get('content')
			if subject and content:
				Record(post_id, update_date, subject, content).update()
			return self.redirect('/blog/%d' % post_id)
		else:
			return self.redirect('/signin')	