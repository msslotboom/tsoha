from db import db
import users

def get_form_fields(form_id):
    sql = "SELECT fields FROM forms WHERE id=:id"
    result = db.session.execute(sql, {"id": form_id}).fetchone()[0]
    result_list = result.split(";")
    result_list.pop()
    return result_list

def add_form(title, fields, admin):
    add_field = "INSERT INTO forms (fields, title) VALUES (:fields, :title) RETURNING ID"
    execute = db.session.execute(add_field, {"fields":fields, "title":title})
    form_id = execute.fetchone()[0]
    db.session.commit()

    admin_id = users.get_user_id(admin)
    add_form_to_user_id = "INSERT INTO userform (user_id, form_id, admin) VALUES (:user_id, :form_id, :admin)"
    execute = db.session.execute(add_form_to_user_id, {"user_id":admin_id, "form_id":form_id, "admin":True})
    db.session.commit()

def get_user_forms_id_and_title(username):
    user_id = users.get_user_id(username)
    sql = "SELECT id, title FROM forms WHERE id IN (SELECT form_id FROM userform WHERE user_id=:user_id)"
    result = db.session.execute(sql, {"user_id":user_id}).fetchall()
    return result
