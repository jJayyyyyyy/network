var reUsername = /^[a-zA-Z0-9_-]{3,20}$/;
var rePassword = /^.{3,20}$/;

var app = new Vue({
	el: '#signin',
	data: {
		username: '',
		password: '',
		validUsername: false,
		validPassword: false,
		isValid: false
	},

	computed: {
		usernameError: function(){
			if( this.username ){
				if( reUsername.test(this.username) ){
					this.validUsername = true;
					return null;
				}else{
					this.validUsername = false;
					return 'Invalid Username';
				}
			}
		},
		passwordError: function(){
			if( this.password ){
				if( rePassword.test(this.password) ){
					this.validPassword = true;
					return null;
				}else{
					this.validPassword = false;
					return 'Invalid password';
				}
			}
		},
		showSubmit: function(){
			this.isValid = (this.validUsername && this.validPassword);
			return this.isValid;
		}
	},
	// methods
	methods: {
		succ: function(){
			if (this.isValid) {
				var user = {
					username: this.username,
					password: this.password
				};
				console.log(user);
				// var form = Object;
				// form.push(user);
			}
		},
		postForm: function () {
			;
		}
	}
})