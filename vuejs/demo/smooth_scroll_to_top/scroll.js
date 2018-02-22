'use strict';

var app = new Vue({
	el: '#scroll',
	methods: {
		backToTop: function(){
			var curPos = document.documentElement.scrollTop;
			console.log(curPos);
			var it = setInterval(function(){
				if(document.documentElement.scrollTop <= 0 ){
					clearInterval(it);
				}else{
					document.documentElement.scrollTop -= 40;
				}
			}, 20);
		}
	}
})

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function(){
	if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
		document.getElementById("myBtn").style.display = "block";
	} else {
		document.getElementById("myBtn").style.display = "none";
	}
};

/*
// When the user clicks on the button, scroll to the top of the document
function topFunction() {
	// onclick="topFunction()"
	document.body.scrollTop = 0;
	document.documentElement.scrollTop = 0;
}
*/