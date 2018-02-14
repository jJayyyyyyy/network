var teamList = [];

var app = new Vue({
	el: '#nba',
	data: {
		teamList: false,
		pathname: ''
	},
	created: function(){
		this.pathname = document.location.pathname;
		this.getTeamList();

	},
	methods: {
		getTeamHomepage: function(conf, col, row){
			var team = getTeam(conf, col, row);
			return team.homepage;
		},
		getTeamLogo: function(conf, col, row){
			var team = getTeam(conf, col, row);
			return team.logo;
		},
		getTeamName: function(conf, col, row){
			var team = getTeam(conf, col, row);
			return team.name;
		},
		getTeamList: function(){
			var APIjson = `${this.pathname}?q=json`;
			var self = this;
			axios.get(APIjson)
				.then(function(resp){
					teamList = resp.data;
					self.teamList = teamList;
				})
		}
	}
})

function getTeamListId(conf, col, row){
	var id = 0;
	if(conf === 'east'){
		id = (col - 1) * 5 + (row - 1);
	}else if(conf === 'west'){
		id = (col - 1) * 5 + (row - 1) + 15;
	}
	return id;
}

function getTeam(conf, col, row){
	var teamListId = getTeamListId(conf, col, row);
	var team = teamList[teamListId];
	return team;
}
