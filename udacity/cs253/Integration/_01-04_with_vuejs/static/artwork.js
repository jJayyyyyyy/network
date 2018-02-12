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
		checkValid: function(){
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
			if( this.checkValid() ){
				var self = this;
				console.log(self.user);
				axios.post('./signin', self.user)
					.then( function(resp){
						console.log(resp);
						if(resp.data === 'welcome'){
							self.reset();
							self.$emit('succ');
						}else{
							self.error.username = 'Invalid login';
							self.error.password = 'Invalid login';
							console.log('Invalid login');
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
		this.getArtworkList()
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
		setModal: function(){
			this.showSigninModal = true;
		},
		resetModal: function(){
			this.showSigninModal = false;
		},
		checkValid: function(){
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
			if( this.checkValid() === true ){
				// todo: post
				var self = this;
				axios.post('./ascii_art', this.artwork)
					.then( function (resp){
						self.resp = resp;
						if(resp.data === 'signin'){
							self.setModal();
							console.log('showSigninModal');
							// fill the modal signin form
						}else if(resp.headers['content-type'] === 'application/json'){
							// todo 增加过渡效果
							console.log('succ');
							self.reset();
							self.artworkList = resp.data;
						}
					})
			}
		},

		getArtworkList: function(){
			var self = this;
			axios.get('./assets/artwork.json')
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