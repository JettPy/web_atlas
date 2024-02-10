from flask import Flask, render_template, url_for
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html", text="araaaaaaa",menu = ["fjffjfj", "slawa loxx"])


@app.route('/profile/<int:name>')
@app.route("/profile/")
def profile(name=""):
    return render_template("profile.html", user=name)


if __name__ == "__main__":
    app .run(debug=True, host="0.0.0.0")
