from page import Page

class NBAHandler(Page):
	filename = 'nba/nba.html'

	def get(self):
		if self.get_args('q') == 'json':
			with open('./static/nba/assets/team_list.json') as f:
				data = f.read()
			return self.json_response(data=data)
		else:
			return self.render_raw(self.filename)
