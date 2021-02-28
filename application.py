from flask import render_template, session, request, redirect, Flask
from flask_socketio import SocketIO, emit, send, join_room
import imdScore, iexStocks

application = Flask(__name__)
# application.config['SECRET_KEY'] = os.environ['SECRET_KEY']
application.config["SECRET_KEY"] = "1023912038109823aljksdflkajds"
app = application
socketio = SocketIO(app, async_mode=None)


@app.route("/", methods=["GET", "POST"])
def welcome():
    if request.method == "POST":
        req = request.form
        print(req)
        result = iexStocks.getFinancials(req["symbol"].upper(), req["pe"])
        print(result)
        session["result"] = result
        return render_template("index.html")
    else:
        return render_template("index.html")


@app.route("/check", methods=["POST", "GET"])
def check():
    req = request.form
    result = iexStocks.getFinancials(req["symbol"].upper(), req["pe"])
    if result["status"] == "success":
        return render_template("check.html", result=result, form=req)
    else:
        return render_template("error.html", result=result)


@app.route("/result", methods=["POST"])
def result():
    req = request.form
    result = imdScore.score(
        float(req["stock-price"]),
        float(req["4-years"]),
        float(req["book-value"]),
        float(req["buy-analysts"]),
        float(req["strong-buy"]),
        float(req["yield"]),
        float(req["margin"]),
        float(req["volume"]),
        float(req["pe"]),
    )
    print(result)
    return render_template("result.html", result=result)


@socketio.on("connect")
def connect():
    print("connected")


@socketio.on("symbolLookup")
def symbolLookup(data):
    print(data)


if __name__ == "__main__":
    socketio.run(app, debug=True)
