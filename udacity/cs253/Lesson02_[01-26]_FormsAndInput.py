#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# use Flask instead of webapp2
from flask import Flask
from flask import Response
# from flask import Request
from flask import request
app = Flask(__name__)

checkbox = '''
<form method="post" action="/checkbox">
	<input type="checkbox" name="q">
	<input type="submit">
</form>
'''

radiobox = '''
<form>
	<label>
		A
		<input type="radio" name="r" value="a">
	</label>
	<br>
	<label>
		B
		<input type="radio" name="r" value="b">
	</label>
	<br>
	<label>
		C
		<input type="radio" name="r" value="c">
	</label>
	<br>
	<input type="submit">
</form>
'''

dropdown = '''
<form>
	<select name="q">
		<option value="1">a</option>
		<option value="2">b</option>
		<option value="3">c</option>
	</select>
	<br><br>
	<input type="submit">
</form>
'''

form = '''\
<form method="post" action="/form">
	<br>
	<label>
		username
		<input name="username">
	</label>
	<br><br>
	<label>
		password
		<input name="password" type="password">
	</label>
	<br><br>
	<input type="submit">
</form>
'''

@app.route('/', methods=['GET'])
def HomePage():
	return dropdown

@app.route('/checkbox', methods=['POST'])
def tCheckBox():
	print(request.get_data())
	print(request.form['q'])
	return request.get_data()

@app.route('/form', methods=['GET', 'POST'])
def tForm():
	if request.method == 'GET':
		res = request.url + str(request.headers)
		return Response(response=res, content_type='text/plain')
	else:
		print(request.get_data())
		return Response(response=request.get_data(), content_type='text/plain')

if __name__ == '__main__':
	app.run(port=8000, debug=True)
