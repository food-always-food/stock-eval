from flask import render_template, session, request, redirect, Flask
from flask_socketio import SocketIO, emit, send, join_room
import imdScore, iexStocks, database

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
    symbolCheck = database.lookupSymbol(req["symbol"].upper())
    if symbolCheck == False:
        result = iexStocks.getFinancials(req["symbol"].upper(), req["pe"])
        print(result)
        database.storeResult(
            result["price"],
            result["yrPrice"],
            result["bookValue"],
            req["buy_analysts"],
            req["strong_buy"],
            result["yield"],
            result["opMargin"],
            result["volume"],
            result["peRatio"],
            result["symbol"],
            f"$tag${result['company']}$tag$",
            f"$tag${result['description']}$tag$",
        )
        if result["status"] == "success":
            return render_template("check.html", result=result, form=req)
        else:
            return render_template("error.html", result=result)
    else:
        result = symbolCheck[0]
        result["price"] = result["cp"]
        result["yrPrice"] = result["op"]
        result["bookValue"] = result["bv"]
        result["yield"] = result["yd"]
        result["opMargin"] = result["om"]
        result["volume"] = result["dv"]
        result["peRatio"] = result["pe"]
        result["description"] = result["age"]
        result["company"] = "FIX ME"
        result["status"] = "success"
        result["database"] = "historical"
        if result["status"] == "success":
            return render_template("check.html", result=result, form=req)
        else:
            return render_template("error.html", result=result)


@app.route("/result", methods=["POST"])
def result():
    req = request.form
    database.storeResult
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
    resultList = database.lookupSymbol(data.upper())
    if resultList != False:
        result = resultList[0]
        score = imdScore.score(
            float(result["cp"]),
            float(result["op"]),
            float(result["bv"]),
            float(result["bu"]),
            float(result["sb"]),
            float(result["yd"]),
            float(result["om"]),
            float(result["dv"]),
            float(result["pe"]),
        )
        resultList[0]["score"] = score
        print(result)
    emit("symbol", resultList)


if __name__ == "__main__":
    socketio.run(app, debug=True)
