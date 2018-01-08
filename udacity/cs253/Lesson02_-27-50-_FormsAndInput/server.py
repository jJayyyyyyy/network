#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, url_for
# from flask import Response, Request
import CheckDate, Form

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
	return Form.write_form()

@app.route('/', methods=['POST'])
def post():
	us_month = request.form['month']
	us_day = request.form['day']
	us_year = request.form['year']

	s_month = CheckDate.valid_month(us_month)
	s_day = CheckDate.valid_day(us_day)
	s_year = CheckDate.valid_year(us_year)

	if not ( s_month and s_day and s_year ):
		return Form.write_form(error='Invalid Date', month=us_month, day=us_day, year=us_year)
	else:
		return redirect(url_for('SuccessLoginHandler'))

@app.route('/WelcomePage')
def SuccessLoginHandler():
	return "<div style=\"color: red\">Welcome!</div>"

if __name__ == '__main__':
	app.run(port=8000, debug=True)
