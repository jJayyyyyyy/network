var signinModal = Vue.component('modal', {
	template: '#modal-template',
	data: function(){
		return {
			user:{
				username: '',
				password: ''
			},
			error: {
				username: '',
				password: ''
			}
		}
	},
	methods: {
		reset: function(){
			this.user = {
				username: '',
				password: ''
			},
			this.error = {
				username: '',
				password: ''
			}
		},
		checkValid: function(){
			var valid = true;
			if( this.user.username ){
				this.error.username = '';
			}else{
				this.error.username = 'Invalid username';
				valid = false;
			}

			if( this.user.password ){
				this.error.password = '';
			}else{
				this.error.password = 'Invalid password';
				valid = false;
			}
			return valid;
		},
		signin: function(){
			if( this.checkValid() ){
				var self = this;
				axios.post('/signin', self.user)
					.then( function(resp){
						console.log(resp)
						if( resp.data === 'welcome' ){
							self.reset();
							self.$emit('succ');
						}else{
							self.error.username = 'Invalid login';
							self.error.password = 'Invalid login';
						}
					})
			}
		},
		cancel: function(){
			this.reset();
			this.$emit('cancel');
		}
	}
})

var app = new Vue({
	el: '#blogpost',
	data: {
		resp: '',
		pathname: '',
		id: '',
		postList: [],
		newPost: {
			subject: '',
			content: '',
			type: ''
		},
		error: {
			subject: '',
			content: ''
		},
		showSigninModal: false
	},
	created: function(){
		this.pathname = document.location.pathname;
		this.id = this.pathname.split('/')[2];
		this.getPostList();
	},
	methods: {
		reset: function(){
			this.newPost = {
				subject: '',
				content: '',
				type: ''
			};
			this.error = {
				subject: '',
				content: ''
			};
			this.showSigninModal = false;
		},
		updatePost: function(){
			this.reset();
			this.newPost.type = 'update';
		},
		checkValid: function(){
			var valid = true;
			if( this.newPost.subject ){
				this.error.subject = '';
			}else{
				this.error.subject = 'Invalid Subject';
				valid = false;
			}

			if( this.newPost.content ){
				this.error.content = '';
			}else{
				this.error.content = 'Invalid Content';
				valid = false;
			}

			return valid;
		},
		submit: function(){
			if(this.checkValid() === true ){
				var APIpost = `${this.pathname}`;
				var self = this;
				axios.post(APIpost, self.newPost)
					.then( function(resp){
						self.resp = resp;
						if( resp.data === 'signin' ){
							self.showSigninModal = true;
						}else if( resp.data === 'updated' ){
							self.postList[0] = self.newPost;
							self.reset();
						}
					})
			}
		},
		getPostList: function(){
			var reDigit = /^\d+$/;
			if(reDigit.test(this.id) && this.id>0 ){
				var APIjson = `${this.pathname}?q=json`
				var self = this;
				axios.get(APIjson)
					.then(function(resp){
						self.postList = resp.data;
					})
			}
		}
	}
})
