#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket, threading

http_response = '''\
HTTP/1.1 200 OK
content-type: text/html\r\n\r\n\
<h1>Hello world!</h1>
'''

def get_socket():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('0.0.0.0', 8080))
	s.listen(5)
	print('Waiting for connection...')
	return s

def tcp_link(sock, addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(http_response.encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed.' % addr)

def main():
	s = get_socket()
	while True:
		sock, addr = s.accept()
		t = threading.Thread(target=tcp_link, args=(sock, addr))
		t.start()

main()


# 过程：
#
# 1. server监听ip:port
# 2. 浏览器访问server的ip:port，建立socket连接
# 3. server接受请求，建立连接
# 4. 浏览器发起GET类型的http request
# 5. server返回http response，内容包括
#	5.1 status line
#	5.2 headers
#	5.3 content
# 6. 关闭socket
