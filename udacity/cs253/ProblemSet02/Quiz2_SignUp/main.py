#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, url_for
import Page, Check

app = Flask(__name__)

@app.route('/', methods=['GET'])
def GetRequestHandler():
	return Page.make_page()

def check_login_form(form):
	us_username = form['username']
	us_pd1 = form['password']
	us_pd2 = form['verify']
	us_email = form['email']
	print('%s\t%s\t%s\t%s\n' % (us_username, us_pd1, us_pd2, us_email) )

	checked_form = Page.get_default_form_args()
	checked_form['username'] = us_username
	checked_form['email'] = us_email
	valid = True

	if not Check.valid_username(us_username):
		checked_form['username_error'] = 'Invalid username'
		valid = False
	if not Check.valid_email(us_email):
		checked_form['email_error'] = 'Invalid email'
		valid = False

	if not Check.valid_verify(us_pd1, us_pd2):
		checked_form['verify_password_error'] = 'Password not matched'
		valid = False
	elif not Check.valid_password(us_pd1):
		checked_form['password_error'] = 'Invalid password'
		valid = False

	checked_form['valid'] = valid	
	return checked_form

@app.route('/', methods=['POST'])
def PostRequestHandler():
	form = request.form
	checked_form = check_login_form(form)

	if checked_form.get('valid') == True:
		return redirect(url_for('SuccessLoginHandler', username=form['username']))
	else:
		checked_form.pop('valid')
		return Page.make_page(checked_form)

@app.route('/welcome', methods=['GET'])
def SuccessLoginHandler():
	username = request.args['username']
	return 'Welcome, %s!' % username

if __name__ == '__main__':
	app.run(port=8000, debug=True)
	# app.run(port=8080, host='0.0.0.0', debug=False)

