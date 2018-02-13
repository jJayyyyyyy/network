var comp = Vue.component('modal', {
	template: '#modal-template',
	data: function(){
		return {
			user: {
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
			};
			this.error = {
				username: '',
				password: ''
			}
		},
		checkValidSignin: function(){
			var valid = true;
			if(this.user.username){
				this.error.username = '';
			}else{
				this.error.username = 'Invalid username';
				valid = false;
			}

			if(this.user.password){
				this.error.password = '';
			}else{
				this.error.password = 'Invalid password';
				valid = false;
			}
			return valid;
		},
		signin: function(){
			if( this.checkValidSignin() ){
				var self = this;
				// console.log(self.user);
				axios.post('/signin', self.user)
					.then( function(resp){
						// console.log(resp);
						if(resp.data === 'welcome'){
							self.reset();
							self.$emit('succ');
						}else{
							self.error.username = 'Invalid login';
							self.error.password = 'Invalid login';
							// console.log('Invalid login');
						}
					} );
			}
		},
		cancel: function(){
			this.reset();
			this.$emit('cancel');
		}
	}
})

var app = new Vue({
	el: '#artwork',
	data: {
		pathname: '',
		resp: '',
		showSigninModal: false,
		error:{
			id: '',
			subject: '',
			content: ''
		},
		artwork: {
			id: '',
			subject: '',
			content: '',
			type: ''
		},
		artworkList: []
	},
	created: function(){
		this.pathname = document.location.pathname;
		this.getArtworkList();
	},

	methods:{
		setAddArtwork: function(){
			this.reset();
			this.artwork.type = 'add';
		},
		setUpdateArtwork: function(){
			this.reset();
			this.artwork.type = 'update';
		},
		reset: function(){
			this.artwork = {
				id: '',
				subject: '',
				content: '',
				type: ''
			};
			this.error = {
				id: '',
				subject: '',
				content: ''
			};
			this.showSigninModal = false;
		},
		checkValidArtwork: function(){
			var valid = true;
			if( this.artwork.type === 'update' ){
				var reDigit = /^\d+$/;
				if( reDigit.test(this.artwork.id) && this.artwork.id>0 ){
					this.error.id = '';
				}else{
					this.error.id = 'Invalid ID';
					valid = false;
				}
			}

			if( this.artwork.subject ){
				this.error.subject = '';
			}else{
				this.error.subject = 'Invalid Subject';
				valid = false;
			}

			if( this.artwork.content ){
				this.error.content = '';
			}else{
				this.error.content = 'Invalid Content';
				valid = false;
			}
			return valid;
		},
		submit: function(){
			if( this.checkValidArtwork() === true ){
				var APIpost = `${this.pathname}`;
				var self = this;
				axios.post(APIpost, self.artwork)
					.then( function (resp){
						self.resp = resp;
						if(resp.data === 'signin'){
							// fill in the modal signin form
							self.showSigninModal = true;
						}else if(resp.data === 'inserted'){
							// todo 增加过渡效果
							self.artworkList.unshift(self.artwork);
							self.reset();
						}else if(resp.data === 'updated'){
							var index = self.artworkList.length - self.artwork.id;
							self.artworkList[index] = self.artwork;
							self.reset()
						}
					})
			}
		},

		getArtworkList: function(){
			var APIjson = `${this.pathname}?q=json`;
			var self = this;
			axios.get(APIjson)
				.then(function(resp){
					self.artworkList = resp.data;
				})
		}
	}
})


function toggle_bg(e){
	if (document.getElementById("btn").value=="Dark on Light"){
		document.getElementById("btn").value="Light on Dark";
		document.getElementById("artwork_list").style.background = "#FFFFFF";
		document.getElementById("artwork_list").style.color = "#000000";
	}

	//Checking if select field is disabled
	else {
		//Change the select field state to enabled and changing the value of button to disable
		document.getElementById("btn").value="Dark on Light";
		document.getElementById("artwork_list").style.background = "#2A4767";
		document.getElementById("artwork_list").style.color = "#FFFFFF";
	}
}




// getArtworkList: function(){
// 	var self = this;
// 	var xhr = new XMLHttpRequest()
// 	xhr.onreadystatechange = function(){
// 		if( xhr.readyState === 4 && xhr.status === 200 ){
// 			var resp = JSON.parse(xhr.responseText)
// 			self.artworkList = resp
// 		}
// 	}
// 	xhr.open('GET', './assets/artwork.json')
// 	xhr.send()
// }