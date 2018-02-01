var url_teams = './assets/teams.json'
var nbateams = null

var app = new Vue({
	el: '#app',
	data: {
		conference: ['east', 'west'],
		eastRegions: ['eastsouth', 'central', 'atlantic'],
		westRegions: ['pacific', 'westnorth', 'westsouth'],
		currentRegion: '',
		range: [0, 1, 2, 3, 4],
		// teams: null,
		teams_east: null,
		teams_west: null,
		message: null
	},

	created: function () {  this.fetchData()  },

	// watch: {
	// 	teams: 'getTeams'
	// },

	// text formatting
	filters: {
		getImage: function(teamId){
			return `./assets/${teamId}.png`
		}
	},

	methods: {
		fetchData: function () {
			var xhr = new XMLHttpRequest()
			var self = this
			xhr.onreadystatechange = function(){
				if(xhr.readyState === 4 && xhr.status === 200){
					nbateams = JSON.parse(xhr.responseText)
					// self.teams = nbateams
					self.teams_east = nbateams['east']
					self.teams_west = nbateams['west']
				}
			}
			xhr.open('GET', url_teams);
			xhr.send()
		},
		getTeams: function(){
			this.teams = nbateams
		},
		getRegion: function(){
			this.teams = nbateams
		}
	}
})
