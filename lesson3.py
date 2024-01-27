import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html", text="Привет!", menu=["1", "2", "3"])


@app.route("/help")
def help():
    return {"a": 1}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
