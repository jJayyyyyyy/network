from flask import Flask, request, redirect, url_for
from rot13 import ROT13Handler
from fizzbuzz import FizzBuzzHandler
from index import IndexHandler
from welcome import WelcomeHandler
from artwork import AsciiArtHandler
from database import init_db
from blog import BlogIndexHandler, NewPostHandler, GetPostHandler, EditPostHandler
from user import SignupHandler, SigninHandler, SignoutHandler

# create app
app = Flask(__name__)


# $ export FLASK_APP=main
# $ python3 -m flask init
@app.cli.command('ini')
def init():
	init_db()
# or add the next line before app.run
# app.cli.command('ini')(database.init_db)

# class Signup(MethodView):
# 	def get(self):
# 		signup = page.Signup()
# 		return signup.render()

# 	def post(self):
# 		return 'pass'


if __name__ == '__main__':
	app.add_url_rule('/', view_func=IndexHandler.as_view('index'))
	app.add_url_rule('/rot13', view_func=ROT13Handler.as_view('rot13'))
	app.add_url_rule('/fizzbuzz', view_func=FizzBuzzHandler.as_view('fizzbuzz'))
	app.add_url_rule('/welcome', view_func=WelcomeHandler.as_view('welcome'))
	app.add_url_rule('/ascii_art', view_func=AsciiArtHandler.as_view('ascii_art'))
	app.add_url_rule('/blog', view_func=BlogIndexHandler.as_view('blog_index'))
	app.add_url_rule('/blog/new_post', view_func=NewPostHandler.as_view('new_post'))
	app.add_url_rule('/blog/<int:post_id>', view_func=GetPostHandler.as_view('post'))
	app.add_url_rule('/blog/edit/<int:post_id>', view_func=EditPostHandler.as_view('edit_post'))
	app.add_url_rule('/signup', view_func=SignupHandler.as_view('signup'))
	app.add_url_rule('/signin', view_func=SigninHandler.as_view('signin'))
	app.add_url_rule('/signout', view_func=SignoutHandler.as_view('signout'))
	app.run(port=8000, debug=True)
