from page import Page

class FizzBuzzHandler(Page):
	filename = './templates/fizzbuzz.html'
	def get(self):
		with open(self.filename, 'r') as f:
			return f.read()
		# fizzbuzz_strn = self.get_args('fizzbuzz_strn')
		# fizzbuzz_list = get_fizzbuzz_list(fizzbuzz_strn)
		# return self.render(self.filename, fizzbuzz_list=fizzbuzz_list)
