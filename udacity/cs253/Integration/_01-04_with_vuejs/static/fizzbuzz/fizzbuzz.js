var app = new Vue({
	el: '#fizzbuzz',
	data: {
		num: null,
		FB: []
	},
	methods: {
		getFB: function(){
			var FB = []
			var fb = ''
			var len = Number(this.num)
			for(let i = 1; i <= len; i++){
				if (i % 15 === 0){
					fb = 'FizzBuzz'
				}else if(i % 3 === 0){
					fb = 'Fizz'
				}else if(i % 5 === 0){
					fb = 'Buzz'
				}else{
					fb = i
				}
				FB.push(fb)
			}
			this.FB = FB
			this.show = !this.show
			console.log(FB)
		}
	}
})
