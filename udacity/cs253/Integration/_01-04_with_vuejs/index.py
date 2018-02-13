from page import Page

class IndexHandler(Page):
	filename = 'index/index.html'
	def get(self):
		return self.render_raw(self.filename)
