# https://docs.python.org/3/library/socket.html#example
import socket

HOST = '127.0.0.1'
PORT = 8888
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall('Hello, world'.encode('utf-8'))
	data = s.recv(1024)
print('msg from server: ', repr(data))
