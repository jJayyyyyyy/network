import re, random, hashlib
from string import ascii_letters as letters
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

def make_salt(length = 5):
	# salt = []
	# for i in range(length):
	# 	salt.append(random.choice(letters))
	# return ''.join(salt)
	return ''.join(random.choice(letters) for x in range(length))

def make_pw_hash(username, password, salt=None):
	if not salt:
		salt = make_salt()
	enc = (username + password + salt).encode('utf-8')
	pw_hash = hashlib.sha256(enc).hexdigest()
	return '%s,%s' % (salt, pw_hash)

def check_pw_hash(username, password, pw_hash):
	salt = pw_hash.split(',')[0]
	return pw_hash == make_pw_hash(username, password, salt)


class User(object):
	def __init__(self, form):
		self.user_id = str(form.get('user_id'))
		self.username = form.get('username')
		self.password = form.get('password')
		self.email = form.get('email')

class Record(User):
	def insert(self):
		query = 'insert into users (username, pw_hash, email) values (?, ?, ?)'
		self.pw_hash = make_pw_hash(self.username, self.password)
		args = (self.username, self.pw_hash, self.email)
		return Database().query_db(query, args)

	def retrieve(self):
		query = 'select * from users where username = ?'
		args = (self.username, )
		record_list = Database().query_db(query, args)
		return record_list

	def update(self):
		query = 'update users set pw_hash = ?, email = ? where username = ?'
		self.pw_hash = make_pw_hash(self.password)
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
		form['password'] = form['verify'] = ''
	return form

def check_usable(form):
	if not Record(form).retrieve():
		form['usable'] = True
	else:
		form['username_error'] = 'Username already taken, please choose another one.'
	return form

class SignupHandler(Page):
	filename = 'signup.html'
	def get(self):
		return self.render(self.filename)

	def post(self):
		form = check_valid(self.form() )	# check if valid
		if form.get('valid') == True:
			form = check_usable(self.form())	# check if exist
			if form.get('usable') == True:
				return self.register(form)
		return self.render(self.filename, **form)

	def register(self, form):
		Record(form).insert()
		record_list = Record(form).retrieve()
		if record_list:
			user = User(form)
			return self.login(user)	# login and set cookie
		else:
			return 'Oops...something went wrong...'
		
class SigninHandler(Page):
	filename = 'signin.html'
	def get(self):
		if self.check_valid_cookie():
			return self.redirect('/welcome')
		else:
			return self.render(self.filename)

	def post(self):
		us_form = self.form()
		record_list = Record(us_form).retrieve()
		if record_list:
			us_username = us_form.get('username')
			us_pw = us_form.get('password')
			record = dict(record_list[0])
			pw_hash = record.get('pw_hash')
			if check_pw_hash(us_username, us_pw, pw_hash):
				user = User(record)
				return self.login(user)# sign in and set cookie
		return self.render(self.filename, error='invalid login')
		
class SignoutHandler(Page):
	def get(self):
		return self.logout()
