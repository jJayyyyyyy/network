from page import Page

class FizzBuzzHandler(Page):
	filename = 'fizzbuzz.html'
	def get(self):
		return self.render_raw(self.filename)
