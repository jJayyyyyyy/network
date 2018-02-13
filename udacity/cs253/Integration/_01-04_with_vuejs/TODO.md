1.	学习与练手

	用参数实现redirect

	流程：

	*	未登录状态，GET请求/blog/new
	*	server的NewBlogpostHandler的get()方法，对请求进行redirect，并添加query参数，转向/signin?redirect=/blog/new
	*	在SigninHandler进行透传，因为url会保留query参数




	发布new blogpost的时候，如果还未登录，就转到/signin，登录成功后，转到/blog/new

	也就是，要进入/blog/new，必须是登录状态，有合法cookie，否则会被redirect到/signin，举个例子，直接在url输入/blog/new，会被转回来。GET和POST都会被转回来

	填写subject和content，两者非空则提交json。否则提示Invalid，而且前端不提交。

	后端也要检查是否为空。如果合法，则插入数据库。然后转回/blog。如果不合法，就直接转回/blog

	因此，new要用form.submit=prevent，

	换用required，更简单，一步到位



为什么vuejs中，local filters无法获得this？

学习中遇到的问题，改造的场景如下：

```html
<div id="app">
	<p>{{ 1 | f1 }}</p>
	<p>{{ 1 | f2 }}</p>
	<p>{{ a | f3 }}</p>
</div>
```

```javascript
var app = new Vue({
	el: '#app',
	data: {
		a: 2
	},
	filters:{
		f1: function(id){
			return this.a;  // undefined
		},
		f2: function(id){
			return id;  	// 1
		},

		f3: function(id){
			return id;      // 2
		}
	}
})
```

每个p的值写在三个注释里了，只有第一个p是空的，而且一直是空的，说明并不会动态更新。如果在f1中用console.log(this)，会得到window，但是在其他的options里面定义的函数却可以获得Vue的实例app的this呢？

ps：如果在f1中加上console.log(this.app)，则会得到undefined，个人猜测此时可能还没有生成app，难道是local filters在Vue的lifecycle之前？

如果不能获得this，那为什么还要把filters分为local和global两类？

ps2: 看了文档Filters — Vue.js ，似乎没有发现相关说明。


1.

index + new 结合，类似artwork的add

blogpost + edit 结合，类似artwork的update

通过前端直接增减dom

而不是分成多个页面


2.  index的每一个标题只是url，点击后，flask只返回post.html模版，如何给前端通知id？

    因为只有一个通用模版，前端收到后，根据另外的参数——id，再去请求json数据，即每篇blogpost的实际subject, content，再填充到模版里面

    对于'https://example.com/abc/1'

    通过js，window.location.pathname，可以获得'/abc/1'，在通过split得到id

3.  点击button，进行post，如果cookie不合法，则激活modal进行登录，否则就完成了提交，然后更新dom


4.  index+new也用类似方法，完成前端的逻辑

    blog相当于artwork拆分成两个部分








客户端的rss应用, 跨域，还是需要反向代理，要么是通过自己的server，要么通过如下方式

http://blog.csdn.net/yw39019724/article/details/20624781

使用google或者yahoo之类的网站提供的api


慎用app.js


SB天猫超市，必须设置允许第三方cookie，否则会被判断为网络环境异常，而且怎么输如验证码都没用






1.	后端发送raw

	保存db的同时，保存json
	
	var artwork = {
		id: '',
		subject: '',
		content: ''
	}

	添加url_rule，使得.json能够得到访问

2.	前端，基本页面不变

	加入vue，请求json

	button：new artwork

	---> 出现subject content

			都有内容后才显示提交

			form附加：类型：add










button: update artwork

---> 出现 update artwork id，subject, content

		都有内容后才显示提交

		form附加：类型：update
