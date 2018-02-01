import requests, json
from io import StringIO

sess = requests.Session()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'mat1.gtimg.com',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

def get_logos():
    url = 'http://mat1.gtimg.com/sports/nba/logo/1602/%d.png'
    for i in range(1, 31):
        try:
            resp = sess.get(url % i, headers=headers)
            with open('%d.png' % i, 'wb') as f:
                f.write(resp.content)
        except:
            pass
        

def get_teams():
    try:
        headers['Host'] = 'matchweb.sports.qq.com'
        url = 'http://matchweb.sports.qq.com/rank/team'
        params = {'competitionId': '100000', 'from': 'NBA_PC'}
        
        resp = sess.get(url, headers=headers, params=params)
        # print(resp.url)
        with open('teams_raw.json', 'w') as f:
            f.write(resp.text)
    except:
        pass
    

def reformat_json():
    with open('teams_raw.json', 'r') as f:
        data = json.loads(f.read())
    data = dict(data[1])
    data['eastsouth'][2]['teamId'] = 30
    new_data = {}
    east = {'eastsouth': data['eastsouth'],
            'central': data['central'],
            'atlantic': data['atlantic']}
    west = {'pacific': data['pacific'],
            'westnorth': data['westnorth'],
            'westsouth': data['westsouth'],}
    new_data['east'] = east
    new_data['west'] = west
    new_data = json.dumps(new_data, ensure_ascii=False)
    with open('teams.json', 'w') as f:
        f.write(new_data)

reformat_json()