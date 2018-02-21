import requests, json, time
import logging

sess = requests.Session()
headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Host': '36kr.com',
	'Connection': 'keep-alive',
	'Cache-Control': 'no-cache',
	'Pragma': 'no-cache',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

def get_readhub():
	url = 'https://api.readhub.me/topic'
	params = {'pageSize': '20'}
	# 前端，一次获取2页，每页20条
	# 后端，3小时更新一次，一次更新20条
	try:
		resp = sess.get(url, headers=headers, params=params).text
		data = json.loads(resp)['data']
		newsList = []
		for item in data:
			news = {}
			news['date'] = item['createdAt']
			news['subject'] = item['title']
			news['content'] = item['summary']
			newsList.append(news)
		with open('readhub.json', 'w') as f:
			f.write(json.dumps(newsList, ensure_ascii=False))
	except Exception as e:
		logging.exception(e)

def get_36kr():
	url = 'https://36kr.com/api/newsflash'
	params = {'per_page': '20'}
	try:
		resp = sess.get(url, headers=headers, params=params).text
		data = json.loads(resp)['data']['items']
		newsList = []
		for item in data:
			news = {}
			news['date'] = item['created_at']
			news['subject'] = item['title']
			news['content'] = item['description']
			newsList.append(news)
		with open('36kr.json', 'w') as f:
			f.write(json.dumps(newsList, ensure_ascii=False))
	except Exception as e:
		logging.exception(e)


def update():
	get_readhub()
	get_36kr()

update()

# TODO crontab

