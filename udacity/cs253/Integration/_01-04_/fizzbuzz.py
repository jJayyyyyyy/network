from page import Page

def get_fizzbuzz_list(fizzbuzz_strn, limit=30):
	fizzbuzz_list = []
	if fizzbuzz_strn and fizzbuzz_strn.isdigit():
		fizzbuzz_n = int(fizzbuzz_strn)
		if fizzbuzz_n > limit:
			fizzbuzz_n = limit
		for i in range(1, fizzbuzz_n + 1):
			if not i % 15:
				item = 'FizzBuzz'
			elif not i % 3:
				item = 'Fizz'
			elif not i % 5:
				item = 'Buzz'
			else:
				item = str(i)
			fizzbuzz_list.append(item)
	return fizzbuzz_list

class FizzBuzzHandler(Page):
	filename = 'fizzbuzz.html'
	def get(self):
		fizzbuzz_strn = self.get_args('fizzbuzz_strn')
		fizzbuzz_list = get_fizzbuzz_list(fizzbuzz_strn)
		return self.render(self.filename, fizzbuzz_list=fizzbuzz_list)
