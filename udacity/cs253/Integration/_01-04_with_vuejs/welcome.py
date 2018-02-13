from page import Page

class WelcomeHandler(Page):
	filename = 'welcome/welcome.html'
	def get(self):
		if self.check_valid_cookie():
			if self.get_args('q') == 'json':
				username = self.cookies().get('username')
				user = [{'username': username}]
				return self.json_response(user)
			else:
				referer = self.get_referer()
				return self.render_raw(self.filename)
		else:
			return self.redirect('/')