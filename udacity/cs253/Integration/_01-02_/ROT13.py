def encode(text, offset=13):
	s = ''
	for i in range(len(text)):
		if text[i].isalpha():
			if (text[i] >= 'a' and text[i] <= 'm') or (text[i] >= 'A' and text[i] <= 'M'):
				s = s + chr( ord(text[i]) + offset )
			else:
				s = s + chr( ord(text[i]) - offset )
		else:
			s = s + text[i]
	return s