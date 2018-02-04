var url_teams = './assets/teams.json'
var nbateams = null
var total = 5
var maxVal = 87
var maxY = 90
var center = {
	x: 150,
	y: 150
}

var stats = [
	{ label: '得分', value: maxVal },
	{ label: '助攻', value: maxVal },
	{ label: '篮板', value: maxVal },
	{ label: '抢断', value: maxVal },
	{ label: '盖帽', value: maxVal }
]

var axisPoints = [
	{x: 137, y:70},
	{x: 221, y:128},
	{x: 192, y:228},
	{x: 88, y:230},
	{x: 45, y:130},
]

Vue.component('polygraph', {
	props: ['stats'],
	template: '#polygraph-template',
	computed: {
		points: function(){
			var points = this.stats.map(function(stat, i){
				var point = valueToPoint(stat.value, i)
				return `${point.x}, ${point.y}`
			}).join(' ')
			return points
		},
		base1: function() {return getBase(1)},
		base2: function() {return getBase(2)},
		base3: function() {return getBase(3)},
		base4: function() {return getBase(4)},
		axis: function() {return getAxis(4)}
	},
	components: {
		// a sub component for the labels
		'axis-label': {
			props: {
				stat: Object,
				index: Number,
			},
			template: '#axis-label-template',
			computed: {
				point: function () {
					var point =  axisPoints[this.index]
					return point
				}
			}
		}
	}
})

var app = new Vue({
	el: '#app',
	data: {
		conference: ['east', 'west'],
		eastRegions: ['eastsouth', 'central', 'atlantic'],
		westRegions: ['pacific', 'westnorth', 'westsouth'],
		currentRegion: '',
		range: [0, 1, 2, 3, 4],
		currentTeam: null,
		teams_east: null,
		teams_west: null,
		message: null,
		stats: null,
		rankInfo: null
	},

	created: function () {  this.fetchData()  },

	// text formatting
	filters: {
		getImage: function(teamId){
			return `./assets/${teamId}.png`
		},
		getTeamPage: function(teamId){
			return `http://nba.stats.qq.com/team/?id=${teamId}`
		}
	},

	methods: {
		fetchData: function () {
			var xhr = new XMLHttpRequest()
			var self = this
			xhr.onreadystatechange = function(){
				if(xhr.readyState === 4 && xhr.status === 200){
					nbateams = JSON.parse(xhr.responseText)
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
		},
		add: function(){
			if(this.stats[2].value < 80){
				this.stats[2].value += 1
			}
		},
		getChart: function(conf, region, ix){
			if(conf && region){
				var team = nbateams[conf][region][ix-1]
				this.currentTeam = team

				this.updateStats()
			}
		},
		updateStats: function(){
			var rank = this.currentTeam['statRank']
			stats[0].value = maxY - 3*rank['pointsRank']
			stats[1].value = maxY - 3*rank['assistsRank']
			stats[2].value = maxY - 3*rank['reboundsRank']
			stats[3].value = maxY - 3*rank['stealsRank']
			stats[4].value = maxY - 3*rank['blocksRank']
			console.log(stats)
			this.stats = stats
			this.rankInfo = `${this.currentTeam['name']}\n`
							+ `场均数据排名\n`
							+ `[得分]: No.${rank['pointsRank']}\n`
							+ `[助攻]: No.${rank['assistsRank']}\n`
							+ `[篮板]: No.${rank['reboundsRank']}\n`
							+ `[盖帽]: No.${rank['stealsRank']}\n`
							+ `[抢断]: No.${rank['blocksRank']}\n`
		}
	}
})

// math helper...
function valueToPoint (value, index) {
	var x     = 0;
	var y     = -value * 0.8;
	var angle = Math.PI * 2 / total * index;
	var cos   = Math.cos(angle);
	var sin   = Math.sin(angle);
	var tx    = x * cos - y * sin + center.x;
	var ty    = x * sin + y * cos + center.y;
	return {
		x: tx,
		y: ty
	}
}

function getBase (level) {
	var base = []
	for(let i=0; i < total; i++){
		var point = valueToPoint(maxVal*level/4, i);
		base.push(`${point.x},${point.y}`)
	}
	return base.join(' ')
}

function getAxis(level){
	var axis = []
	for (let i = 0; i < total; i++ ){
		var point = valueToPoint(maxVal, i);
		axis.push(`${point.x},${point.y}`)
		axis.push(`${center.x},${center.y}`)
	}
	return axis.join(' ')
}