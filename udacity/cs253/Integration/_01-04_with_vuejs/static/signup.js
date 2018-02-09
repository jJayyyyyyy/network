var reUsername = /^[a-zA-Z0-9_-]{3,20}$/;
var rePassword = /^.{3,20}$/;
var reEmail = /^[\S]+@[\S]+.[\S][\S]+$/;
var app = new Vue({
	el: '#signup',
	data: {
		username: '',
		password: '',
		verify: '',
		email: '',
		validUsername: false,
		validPassword: false,
		validVerify: false,
		validEmail: false,
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
		verifyError: function(){
			if( this.verify ){
				if( this.verify === this.password ){
					this.validVerify = true;
					return null;
				}else{
					this.validVerify = false;
					return 'Password not matched';
				}
			}
		},
		emailError: function(){
			if( this.email ){
				if( reEmail.test(this.email) ){
					this.validEmail = true;
					return null;
				}else{
					this.validEmail = false;
					return 'Invalid Email';
				}
			}else{
				this.validEmail = true;
			}
		},
		showSubmit: function(){
			this.isValid = (this.validUsername && this.validPassword && this.validVerify && this.validEmail);
			return this.isValid;
		}
	},
	// methods
	methods: {
		succ: function(){
			if (this.isValid) {
				var user = {
					username: this.username,
					password: this.password,
					email: this.email
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