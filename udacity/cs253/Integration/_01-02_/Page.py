import os
from html import escape

def fill_template(name='index', **kw):
	try:
		filename = '%s.html' % name
		path = os.path.join('.', 'templates', filename)
		with open(filename, 'r') as f:
			page = f.read()
		args = dict( (key, escape(val)) for (key, val) in kw.items() )
		return page % args
	except:
		return 'Page Not Found!'

def get_default_signup_args():
	return {'username': '',
			'username_error': '',
			'password_error': '',
			'verify_error': '',
			'email': '',
			'email_error': ''}

def render_index():
	page = fill_template('index')
	return page

def render_rot13(text=''):
	args = {'text': text}
	return fill_template('rot13', **args)

def render_signup(form={}):
	if form:
		args = form
	else:
		args = get_default_signup_args()
	print(args)
	return fill_template('signup', **args)

def render_welcome(username=''):
	if username:
		args = {'username': username, 'a': 'a'}
		return fill_template('welcome', **args)
	else:
		return 'Invalid username<br><br><a href="/">Back</a>'
