from flask import render_template, session, request, redirect, Flask
import imdScore, iexStocks

application = Flask(__name__)
# application.config['SECRET_KEY'] = os.environ['SECRET_KEY']
application.config["SECRET_KEY"] = "1023912038109823aljksdflkajds"
app = application


@app.route("/", methods=["GET", "POST"])
def welcome():
    if request.method == "POST":
        req = request.form
        print(req)
        result = iexStocks.getFinancials(req['symbol'],req['pe'])
        print(result)
        session['result'] = result
        return render_template("index.html")
    else:
        return render_template("index.html")

@app.route("/check",methods=["POST"])
def check():
    req = request.form
    print(req)
    result = imdScore.score(int(req['stock-price']),int(req['4-years']),int(req['book-value']),int(req['buy-analysts']),int(req['strong-buy']),int(req['yield']),int(req['margin']),int(req['volume']),int(req['pe']))
    print(result)
    return render_template("check.html")

@app.route("/result",methods=["POST"])
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)
