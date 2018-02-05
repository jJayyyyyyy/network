from page import Page

class WelcomeHandler(Page):
	filename = 'welcome.html'
	def get(self):
		username = self.cookies().get('username')
		if username:
			return self.render(self.filename, username=username)
		else:
			return self.redirect('/')