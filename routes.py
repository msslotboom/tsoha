from flask import Flask
from flask import redirect, render_template, request
from app import app
from db import db
import timemanager

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
    
    timemanager.add_timestamp(time, task, 1)
    total_time = timemanager.get_total_time_user(1)
    
    return render_template("result.html", task=task,
                                          time=time,
                                          total=total_time,
                                          user_id = id
                                          )