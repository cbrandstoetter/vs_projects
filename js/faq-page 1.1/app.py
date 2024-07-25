from flask import Flask, render_template
import sqlite3



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/faq')
def give_faq():
    return render_template('faq-page.html')



if __name__ == '__main__':
    app.run(debug=True)

