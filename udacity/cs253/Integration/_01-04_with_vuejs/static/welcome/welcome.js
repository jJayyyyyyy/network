var app = new Vue({
	el: '#welcome',
	data: {
		pathname: '',
		redirectPath: '',
		userList: []
	},
	created: function(){
		this.pathname = document.location.pathname;
		this.redirectPath = document.location.search.split('=')[1]
		this.getUsername();
	},
	methods: {
		getUsername: function(){
			var APIjson = `${this.pathname}?q=json`;
			var self = this;
			axios.get(APIjson)
				.then(function(resp){
					self.userList = resp.data;
					self.redirect();
				})
		},
		redirect: function(){
			var self = this;
			if( self.redirectPath ){
				window.setTimeout( function(){ window.location.replace( `${self.redirectPath}` ); }, 2000 );
			}
		}
	}
})