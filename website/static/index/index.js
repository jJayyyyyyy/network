'use strict';

var app = new Vue({
	el: '#vindex',
	data: {
		newsList36kr: [],
		newsListReadHub: [],
		newsList: null,
		frontend: true,
		backend: false,
		curPage: 1,
		curNewsSrc: 1,
		totalPage: 2
	},
	created: function(){
		this.getJsonData();
	},
	filters: {
		calcTimeLag: function(date){
			var past = new Date(date);
			var now = new Date();
			var sec = (now - past)/1000;
			var minute = Math.floor( sec / 60 );
			var hour = Math.floor(minute / 60);
			var day = Math.floor(hour / 24);
			if( day > 0 ){
				return day + 'd ago';
			}else if(hour > 0){
				return hour + 'h ago';
			}else{
				return minute + 'min ago';
			}
		}
	},
	methods: {
		reset: function(){
			this.frontend = true;
			this.backend = false;
			this.curPage = 1;
			this.curNewsSrc = 1;
			this.newsList = null;
		},
		prevPage: function(){
			if( this.frontend ){
				return '...';
			}else{
				return 'Prev';
			}
		},
		nextPage: function(){
			if( this.backend ){
				return '...';
			}else{
				return 'Next';
			}
		},
		goPrev: function(event){
			if( this.curPage > 1 ){
				this.curPage--;
				this.getNewsList(this.curPage);
				this.goToTop();
				this.backend = false;
			}
			if( this.curPage === 1 ){
				this.frontend = true;
				// alert
			}
		},
		goNext: function(){
			if( this.curPage < 2 ){
				this.curPage++;
				this.getNewsList(this.curPage);
				this.goToTop();
				this.frontend = false;
			}
			if( this.curPage === 2 ){
				this.backend = true;
			}
		},
		switchNewsSrc: function(src){
			this.reset();
			this.curNewsSrc = src;
			this.getNewsList(this.curPage);
		},
		getNewsList: function(page){
			var begin = (this.curPage - 1)*10;
			var end = this.curPage * 10;
			if(this.curNewsSrc === 1){
				this.newsList = this.newsListReadHub.slice(begin, end);
			}else{
				this.newsList = this.newsList36kr.slice(begin, end);
			}
		},
		getJsonData: function(){
			var self = this;
			var APIJsonReadHub = '/static/index/db/readhub.json';
			var APIJson36kr = '/static/index/db/36kr.json';
			axios.get(APIJsonReadHub)
				.then( function(resp){
					self.newsListReadHub = resp.data;
					var page = 1;
					self.getNewsList(page);
				})
			axios.get(APIJson36kr)
				.then( function(resp){
					self.newsList36kr = resp.data;
				})
		},
		goToTop: function(){
			var it = setInterval(function(){
				if(document.documentElement.scrollTop <= 0 ){
					clearInterval(it);
				}else{
					document.documentElement.scrollTop -= 40;
				}
			}, 20);
		},

	}
})

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function(){
	if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
		document.getElementById("go-to-top").style.display = "block";
	} else {
		document.getElementById("go-to-top").style.display = "none";
	}
};
