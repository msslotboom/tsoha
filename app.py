from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    task = request.form["task"]
    time = request.form["time"]
    return render_template("result.html", task=task,
                                          time=time)