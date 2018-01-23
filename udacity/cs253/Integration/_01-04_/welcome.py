from page import Page

class WelcomeHandler(Page):
	filename = 'welcome.html'
	def get(self):
		username = self.get_args('username')
		return self.render(self.filename, username=username)
