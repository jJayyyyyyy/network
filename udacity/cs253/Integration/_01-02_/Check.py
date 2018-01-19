import re
import Page

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
	us_username = form['username']
	us_pd1 = form['password']
	us_pd2 = form['verify']
	us_email = form['email']
	print('%s\t%s\t%s\t%s\n' % (us_username, us_pd1, us_pd2, us_email) )

	checked_form = Page.get_default_signup_args()
	checked_form['username'] = us_username
	checked_form['email'] = us_email
	valid = True

	if not valid_username(us_username):
		checked_form['username_error'] = 'Invalid username'
		valid = False
	if not valid_email(us_email):
		checked_form['email_error'] = 'Invalid email'
		valid = False

	if not valid_verify(us_pd1, us_pd2):
		checked_form['verify_error'] = 'Password not matched'
		valid = False
	elif not valid_password(us_pd1):
		checked_form['password_error'] = 'Invalid password'
		valid = False

	if valid:
		checked_form['valid'] = valid
	return checked_form