import sqlite3


def new_content(tit, cont):
    connection = sqlite3.Connection('database.db')
    cur = connection.cursor()
    cur.execute("INSERT INTO posts (title, content) VALUES ('%s', '%s')" % (tit, cont))
    connection.commit()
    connection.close()


def all_posts():
    connection = sqlite3.Connection('database.db')
    cur = connection.cursor()
    posts = (cur.execute("SELECT * FROM posts").fetchall())
    connection.close()
    return posts


def post_by_id(id):
    connection = sqlite3.Connection('database.db')
    cur = connection.cursor()
    content = (cur.execute("SELECT content FROM posts WHERE id=%d" % id).fetchall())
    connection.close()
    return content [0]


def delete_all_posts():
    connection = sqlite3.Connection('database.db')
    cur = connection.cursor()
    cur.execute("DELETE FROM posts")
    connection.commit()
    connection.close()


def delete_post(post_id):
    connection = sqlite3.Connection('database.db')
    cur = connection.cursor()
    cur.execute("DELETE FROM posts WHERE id=%s" % post_id)
    connection.commit()
    connection.close()
    return None