import re

re_username = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
re_password = re.compile(r'^.{3,20}$')
re_email = re.compile(r'^[\S]+@[\S]+.[\S]+$')

def valid_username(username):
	return re_username.match(username)

def valid_password(password):
	return re_password.match(password)

def valid_verify(pd1, pd2):
	return pd1 == pd2

def valid_email(email):
	if not email:
		return True
	else:
		return re_email.match(email)
