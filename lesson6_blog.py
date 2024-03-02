from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlcemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)


# Тут мы будем хранить посты
posts = []


@app.route('/')
def index():
    return render_template('index.html')


# Сделаем вкладку с блогом, будем публиковать посты и отображать их.
# Для обработки запросов от клиента надо расширить стандартный route.
# По умолчанию мы работаем с методами GET, добавив строчку methods=['GET', 'POST']
# Мы сможем обрабатывать запрсы от клиента с помощью метода POST
@app.route('/blog', methods=['GET', 'POST'])
def blog():
    # Далее используя модуль request будем проверять, нсли пришел метод POST
    if request.method == 'POST':
        # Будем доставать поля title и content из запроса
        title = request.form['title']
        content = request.form['content']
        # Группируем данные в словарь и добавлем дату создания поста
        post = {"title": title, "content": content, 'date': datetime.now()}
        # Сохраняем пост в массив постов
        posts.append(post)
        print(posts)
    # После выполнения запроса, обновляем шаблон страницы
    return render_template('blog.html', posts=posts)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
