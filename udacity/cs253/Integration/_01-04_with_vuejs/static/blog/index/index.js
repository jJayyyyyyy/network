var app = new Vue({
	el: '#index',
	data: {
		pathname: '',
		postList: []
	},
	created: function(){
		this.getPostList();
		this.pathname = document.location.pathname;
	},
	filters:{
		getPostUrl: function(id){
			var pathname = document.location.pathname;
			return `${pathname}/${id}`;
		}
	},
	methods: {
		getPostList: function(){
			var APIjson = `${this.pathname}?q=json`;
			var self = this;
			axios.get(APIjson)
				.then(function(resp){
					self.postList = resp.data;
				})
		}
	}
})