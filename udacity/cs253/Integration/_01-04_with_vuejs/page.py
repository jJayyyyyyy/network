import datetime, hmac
from flask import render_template, request, redirect, make_response, json
from flask.views import MethodView

hkey = 'DK'.encode()

class Page(MethodView):
	def hsts(self, resp):
		resp = make_response(resp)
		resp.headers['Strict-Transport-Security'] = 'max-age=15768000'
		return resp
	
	def render(self, filename='', **kw):
		return self.hsts(render_template(filename, **kw))
		
	def render_raw(self, filename):
		filename = './templates/%s' % filename
		with open(filename, 'r') as f:
			return self.hsts(f.read())

	def redirect(self, url):
		return self.hsts(redirect(url))

	def get_date(self, year=0, month=0, day=0):
		if year and month and day:
			return datetime.date(year, month, day)
		else:
			return datetime.date.today()

	def get_args(self, key):
		return request.args.get(key)

	def form(self):
		form = {}
		if request.is_json:
			form = request.get_json()	# type-dict
		else:
			form = request.form.to_dict()
		return form

	def cookies(self):
		return request.cookies

	def logout(self):
		resp = make_response(self.redirect('/'))
		resp.set_cookie(key='uid', value='', max_age=5)
		resp.set_cookie(key='username', value='', max_age=5)
		return resp

	# cookie 用uid + secret(fixed) 进行hmac
	# pw_hash 用name + pw + salt(random) 进行hash
	def login(self, user):
		if request.is_json:
			resp = make_response('welcome')
		else:
			resp = make_response(self.redirect('/welcome'))
		resp.set_cookie(key='username', value=user.username)
		
		uid = user.uid
		username = user.username
		key = 'uid'
		val = make_secure_cookie(user.uid, username)
		resp.set_cookie(key=key, value=val)
		return resp

	# TODO
	def check_valid_cookie(self):
		val = self.cookies().get('uid')
		username = self.cookies().get('username')
		return check_secure_cookie(val, username)

	def json_response(self, filename='artwork.json', data=''):
		if data:
			resp = make_response(data)
		else:
			with open('./assets/%s' % filename) as f:
				resp = make_response(f.read())
		resp.headers['content-type'] = 'application/json'	
		return resp

	def png_response(self, filename):
		with open('./assets/%s' % filename) as f:
			resp = make_response(f.read())
		resp.headers['content-type'] = 'image/png'
		return resp

def make_secure_cookie(uid, username):
	msg = uid + username
	digest = hmac.new(hkey, msg.encode()).hexdigest()
	val = '%s|%s' % (uid, digest)
	return val

# TODO
def check_secure_cookie(val, username):
	if val:
		uid = val.split('|')[0]
		us_val = make_secure_cookie(uid, username)
		return val == us_val
	