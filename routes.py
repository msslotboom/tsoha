from flask import redirect, render_template, request, session, flash
from app import app
import timemanager
import users
import forms
import secrets


@app.route("/form", methods=["POST"])
def form():
    form_id = request.form["form_id"]
    print(form_id)
    fields = forms.get_form_fields(form_id)
    return render_template("form.html", fields=fields, enumerate=enumerate)


@app.route("/create_user")
def create_page():
    return render_template("create_user.html")


@app.route("/create_user", methods=["POST"])
def create_user():
    username = request.form["username"]
    password = request.form["password"]
    password_repeat = request.form["password_repeat"]

    if users.create_user(username, password) and password == password_repeat:
        if users.login(username, password):
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        return redirect("/login")
    else:
        return redirect("/create_user")


@app.route("/result", methods=["POST"])
def result():
    task = request.form["task"]
    time = request.form["time"]

    if session["csrf_token"] != request.form["csrf_token"]:
        return "403 Forbidden"

    timemanager.add_timestamp(time, task, 1)
    total_time = timemanager.get_total_time_user(1)

    return render_template("result.html", task=task,
                           time=time,
                           total=total_time,
                           user_id=id
                           )


@app.route("/")
def index():
    try:
        username = session["username"]
        user_forms = forms.get_user_forms_id_and_title(username)
        admin_forms = forms.get_admin_form_id_and_title(username)
        print(admin_forms)
        if len(admin_forms) > 0:
            admin = True
        else:
            admin = False
    except:
        user_forms = []
        admin_forms = []
        admin = False
    return render_template("index.html", user_forms=user_forms, admin_forms=admin_forms, admin=admin)


@app.route("/login")
def show_login_field():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username, password):
        session["username"] = username
        session["csrf_token"] = secrets.token_hex(16)
        return redirect("/")
    else:
        return redirect("/login")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/create_form")
def dislay_create_form():
    return render_template("create_form.html")


@app.route("/create_form", methods=["POST"])
def create_form():
    fields = request.form["fields"]
    title = request.form["title"]
    forms.add_form(title, fields, session["username"])
    return redirect("/")


@app.route("/add_user_to_form", methods=["POST"])
def redirect_add_user():
    form_id = request.form["form_id"]
    return render_template("add_user.html", form_id=form_id)


@app.route("/add_user", methods=["POST"])
def add_user_to_form():
    username = request.form["username"]
    form_id = request.form["form_id"]
    admin = request.form["admin"]
    try:
        forms.add_user_to_form(username, int(form_id), admin)
        flash("Käyttäjä lisätty")
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/")
