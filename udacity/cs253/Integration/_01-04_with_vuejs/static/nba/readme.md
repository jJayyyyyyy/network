Component template should contain exactly one root element.

要把script给圈起来
http://www.cnblogs.com/liziyou/p/6708537.html


全局变量要放在最上面，否则

func ref

global var

func def

这样是没法引用到全局变量的


##	TODO: 增加radar chart

*	component
*	template
*	数据传递


filters似乎可以用methods里面定义一个function来实现其功能，比如改编一下文档里面的demo

```html
<div id="app">
	<div v-bind:id="id | add1"></div>
	<div v-bind:id="add2(id)"></div>
</div>
```

```javascript
var app = new Vue({
	el: '#app',
	data: {
		id: 1
	},
	filters:{
		add1: function(id){
			return id + 1
		}
	},
	methods:{
		add2: function(id){
			return id + 2
		}
	}
})
```


add1和add2可以实现基本相同的功能。

所以，vuejs中的filters有什么特别之处/优点？有那些场景只能使用filter？

暂时想到的是，如果定义一个global的filter，那它可以被共用，不知道这个想法是否正确。如果正确，那么local的filters有哪些特别的用处吗？


failed to resolve directive

时有时无

根据console的提示找了半天不知道哪里错了

最后发现 html 里面多了个 v-



重新安排一下数据结构
不再是conference --- region --- teamList

而是直接给出teamList，把联盟和赛区，作为每个team的属性之一
至于list的顺序，则按照原来的conference --- region --- teamList顺序

team = {
	teamListId: '',	// 内部使用
	teamIdQq: '',	// 与球队主页链接、logo图片链接有关
	name: '',
	conference: '',
	region: '',
	stat: {},
}

teamList = [{team1}, {team2}, {team3}, ... ]


nba = {
	teamList: [],
	east: {
		'': [idList],
		'':
	},
	west: {

	}
}




总的 statList 保存为 全局变量，这样 app 的 主component 和 子component 之间，只需要传id，而不需要传递一个完整的 stat，这样有了id之后，就可以通过全局statList去索引指定id的stat



NBA

##	页面内容：

1.	第一层

	大标题

2.	第二层

	左右两个table，东西联盟

	6个赛区

	每个赛区，队标+队名，队名链接指向 nba.stats.qq.com/team/?id=id

	鼠标移到第二层不同的队名时，前端会在第三层显示该队的数据排名

3.	第三层

	svg，雷达图

##	数据

*	后端不使用db，只保存3个json文件，每天 crontab 定时用 update.py 更新

	通过py，得到 teams_raw.json 和 stats.json，提取数据，合成 teams.json

	回传给浏览器的只有 teams.json

*	浏览器请求页面时，返回模版nba.html

	通过html内的src，使浏览器再请求css, js

	通过js，请求 teams.json

	通过js，请求各队 logo ，文件名 ${id}.png

##	后端工作

*	router/WSGI

	/nba ---> NBAHandler ---> get() ---> return render_raw(nba.html)

	/nba?q=json ---> NBAHandler ---> get() ---> return teams.json

##	前端工作

*	使用 vuejs 完成数据请求与页面填充，以及 reactive svg
