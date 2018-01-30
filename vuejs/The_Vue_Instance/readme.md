这一节里面提到了hook，钩子。

>  Along the way, it also runs functions called lifecycle hooks, giving users the opportunity to add their own code at specific stages.

略微查了下资料，个人理解hook就是一个你可以插入自己代码的地方。

![lifecycle](https://vuejs.org/images/lifecycle.png)

上面的流程图中，红色框的地方就是hook，是Vue提供的一个接口。同时这些hook也是一个Vue对象的property，属性。

如果你想在红色框所在的阶段做点什么事情，就可以用这些hook，进入这些hook（入口），则需要通过给相应的hook(property)赋值一个函数，也就是property是key，函数是value

以文档中的demo为例，从流程图中可以看到created是一个hook，对应Vue的created属性，它的value是一个自己写的函数，这样，到了created阶段，这个函数就会被调用和执行。然后继续created之后的阶段

```javascript
var vm = new Vue({
  data: {
    a: 1
  },
  created: function () {
    // `this` points to the vm instance
    console.log('a is: ' + this.a)
  }
})
// => "a is: 1"
```

<br><br><br>

* [vue 中钩子 是怎样的一个概念?](https://www.zhihu.com/question/50880439)
* [什么叫“钩子”？](https://segmentfault.com/q/1010000004335505)
