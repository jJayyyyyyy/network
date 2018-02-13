var reLow = /[a-mA-M]/;
var reHigh = /[n-zN-Z]/;

var app = new Vue({
	el: '#rot13',
	data: {
		text: ''
	},
	computed: {
		encoded: function (){
			var newStr = [];
			var len = this.text.length;
			for(let i=0; i < len; i++ ){
				var ch = this.text[i];
				if( reLow.test(ch) ){
					ch = ch.charCodeAt() + 13;
					ch =  String.fromCharCode(ch);
				}else if( reHigh.test(ch) ){
					ch = ch.charCodeAt() - 13;
					ch = String.fromCharCode(ch);
				}
				newStr.push(ch);
			}
			newStr = newStr.join('');
			return newStr
		}
	}
})