from flask import render_template, session, request, redirect, Flask

application = Flask(__name__)
# application.config['SECRET_KEY'] = os.environ['SECRET_KEY']
application.config["SECRET_KEY"] = "1023912038109823aljksdflkajds"
app = application


@app.route("/", methods=["GET", "POST"])
def welcome():
    if request.method == "POST":
        req = request.form
        print(req)
        return render_template("index.html")
    else:
        page = {
            "title": "Welcome to Castle Braumburg",
            "background": "welcome/castle.jpg",
        }
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
