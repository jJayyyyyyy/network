var teamList = [];
const total = 5;
const maxVal = 87;
const maxY = 90;
const center = {
	x: 150,
	y: 150
}

var labelList = [
	{	x: 137, y:70, name:'得分'	},
	{	x: 221, y:128, name:'助攻'	},
	{	x: 192, y:228, name:'篮板'	},
	{	x: 88, y:230, name:'抢断'	},
	{	x: 45, y:130, name:'盖帽'	}
]

Vue.component('polygraph', {
	template: '#polygraph-template',
	props: ['id'],
	computed: {
		rankPoints: function(){
			return getRankPoints(this.id);
		}
	}
})

Vue.component('polygraph-base', {
	template: '#polygraph-base-template',
	data: function(){
		return {
			base1: getBase(1),
			base2: getBase(2),
			base3: getBase(3),
			base4: getBase(4),
			axis:  getAxis(4),
		}
	}
})

Vue.component('axis-label', {
	template: '#axis-label-template',
	props: ['label']
})


var app = new Vue({
	el: '#nba',
	data: {
		teamList: false,
		pathname: '',
		labelList: labelList,
		curId: '',
		tooltipText: ''
	},
	created: function(){
		this.pathname = document.location.pathname;
		this.getTeamList();

	},
	methods: {
		setCurId: function(conf, col, row){
			this.curId = getTeamListId(conf, col, row);
			this.updateTooltipText();
		},
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
		updateTooltipText: function(){
			var team = teamList[this.curId];
			var name = team['name'];
			var rank = team['stat']['rank'];
			this.tooltipText = `${name}\n`
							+ `场均数据排名\n`
							+ `[得分]: No.${rank['pointsRank']}\n`
							+ `[助攻]: No.${rank['assistsRank']}\n`
							+ `[篮板]: No.${rank['reboundsRank']}\n`
							+ `[盖帽]: No.${rank['stealsRank']}\n`
							+ `[抢断]: No.${rank['blocksRank']}\n`
		},
		getTeamList: function(){
			var APIjson = `${this.pathname}?q=json`;
			var self = this;
			axios.get(APIjson)
				.then(function(resp){
					teamList = resp.data;
					self.teamList = true;
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

function getRankPoints(teamListId){
	var points = [], valY, point;
	var rank = teamList[teamListId]['stat']['rank'];

	valY = maxY - 3*rank['pointsRank'];
	point = valueToPoint(valY, 0);
	points.push(`${point.x},${point.y}`);

	valY = maxY - 3*rank['assistsRank'];
	point = valueToPoint(valY, 1);
	points.push(`${point.x},${point.y}`);

	valY = maxY - 3*rank['reboundsRank'];
	point = valueToPoint(valY, 2);
	points.push(`${point.x},${point.y}`);

	valY = maxY - 3*rank['stealsRank'];
	point = valueToPoint(valY, 3);
	points.push(`${point.x},${point.y}`);

	valY = maxY - 3*rank['blocksRank'];
	point = valueToPoint(valY, 4);
	points.push(`${point.x},${point.y}`);

	return points.join(' ');
}


function getBase (level){
	var base = [];
	for(let i=0; i < total; i++){
		var point = valueToPoint(maxVal*level/4, i);
		base.push(`${point.x},${point.y}`);
	}
	return base.join(' ');
}

function getAxis(level){
	var axis = [];
	for (let i = 0; i < total; i++ ){
		var point = valueToPoint(maxVal, i);
		axis.push(`${point.x},${point.y}`);
		axis.push(`${center.x},${center.y}`);
	}
	return axis.join(' ');
}
