from flask import render_template
from post import Post

def fill_template(name='blog', **kw):
	filename = name + '.html'
	return render_template(filename, **kw)

def render_blog(record_list=[]):
	post_list = []
	for record in record_list:
		post = Post(*record)
		post_list.append(post)
	return fill_template(name='blog', post_list=post_list)

def render_post(record):
	post = None
	if record:
		post = Post(*record)
	return fill_template(name='post', post=post)

def render_new_post(**kw):
	return fill_template(name='new_post', **kw)

def render_edit_post(**kw):
	return fill_template(name='edit_post', **kw)