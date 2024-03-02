from datetime import datetime
from flask import Flask, render_template, url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///posts.ab'
db = SQLAlchemy
@app.route("/")
def index():
    return render_template("index.html")
class Post(db.Model):
    id = db.Column(db.Integer, primary_keysTrue)
    title = db.Column(db.String(100),nullabl=False)
    content = db.Column(db.Text,nullabl=False)
    date_posted = db.Column(db.DateTime,nullabl=False,defualt=datetime.now)
posts = []

@app.route('/blog', methods=['GET','POST'])
def blog():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = {'title': title, 'content': content, 'date': datetime.now()}
        posts.append(post)
        print(posts)
    return render_template("blog.html",posts=posts)


if __name__ == "__main__":
    app .run(debug=True, host="0.0.0.0")
