##	Intro

*	使用 `Python` 和 `C` 实现了一个简单的 `HTTP client`, 基本功能是通过 `TCP` 向 `server` 发出连接请求, `TCP` 携带的数据遵循 `HTTP` 格式, `request headers` 内容如下

	```
	GET / HTTP/1.1\r\nHost: github.com\r\nConnection: close\r\n\r\n
	```

*	仅用于网络编程学习和 `HTTP` 连接测试, `HTTPS` 需要另外处理

*	目标网站是 `github.com` (如果换成 `sina.com.cn`, 则会返回更多信息)

	`client` 发出 `http request` 访问 `http://github.com` 后, 如果网络正常, 会收到 `server` 发过来的 `http response`, 而且是一条 `302` 重定向信息, 其内容如下

	*	未解码

		```
		b'HTTP/1.1 301 Moved Permanently\r\nContent-length: 0\r\nLocation: https://github.com/\r\nConnection: close\r\n\r\n'
		```

	*	解码后

		```
		HTTP/1.1 301 Moved Permanently
		Content-length: 0
		Location: https://github.com/
		Connection: close


		```

	我们把这个重定向信息(`http response`)打印出来, 然后退出程序, 测试完成

	<br>

##	Reference

*	[TCP 编程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432004374523e495f640612f4b08975398796939ec3c000)

*	[tcp client.c 1](https://blog.csdn.net/u012234115/article/details/54142273)

*	[tcp client.c 2](https://blog.csdn.net/u013377887/article/details/62429457)

*	[gethostbyname](http://man7.org/linux/man-pages/man3/gethostbyname.3.html)

*	[sockaddr_in](https://www.gta.ufrj.br/ensino/eel878/sockets/sockaddr_inman.html)

*	[AF_INET, IPv4](https://stackoverflow.com/questions/1593946/what-is-af-inet-and-why-do-i-need-it)

*	[HTTP - Messages](https://www.tutorialspoint.com/http/http_messages.htm)

*	[HTTP_headers](https://jjayyyyyyy.github.io/2017/05/01/HTTP_headers.html)
