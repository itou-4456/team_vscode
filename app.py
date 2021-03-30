from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

@app.route("/en")
def en():
    return render_template("en.html")

@app.route("/hankei")
def hankei():
    han = request.args.get("han")
    han = int(han)
    menseki = han * han * 3.14
    ensyu = 2 * han * 3.14
    return render_template("hankei.html", menseki=menseki, ensyu=ensyu)

@app.route("/kyuyo")
def kyuyo():
    return render_template("kyuyo.html")

@app.route("/gekkyu")
def gekkyu():
    zikyu = request.args.get("zikyu")
    time = request.args.get("time")
    zikyu = int(zikyu)
    time = int(time)
    gekkyu = zikyu * time
    return render_template("gekkyu.html", gekkyu=gekkyu)

if __name__ == "__main__":
    app.run(debug=True)