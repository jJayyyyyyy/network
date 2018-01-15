##	Intro

1.	1-16小节的测试代码放在`concept_01_16`文件夹内

2.	首先在命令行运行python3，然而导入并运行`main.py`中的`init_db()`，这样就建立了名为`ascii_art.db`的数据库文件，根据`schemal.sql`，里面有一个叫做`entries`的`table`

	```bash
	$ python3
	>>> from main import init
	>>>	init_db()
	```

3.	可以通过`test_db.py`对刚才建立的数据库进行测试，包括

	*	添加新记录
	*	查询已有记录
	*	删除记录
	*	重新初始化

4.	`main.py`通过Flask和sqlite3实现了Lesson3的剩余功能，即可以添加一条记录，内容包括了[id, title, art]

5.	不可能一次达到完美的，前端后端都是，总会经历多次重构。不要纠结，不要OCD

##	TODO

*	GAE版本
*	重构(optional)

##	Reference

*	[udacity](https://classroom.udacity.com/courses/cs253)
*	[w3school SQL](https://www.w3schools.com/sql/)
*	[flask SQLite](http://flask.pocoo.org/docs/0.12/patterns/sqlite3/)
*	[ascii art](http://chris.com/ascii/index.php)
*	[w3school CSS](https://www.w3schools.com/css/)
