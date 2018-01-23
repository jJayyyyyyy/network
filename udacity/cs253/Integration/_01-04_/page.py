from flask import render_template, request, redirect, make_response
from flask.views import MethodView
import datetime

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


	def logout(self):
		resp = make_response(self.redirect('/'))
		resp.set_cookie(key='user_id', value='', max_age=5)
		return resp

	# cookie 用user_id + secret(fixed) 进行hmac
	# pw_hash 用pw + salt(random) 进行hash
	def login(self, user_id):
		resp = make_response(self.redirect('/'))
		key = 'user_id'
		val = user_id
		resp.set_cookie(key, val)
		# self.set_secure_cookie('user_id', str(user_id))
		return resp

	def set_secure_cookie(self, id):
		val = make_cookie_val(id)
		response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/;' % val)

	def reset_cookie(self):
		response.headers.add_header('Set-Cookie', 'user_id=; Path=/;')

def make_cookie_val(user_id):
	h_val = hmac.new(user_id, secret).hexdigest()
	return '%s|%s' % (user_id, h_val)

def check_cookie_val(val):
	pass