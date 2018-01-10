from html import escape

title = '<h2>ROT13:</h2>'

form = '''\
<form method="post">
	<textarea name="text" style="height: 100px; width: 400px;">%(text)s</textarea>
	<br>
	<input type="submit">
</form>
'''

def make_page(text=''):
	page = title + form % { 'text': escape(text)}
	return page
