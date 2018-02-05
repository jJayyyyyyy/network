from page import Page

class IndexHandler(Page):
	filename = 'index.html'
	def get(self):
		return self.render(self.filename)
