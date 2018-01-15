from flask import render_template
from Art import ArtWork

def fill_template(name='index', **kw):
	filename = name + '.html'
	return render_template(filename, **kw)

def render_index():
	page = fill_template('index')
	return page

def render_art(error='', record_list=[]):
	if error:
		page = fill_template('art', error=error)
	else:
		artwork_list = []
		for record in record_list:
			artwork = ArtWork(*record)
			artwork_list.append(artwork)
		page = fill_template('art', artwork_list=artwork_list)
	return page