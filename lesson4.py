import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index2.html", text="Привет!", menu=["1", "2", "3"])

# Добавим роут для профиля
# Добавим аргумент к нашей ссылке - имя name.
# Теперь если будет передано имя, шаблонизатор будет строить макет где оно используется,
# а если не передано, будет использовать значение по умолчанию.
# Параметры передаются в треугольных скобочках <>:
# Не забудьте передать этот параметр в функцию которую вызывает flask.
@app.route('/profile/<name>')
@app.route("/profile/")
def profile(name=""):
    return flask.render_template("profile.html", user=name)


@app.route("/help")
def help():
    return {"a": 1}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
