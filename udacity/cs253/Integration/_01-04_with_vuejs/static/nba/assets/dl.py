import requests, json, time
from io import StringIO
import logging

sess = requests.Session()
headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Host': 'nba.stats.qq.com',
	'Cache-Control': 'no-cache',
	'Pragma': 'no-cache',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

def get_team_list_raw():
	headers['Host'] = 'matchweb.sports.qq.com'
	url = 'http://matchweb.sports.qq.com/rank/team'
	params = {'competitionId': '100000', 'from': 'NBA_PC'}
	try:
		resp = sess.get(url, headers=headers, params=params).text
		resp = resp.lstrip('[0,').rstrip(',""]')
		data = json.loads(resp)
		for i in range(5):
			if '30.png' in data['eastsouth'][i]['badge']:
				data['eastsouth'][i]['teamId'] = 30
		with open('team_list_raw.json', 'w') as f:
			f.write(json.dumps(data))
	except Exception as e:
		logging.exception(e)

## param: teamQqId
## return: {'rank': {statRank} }
def get_team_stat(teamQqId):
	headers['Host'] = 'ziliaoku.sports.qq.com'
	url = 'http://ziliaoku.sports.qq.com/cube/index'
	params = {  'cubeId': '12',
				'dimId': '3,4,12,13',
				'from': 'sportsdatabase',
				'params': 't1:%d' % teamQqId}
	
	team_stat = {}
	try:
		resp = sess.get(url, headers=headers, params=params).text
		data = json.loads(resp)['data']
		data['regStatRank'].pop('teamId')
		team_stat = {'rank': data['regStatRank']}
	except Exception as e:
		logging.exception(e)
	
	time.sleep(2)
	return team_stat

def make_team_list():
	league = {
		'east': ['eastsouth', 'central', 'atlantic'],
		'west': ['pacific', 'westnorth', 'westsouth']
	}
	with open('team_list_raw.json') as f:
		data = json.loads(f.read())
	
	team_list = []
	for conf, regionList in sorted(league.items()):
		print(conf)
		for region in regionList:
			qq_team_list = data[region]
			for qq_team in qq_team_list:
				teamQqId = int(qq_team['teamId'])
				name = qq_team['name']
				team = {}
				team['teamQqId'] = teamQqId
				team['teamListId'] = len(team_list)
				team['stat'] = get_team_stat(teamQqId)
				team['name'] = name
				team['homepage'] = 'http://nba.stats.qq.com/team/?id=%d' % teamQqId
				team['logo'] = '/static/nba/assets/logo/%d.png' % teamQqId
				team['conference'] = conf
				team['region'] = region
				team_list.append(team)
				print(teamQqId, name)

	data = json.dumps(team_list, ensure_ascii=False)
	with open('team_list.json', 'w') as f:
		f.write(data)

def update():
	get_team_list_raw()
	make_team_list()

update()

# TODO crontab
# get_stats()
# update_team_stats()
