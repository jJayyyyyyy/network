// The raw data to observe
var maxVal = 90
var center = {
	x: maxVal,
	y: maxVal
}

var stats = [
	{ label: 'A', value: maxVal/2 },
	{ label: 'B', value: maxVal/3 },
	{ label: 'C', value: maxVal/5 },
	{ label: 'D', value: maxVal - 60 },
	{ label: 'E', value: maxVal - 50}
]

function getPointList(stat_list){
	var total = stat_list.length
	var pointList = []
	for(let i=0; i<total; i++ ){
		var stat = stat_list[i]
		var point = valueToPoint(stat.value, i, total)
		console.log(point)
		pointList.push(`${point.x}, ${point.y}`)
	}
	// pointList = pointList.join[' ']
	console.log(pointList)
	return pointList
}

// A resusable polygon graph component
Vue.component('polygraph', {
		props: ['stats'],
		template: '#polygraph-template',
		computed: { // a computed property for the polygon's points
								points: function () {
									var total = this.stats.length
									var points = this.stats.map(function (stat, i) {
										var point = valueToPoint(stat.value, i, total)
										return `${point.x}, ${point.y}`
									}).join(' ')
									return points
								},
								base1: function() {return getBase(1, this.stats.length)},
								base2: function() {return getBase(2, this.stats.length)},
								base3: function() {return getBase(3, this.stats.length)},
								base4: function() {return getBase(4, this.stats.length)},
								axis: function() {return getAxis(4, this.stats.length)}
		},
		components: {
									// a sub component for the labels
									'axis-label': {
										props: {
											stat: Object,
											index: Number,
											total: Number
										},
										template: '#axis-label-template',
										computed: {
										point: function () {
											return valueToPoint(
											+this.stat.value + 10,
											this.index,
											this.total
											)
										}
										}
									}
								}
})

// math helper...
function valueToPoint (value, index, total) {
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

function getBase (level, total) {
	var base = []
	for(let i=0; i < total; i++){
		var point = valueToPoint(maxVal/4*level, i, total);
		base.push(`${point.x},${point.y}`)
	}
	return base.join(' ')
}

function getAxis(level, total){
	var axis = []
	for (let i = 0; i < total; i++ ){
		var point = valueToPoint(maxVal, i, total);
		axis.push(`${point.x},${point.y}`)
		axis.push(`${center.x},${center.y}`)
	}
	return axis.join(' ')
}

// bootstrap the demo
new Vue({
	el: '#demo',
	data: {
	newLabel: '',
	stats: stats
	},
	methods: {
	add: function (e) {
		e.preventDefault()
		if (!this.newLabel) return
		this.stats.push({
		label: this.newLabel,
		value: maxVal
		})
		this.newLabel = ''
	},
	remove: function (stat) {
		if (this.stats.length > 3) {
		this.stats.splice(this.stats.indexOf(stat), 1)
		} else {
		alert('Can\'t delete more!')
		}
	}
	}
})