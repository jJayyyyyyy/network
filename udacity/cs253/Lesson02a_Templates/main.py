#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, url_for
import Page, Check

app = Flask(__name__)

@app.route('/fizzbuzz', methods=['GET'])
def get_fizzbuzz():
	n = request.args.get('n')
	return Page.render_fizzbuzz(n)

@app.route('/', methods=['GET'])
def get_index():
	return Page.render_index()

@app.route('/rot13', methods=['GET'])
def get_rot13():
	return Page.render_rot13()

@app.route('/rot13', methods=['POST'])
def post_rot13():
	text = request.form.get('text')
	return Page.render_rot13(text)

@app.route('/signup', methods=['GET'])
def get_signup():
	return Page.render_signup()

@app.route('/signup', methods=['POST'])
def post_signup():
	checked_form = Check.check_signup_form( request.form )
	if checked_form.get('valid') == True:
		return redirect( url_for( 'get_welcome', username=checked_form.get('username') ) )
	else:
		return Page.render_signup(checked_form)

@app.route('/welcome', methods=['GET'])
def get_welcome():
	username = request.args.get('username')
	return Page.render_welcome(username)

if __name__ == '__main__':
	app.run(port=8000, debug=True)
	# app.run(port=8080, host='0.0.0.0', debug=False)

