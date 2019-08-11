# https://docs.python.org/3/library/socket.html#example
import socket
server_host = '0.0.0.0'
port = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((server_host, port))
	s.listen(1)
	conn, addr = s.accept()
	with conn:
		print('Client: ', addr)
		while True:
			data = conn.recv(1024)
			if not data:
				break
			conn.sendall('received\n'.encode('utf-8'))
