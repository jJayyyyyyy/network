def main():
	import socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('github.com', 80))
	s.send(b'GET / HTTP/1.1\r\nHost: github.com\r\nConnection: close\r\n\r\n')
	buf = []

	while True:
		d = s.recv(1024)
		if d:
			buf.append(d)
		else:
			break

	data = b''.join(buf)
	print(data.decode())
	s.close()

if __name__ == '__main__':
	main()