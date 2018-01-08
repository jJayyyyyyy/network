import html

form = '''\
<form method="post">
	What is your birthday?
	<br><br>
	<label>
		month
		<input type="text" name="month" value="%(month)s">
	</label>
	<label>
		day
		<input type="text" name="day" value="%(day)s">
	</label>
	<label>
		year
		<input type="text" name="year" value="%(year)s">
	</label>
	<div style="color: red">%(error)s</div>
	<br><br>
	<input type="submit">
</form>
'''

def write_form(error='', month='', day='', year=''):
	return form % { 'error': html.escape(error),
                        'month': html.escape(month),
                        'day': html.escape(day),
                        'year': html.escape(year)}

