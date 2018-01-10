from html import escape

head = '''
<head>
	<title>Sign Up</title>
		<style type="text/css">
			.label {text-align: right}
			.error {color: red}
	</style>
</head>
'''

body = '''
<body>
	<h2>Signup</h2>
	%(form)s
</body>
'''

form = '''\
<form method="post">
	<table>
		<tr>
			<td class="label">Username</td>
			<td><input type="text" name="username" value="%(username)s"></td>
			<td class="error">%(username_error)s</td>
		</tr>
		<tr>
			<td class="label">Password</td>
			<td><input type="password" name="password" value="%(password)s"></td>
			<td class="error">%(password_error)s</td>
		</tr>
		<tr>
			<td class="label">Verify Password</td>
			<td><input type="password" name="verify" value="%(verify)s"></td>
			<td class="error">%(verify_error)s</td>
		</tr>
		<tr>
			<td class="label">Email (Optional)</td>
			<td><input type="text" name="email" value="%(email)s"></td>
			<td class="error">%(email_error)s</td>
		</tr>
	</table>
	<input type="submit">
</form>
'''

def get_default_form_args():
	return {
		'username': '',
		'username_error': '',
		'password': '',
		'password_error': '',
		'verify': '',
		'verify_error': '',
		'email': '',
		'email_error': ''
	}

default_form_args = get_default_form_args()

def make_page(form_args=default_form_args):
	form_args = dict( (key, escape(val)) for (key, val) in form_args.items() )
	m_form = form % form_args
	m_body = body % {'form': m_form}
	m_page = '<html>%(head)s%(body)s</html>' % {'head': head, 'body': m_body}
	return m_page
