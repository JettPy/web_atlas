import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/help")
def help():
    return """<a href="http://127.0.0.1:5000">This is help page</a>"""


if __name__ == "__main__":
    app.run(debug=True)
