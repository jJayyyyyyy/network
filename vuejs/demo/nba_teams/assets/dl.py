import requests, json, time
from io import StringIO

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

def get_logos():
    headers['Host'] = 'mat1.gtimg.com'
    url = 'http://mat1.gtimg.com/sports/nba/logo/1602/%d.png'
    for i in range(1, 31):
        try:
            resp = sess.get(url % i, headers=headers)
            with open('%d.png' % i, 'wb') as f:
                f.write(resp.content)
        except:
            pass
        
def get_teams_raw():
    headers['Host'] = 'matchweb.sports.qq.com'
    url = 'http://matchweb.sports.qq.com/rank/team'
    params = {'competitionId': '100000', 'from': 'NBA_PC'}
    try:
        resp = sess.get(url, headers=headers, params=params).text
        resp = resp.lstrip('[0,').rstrip(',""]')
        with open('teams_raw.json', 'w') as f:
            f.write(resp)
    except:
        pass


def get_stats():
    headers['Host'] = 'ziliaoku.sports.qq.com'
    url = 'http://ziliaoku.sports.qq.com/cube/index'
    params = {  'cubeId': '12',
                'dimId': '3,4,12,13',
                'from': 'sportsdatabase'
    }
    all_stats = {}
    for id in range(1, 31):
        all_stats[str(id)] = {}
        params['params'] = 't1:%d' % id
        try:
            resp = sess.get(url, headers=headers, params=params).text
            data = json.loads(resp)['data']
            all_stats[str(id)]['statRank'] = data['regStatRank']
            all_stats[str(id)]['statAssociation'] = data['nbaTeamUnionRegSeasonStat']
            all_stats[str(id)]['statTeam'] = data['nbaTeamRegSeasonStat']
        except Exception as e:
            print(e)
        time.sleep(2)

    all_stats = json.dumps(all_stats, ensure_ascii=False)
    with open('stats.json', 'w') as f:
        f.write(all_stats)

def filter_teams(team_list):
	new_team_list = []
	for i in range(5):
		team = team_list[i]
		new_team = {}
		new_team['name'] = team['name']
		new_team['teamId'] = team['teamId']
		new_team_list.append(new_team)
	return new_team_list

def get_teams():
	with open('teams_raw.json', 'r') as f:
		data = json.loads(f.read()) # type(data) ==> dict
	data['eastsouth'][2]['teamId'] = '30'

	new_data = {
		'east': {
			'atlantic': filter_teams(data['atlantic']),
			'central': filter_teams(data['central']),
			'eastsouth': filter_teams(data['eastsouth'])
		},
		'west': {
			'pacific': filter_teams(data['pacific']),
			'westnorth': filter_teams(data['westnorth']),
			'westsouth': filter_teams(data['westsouth'])
		}
	}

	new_data = json.dumps(new_data, ensure_ascii=False) # in case javascript can't read 'key' in str_json
	with open('teams.json', 'w') as f:
		f.write(new_data)

def update_team_stats():
	with open('stats.json', 'r') as f:
		stats = json.loads(f.read())

	with open('teams.json', 'r') as f:
		data = json.loads(f.read())

	for conf in data:	
		for region in data[conf]:
			for i in range(5):
				team = data[conf][region][i]
				teamId = team['teamId']
				stat = stats[teamId]
				team['statRank'] = stat['statRank']
				team['statTeam'] = stat['statTeam']
				team['statAssociation'] = stat['statAssociation']
				data[conf][region][i] = team

	data = json.dumps(data, ensure_ascii=False)
	with open('teams.json', 'w') as f:
		f.write(data)

# TODO crontab
# get_stats()
# update_team_stats()
