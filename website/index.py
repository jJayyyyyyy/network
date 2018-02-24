from page import Page
import os.path
from time import time
from subprocess import call

basepath = 'static/index/db/%s'
filename_readhub = basepath % 'readhub.json'
filename_36kr = basepath % '36kr.json'

class IndexHandler(Page):
	filename = 'index/index.html'
	def get(self):
		self.update_json()
		if self.get_args('q') == 'json':
			return self.q_json()

		return self.render_raw(self.filename)

	def update_json(self):
		last_modified_readhub = os.path.getmtime(filename_readhub)
		last_modified_36kr = os.path.getmtime(filename_36kr)
		now = time()
		expires_readhub = now - last_modified_readhub > 3600
		expires_36kr = now - last_modified_36kr > 3600

		# 若本次请求时，距离上一次更新文件已经超过1h，则再次更新文件
		# 通过用户的请求来更新，而不是主动更新，节省资源
		if expires_readhub and expires_36kr:
			filename = basepath % 'get_news.py'
			print(filename)
			call(['python3', filename])
	
	def q_json(self):
		# 对于已经更新过的json数据
		# 由于客户端是通过axios（而不是浏览器）进行json请求的
		# 所以在服务端设置cache-control没有用
		# 服务端只在json_response中添加last-modified
		# 在客户端的app.js，进行逻辑判断，now - last-modified > 120s，则请求json，否则不发起请求
		
		# 取消，缓存的是css, js和png，是html里面固定了的东西
		# 每次刷新都会重新请求的是index.html
		# js没办法获取cache中的json，因此每次都必须重新请求json，否则填充的内容就是空的
		
		if self.get_args('src') == 'readhub':
			with open(filename_readhub) as f:
				return self.json_response(data=f.read())

		if self.get_args('src') == '36kr':
			with open(filename_36kr) as f:
				return self.json_response(data=f.read())