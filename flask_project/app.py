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
# check which form was pressed
# request.form check for "post" or "delete"
# improvements: 
# check for valid input in form and return error if too long, false formatting etc.
# ask again when delete is pressed to be sure
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
