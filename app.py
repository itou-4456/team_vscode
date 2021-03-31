from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

@app.route("/kyuyo")
def kyuyo():
    return render_template("kyuyo.html")

@app.route("/en")
def en():
    return render_template("en.html")

if __name__ == "__main__":
    app.run(debug=True)