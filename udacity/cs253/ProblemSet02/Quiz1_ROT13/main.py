#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, url_for
import ROT13, Page

app = Flask(__name__)

@app.route('/', methods=['GET'])
def GetRequestHandler():
	return Page.make_page()

@app.route('/', methods=['POST'])
def PostRequestHandler():
	text = ROT13.encode( request.form['text'] )
	return Page.make_page(text=text)

if __name__ == '__main__':
	app.run(port=8000, debug=True)
