from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///slotboom"
db = SQLAlchemy(app)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    task = request.form["task"]
    time = request.form["time"]
    sql = "INSERT INTO time (hours, task) VALUES (:time, :task)"
    db.session.execute(sql, {"time":time, "task":task})
    db.session.commit()
    return render_template("result.html", task=task,
                                          time=time)