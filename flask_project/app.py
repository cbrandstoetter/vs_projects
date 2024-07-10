from flask import Flask, render_template, request
from db import all_posts
from markupsafe import escape
from db import post_by_id
from db import new_content
from db import delete_all_posts
from werkzeug.exceptions import abort
app = Flask(__name__)
from db import delete_post

@app.route('/data')
def data():
    return render_template('data.html', data = all_posts())


@app.route('/about')
def about():
    return "This is the about page!"


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/<id>")
def get_post(id):
    try:
        content = escape(post_by_id(int(id)))
        return f"This is your requested content:\n{content}"
    except:
        abort(404)

@app.route('/posts')
def posts():
    return render_template('posts.html')

@app.route('/posts', methods=['POST'])
def post_posts():
    if 'post' in request.form:
        try:
            title = request.form['title']
            content = request.form['content']
            new_content(title, content)
            return posts()
        except:
            return "bad"
    elif 'delete' in request.form:
        try:
            delete_all_posts()
            return "all posts deleted"
        except:
            return "could not delete posts"



@app.route('/data', methods=['POST'])
def delete():
    post_id = request.form['post_id']
    delete_post(post_id)
    return data()


"""
DONE

Since youll need to get a blog post by its ID from the database in multiple locations later in this project, 
youll create a standalone function called get_post(). You can call it by passing it an ID and receive back 
the blog post associated with the provided ID, or make Flask respond with a 404 Not Found message if the blog post does not exist.
use "abort()" from flask/Werkzeug library"

"""


"""
new post : DONE
edit and delete post: 

Now that youve finished displaying the blog posts that are present in the database on the web application, 
you need to allow the users of your application to write new blog posts and add them to the database, 
edit the existing ones, and delete unnecessary blog posts.

"""