from page import Page

class ROT13Handler(Page):
	filename = 'rot13/rot13.html'
	def get(self):
		return self.render_raw(self.filename)
