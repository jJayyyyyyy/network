import datetime, hmac
from flask import render_template, request, redirect, make_response
from flask.views import MethodView

hkey = 'DK'.encode()

class Page(MethodView):
	def render(self, filename='', **kw):
		return render_template(filename, **kw)

	def get_args(self, key):
		return request.args.get(key)

	def redirect(self, url):
		return redirect(url)

	def get_date(self, year=0, month=0, day=0):
		if year and month and day:
			return datetime.date(year, month, day)
		else:
			return datetime.date.today()

	def form(self):
		return request.form.to_dict()

	def cookies(self):
		return request.cookies

	def logout(self):
		resp = make_response(self.redirect('/'))
		resp.set_cookie(key='user_id', value='', max_age=5)
		resp.set_cookie(key='username', value='', max_age=5)
		return resp

	# cookie 用user_id + secret(fixed) 进行hmac
	# pw_hash 用name + pw + salt(random) 进行hash
	def login(self, user):
		resp = make_response(self.redirect('/welcome'))
		resp.set_cookie(key='username', value=user.username)
		
		user_id = user.user_id
		username = user.username
		key = 'user_id'
		val = make_secure_cookie(user.user_id, username)
		resp.set_cookie(key=key, value=val)
		return resp

	# TODO
	def check_valid_cookie(self):
		val = self.cookies().get('user_id')
		username = self.cookies().get('username')
		return check_secure_cookie(val, username)

def make_secure_cookie(user_id, username):
	msg = user_id + username
	digest = hmac.new(hkey, msg.encode()).hexdigest()
	val = '%s|%s' % (user_id, digest)
	return val

# TODO
def check_secure_cookie(val, username):
	if val:
		user_id = val.split('|')[0]
		us_val = make_secure_cookie(user_id, username)
		return val == us_val
	