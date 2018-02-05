from page import Page
import codecs

class ROT13Handler(Page):
	filename = 'rot13.html'
	def get(self):
		return self.render(self.filename)

	def post(self):
		rot13_text = self.form().get('rot13_text')
		if rot13_text:
			rot13_text = codecs.encode(rot13_text, ('rot13'))
		return self.render(self.filename, rot13_text=rot13_text)
