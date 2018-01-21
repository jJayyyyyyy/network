import re
import page

re_username = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
def valid_username(username):
	return re_username.match(username)

re_password = re.compile(r'^.{3,20}$')
def valid_password(password):
	return re_password.match(password)

re_email = re.compile(r'^[\S]+@[\S]+.[\S]+$')
def valid_verify(pd1, pd2):
	return pd1 == pd2

def valid_email(email):
	if not email:
		return True
	else:
		return re_email.match(email)

def check_signup_form(form):
	for item in form.items():
		print(item)
	valid = True

	if not valid_username( form['username'] ):
		form['username_error'] = 'Invalid username'
		valid = False
	if not valid_email( form['email'] ):
		form['email_error'] = 'Invalid email'
		valid = False
	if not valid_verify( form['password'], form['verify'] ):
		form['verify_error'] = 'Password not matched'
		valid = False
	elif not valid_password( form['password'] ):
		form['password_error'] = 'Invalid password'
		valid = False

	if valid:
		form['valid'] = valid
	else:
		form['password'] = form['verify'] = ''
	return form

