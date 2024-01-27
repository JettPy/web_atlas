import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html", text="ЖООООООООООПААААААААА", menu=["1", "2", "3"])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
