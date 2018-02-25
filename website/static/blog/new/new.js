'use strict';

var app = new Vue({
	el: '#editor',
	data: {
		pathname: '',
		subject: '',
		content: '',
		valid: false,
	},
	created: function(){
		this.pathname = document.location.pathname;
	},
	methods: {
		showModal: function(){
			this.valid = this.subject != '' && this.content != '';
			return !this.valid;
		},
		submit: function(){
			if( this.valid ){
				var self = this;
				var APIpost = `${self.pathname}`;
				var newPost = {
					'subject': self.subject,
					'content': self.content,
				};
				axios.post(APIpost, newPost)
					.then( function(resp){
						window.location.replace(resp.data)
					})
			}
		}
	}
})