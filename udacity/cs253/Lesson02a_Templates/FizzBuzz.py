def get(n):
	fizzbuzz = []
	if n and n.isdigit():
		n = int(n)
		if n > 30:
			n = 30
		for i in range(1, n+1):
			if not i % 15:
				item = 'FizzBuzz'
			elif not i % 3:
				item = 'Fizz'
			elif not i % 5:
				item = 'Buzz'
			else:
				item = str(i)
			fizzbuzz.append(item)
	return fizzbuzz