from flask import redirect, render_template, request, session
from app import app
import timemanager, users

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/create_user")
def create_page():
    return render_template("create_user.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    username = request.form["username"]
    password = request.form["password"]
    password_repeat = request.form["password_repeat"]

    if users.create_user(username, password) and password==password_repeat:
        if users.login(username, password):
            session["username"] = username
            return redirect("/")
        else:
            return redirect("/login")
    else:
        return redirect("/create_user")

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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def show_login_field():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username, password):
        session["username"] = username
        return redirect("/")
    else:
        return redirect("/login")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")