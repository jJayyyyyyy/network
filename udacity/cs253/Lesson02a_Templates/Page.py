from html import escape
from flask import render_template # flask will help us auto escape html
import os
import ROT13, FizzBuzz

def fill_template(name='index', **kw):
	filename = '%s.html' % name
	return render_template(filename, **kw)

def get_default_signup_args():
	return {'username': '',
			'username_error': '',
			'password_error': '',
			'verify_error': '',
			'email': '',
			'email_error': ''}

def render_fizzbuzz(n):
	fizzbuzz = FizzBuzz.get(n)
	page = fill_template('fizzbuzz', FizzBuzz=fizzbuzz)
	return page

def render_index():
	page = fill_template('index')
	return page

def render_rot13(text=''):
	text = ROT13.encode(text)
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
