import hmac
from flask import render_template, request, redirect, make_response
from flask.views import MethodView
import json
import os.path
from time import time, gmtime, strftime
from datetime import datetime, date

hkey = 'DK'.encode()

class Page(MethodView):
	def hsts(self, resp):
		resp = make_response(resp)
		resp.headers['Strict-Transport-Security'] = 'max-age=15768000'
		return resp
	
	def render(self, filename='', **kw):
		return self.hsts(render_template(filename, **kw))
		
	def render_raw(self, filename):
		filename = './static/%s' % filename
		with open(filename, 'r') as f:
			return self.hsts(f.read())

	def redirect(self, target):
		return self.hsts(redirect(target))

	def get_referer(self):
		return request.headers.get('referer')

	def get_date(self, year=0, month=0, day=0):
		if year and month and day:
			return date(year, month, day)
		else:
			return date.today()

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
			target = '/welcome'
			if self.get_args('redirect'):
				# /welcome?redirect=/blog/new 
				target += '?redirect=%s' % self.get_args('redirect')
			resp = make_response(self.redirect(target))
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

	def json_response(self, record_list=[], data=''):
		if record_list:
			item_list = []
			for record in record_list:
				item = {}
				for key in record.keys():
					item[key] = record[key]
				item_list.append(item)
			data = json.dumps(item_list, ensure_ascii=False)
		resp = make_response(data)
		resp.headers['content-type'] = 'application/json'
		# resp.headers['last-modified'] = strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
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

def check_secure_cookie(val, username):
	if val:
		uid = val.split('|')[0]
		us_val = make_secure_cookie(uid, username)
		return val == us_val
	