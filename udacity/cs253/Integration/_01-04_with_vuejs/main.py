from flask import Flask, request, redirect, url_for
from rot13 import ROT13Handler
from fizzbuzz import FizzBuzzHandler
from index import IndexHandler
from welcome import WelcomeHandler
from artwork import AsciiArtHandler
from database import init_db
from blog import BlogIndexHandler, NewBlogpostHandler, BlogPostHandler
from user import SignupHandler, SigninHandler, SignoutHandler
from nba import NBAHandler

# create app
app = Flask(__name__)

# $ export FLASK_APP=main
# $ python3 -m flask init
@app.cli.command('ini')
def init():
	init_db()
# or add the next line before app.run
# app.cli.command('ini')(database.init_db)

if __name__ == '__main__':
	app.add_url_rule('/', view_func=IndexHandler.as_view('index'))
	app.add_url_rule('/rot13', view_func=ROT13Handler.as_view('rot13'))
	app.add_url_rule('/fizzbuzz', view_func=FizzBuzzHandler.as_view('fizzbuzz'))
	app.add_url_rule('/welcome', view_func=WelcomeHandler.as_view('welcome'))
	app.add_url_rule('/ascii_art', view_func=AsciiArtHandler.as_view('ascii_art'))
	app.add_url_rule('/blog/', view_func=BlogIndexHandler.as_view('blog_index'))
	app.add_url_rule('/blog/new', view_func=NewBlogpostHandler.as_view('new_blogpost'))
	app.add_url_rule('/blog/<int:id>', view_func=BlogPostHandler.as_view('blogpost'))
	# app.add_url_rule('/blog/edit/<int:id>', view_func=EditPostHandler.as_view('edit_post'))
	app.add_url_rule('/signup', view_func=SignupHandler.as_view('signup'))
	app.add_url_rule('/signin', view_func=SigninHandler.as_view('signin'))
	app.add_url_rule('/signout', view_func=SignoutHandler.as_view('signout'))
	app.add_url_rule('/nba', view_func=NBAHandler.as_view('nba'))
	app.run(port=8080, host='0.0.0.0', debug=True)
	# app.run(port=8080, host='0.0.0.0', debug=False)
