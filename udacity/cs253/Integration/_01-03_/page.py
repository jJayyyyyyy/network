from flask import render_template
import DS

def fill_template(name='index', **kw):
	filename = name + '.html'
	return render_template(filename, **kw)

class Page(object):
	def __init__(self):
		self.name = 'index'

	def render(self, **kw):
		return fill_template(name=self.name, **kw)

class Index(Page):
	def __init__(self):
		self.name = 'index'

class ROT13(Page):
	def __init__(self):
		self.name = 'rot13'

	def render(self, rot13_text=''):
		rot13_text = self.rotate(rot13_text)
		return fill_template(name=self.name, rot13_text=rot13_text)

	def rotate(self, text, res='', offset=13):
		for ch in text:
			if ch.isalpha():
				if (ch >= 'a' and ch <= 'm') or (ch >= 'A' and ch <= 'M'):
					res = res + chr( ord(ch) + offset )
				else:
					res = res + chr( ord(ch) - offset )
			else:
				res = res + ch
		return res

class FizzBuzz(Page):
	def __init__(self, fizzbuzz_strn):
		self.name = 'fizzbuzz'
		self.fizzbuzz_list = []
		if fizzbuzz_strn and fizzbuzz_strn.isdigit():
			self.fizzbuzz_n = int(fizzbuzz_strn)
			self.get_fizzbuzz_list()

	def render(self):
		return fill_template(name=self.name, fizzbuzz_list=self.fizzbuzz_list)

	def get_fizzbuzz_list(self, limit=30):
		if self.fizzbuzz_n > limit:
			self.fizzbuzz_n = limit
		for i in range(1, self.fizzbuzz_n + 1):
			if not i % 15:
				item = 'FizzBuzz'
			elif not i % 3:
				item = 'Fizz'
			elif not i % 5:
				item = 'Buzz'
			else:
				item = str(i)
			self.fizzbuzz_list.append(item)

class Welcome(Page):
	def __init__(self, username=''):
		self.name = 'welcome'

class AsciiArt(Page):
	def __init__(self):
		self.name = 'ascii_art'

	def render(self, record_list=[], **kw):
		artwork_list = []
		for record in record_list:
			artwork = DS.Artwork(*record)
			artwork_list.append(artwork)
		return fill_template(name=self.name, artwork_list=artwork_list, **kw)

class Blog(Page):
	def __init__(self):
		self.name = 'blog'

	def render_edit_post(self, record, **kw):
		post = DS.Post(*record)
		return fill_template(name='blog_edit_post', post=post, **kw)

	def render_index(self, record_list=[]):
		post_list = []
		for record in record_list:
			post = DS.Post(*record)
			post_list.append(post)
		return fill_template(name='blog_index', post_list=post_list)

	def render_post(self, record):
		post = DS.Post(*record)
		print(post.subject)
		return fill_template(name='blog_post', post=post)

	def render_new_post(self, **kw):
		return fill_template(name='blog_new_post', **kw)
