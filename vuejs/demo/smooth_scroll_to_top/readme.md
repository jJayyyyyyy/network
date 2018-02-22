1.	动画，静态的帧，连起来，间隔非常短，就变成了动画animation

2.	注意，不能用

	```javascript
	var pos = document.documentElement.scrollTop;
	// pos -= 50;
	```
	
	pos只是赋值，不是引用。必须操作原对象
	
	```javascript
	document.documentElement.scrollTop -= 40;
	```
	
*	[How TO - Scroll Back To Top Button](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp)
*	[DOM Animation](https://www.w3schools.com/js/js_htmldom_animate.asp)
*	[DOM Animation tryjs_dom_animate_3](https://www.w3schools.com/js/tryit.asp?filename=tryjs_dom_animate_3)
*	[setInterval](https://www.w3schools.com/jsref/met_win_setinterval.asp)
*	[setInterval](http://www.w3school.com.cn/jsref/met_win_setinterval.asp)
