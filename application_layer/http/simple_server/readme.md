##	过程：

1.	server监听ip:port

2.	浏览器访问server的ip:port，建立socket连接

3.	server接受请求，建立连接

4.	浏览器发起GET类型的http request

5.	server返回http response，内容包括

	*	status line
	*	headers
	*	content

6.	关闭socket