import re
from page import Page
from database import Database

UNUSED = 0

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


def hash(pw):
	return pw

class User(object):
	def __init__(self, **form):
		self.username = form.get('username')
		pw = form.get('password')
		self.pw_hash = pw # HASH
		self.email = form.get('email')
		# self.username = username
		# self.pw_hash = get_pw_hash(username, pw)
		# self.email = email

class Record(User):
	def insert(self):
		query = 'insert into users (username, pw_hash, email) values (?, ?, ?)'
		args = (self.username, self.pw_hash, self.email)
		return Database().query_db(query, args)

	def retrieve(self):
		query = 'select * from users where username = ?'
		args = (self.username, )
		record_list = Database().query_db(query, args)
		if record_list == []:
			return None
		else:
			return record_list[0]

	def update(self):
		query = 'update users set pw_hash = ?, email = ? where username = ?'
		args = (self.pw_hash, self.email, self.username)
		return Database().query_db(query, args)

def check_valid(form):
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
		for item in form.items():
			print(item)
		form['password'] = form['verify'] = ''
	return form

def check_usable(form):
	print(form)
	if Record(**form).retrieve() == None:
		form['usable'] = True
	else:
		form['username_error'] = 'Username already taken, please choose another one.'
	return form

class SignupHandler(Page):
	filename = 'signup.html'

	def get(self):
		return self.render(self.filename)

	def post(self):
		# check if valid
		form = check_valid( self.form() )
		if form.get('valid') == True:
			# check if exist
			form = check_usable(self.form())
			if form.get('usable') == True:
				return self.register(form)
		return self.render(self.filename, **form)

	def register(self, form):
		# insert database
		Record(**form).insert()
		return 'Welcome, %s' % form.get('username')
		# login, cookie thing

		return self.login()
		
		# return self.login()
		# redirect
		# return self.redirect('/')
		
class SigninHandler(Page):
	filename = 'signin.html'

	def get(self):
		return self.render(self.filename)

	def post(self):
		us_name = self.form().get('username')
		us_pw = self.form().get('password')
		
		record = Record(username=us_name).retrieve()
		if record:
			s_user_id = record[0]
			s_username = record[1]
			s_pw_hash = record[2]
			if us_pw == s_pw_hash:
				return self.login(user_id=str(s_user_id))
		error = 'invalid login'
		return self.render(self.filename, error=error)
		
class SignoutHandler(Page):
	def get(self):
		return self.logout()
