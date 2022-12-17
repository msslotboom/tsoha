from flask import Flask
from flask import redirect, render_template, request
from app import app
from db import db

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/create_user")
def create_page():
    return render_template("create_user_form.html")

def create():
    pass

@app.route("/result", methods=["POST"])
def result():
    task = request.form["task"]
    time = request.form["time"]
    # user_id is temporarily hardcoded
    id = 1
    sql_insert = "INSERT INTO time (hours, task, user_id, logged_at) VALUES (:time, :task, :id, NOW())"
    sql_tot_time = "SELECT SUM (hours) FROM time WHERE user_id =:user_id"

    db.session.execute(sql_insert, {"time":time, "task":task, "id":id})
    db.session.commit()
    print("debug print")
    result = db.session.execute(sql_tot_time, {"user_id":id})
    total = result.fetchone()[0]
    db.session.commit()

    return render_template("result.html", task=task,
                                          time=time,
                                          total=total,
                                          user_id = id
                                          )