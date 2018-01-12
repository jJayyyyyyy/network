此前使用的填充html的方法叫做**string substitution**, 但是在面对更大的html时，这种替换方法(可能)会变得比较麻烦。

下一期将使用jinja2, 这个引擎可以帮助我们更好更方便地完成上述功能。

Templates are a way to organize your html in a way that's easier than string substitution. String substitution can get a little hairy once you get very large html files.

Jinja2 is one of the templating engines. And it is basically glorified string substitution except that it helps you handle separating those out into multiple files and folders so that you dont have to worry about it as much.

*	[Primer on Jinja Templating](https://realpython.com/blog/python/primer-on-jinja-templating/)
*	[Jinja2](http://jinja.pocoo.org/)

*	PS:

	初步研究了Jinja2之后，发现我们的替换思路很像，我的填充方法是Page.py里面的`fill_template()`，不过，很显然Jinja2是一个更好的引擎，而且有更多其他功能，所以我们不用自己造轮子啦~
