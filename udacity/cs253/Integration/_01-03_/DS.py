class Post(object):
	def __init__(self, post_id, update_date, subject, content):
		self.post_id = post_id
		self.update_date = update_date
		self.subject = subject
		self.content = content

class Artwork(object):
	def __init__(self, artwork_id, subject, content):
		self.artwork_id = artwork_id
		self.subject = subject
		self.content = content
