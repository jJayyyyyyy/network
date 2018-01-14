from wsgiref.simple_server import make_server

def application(environ, start):
	content = [b'<h1>Hello, world!</h1>']
	start('200 OK', [('Content-Type', 'text/html')])
	return content

ip = '0.0.0.0'
port = 8000
httpd = make_server(ip, port, application)
httpd.serve_forever()
