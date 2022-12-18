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
    add_user_to_form(admin, form_id, True)

def get_user_forms_id_and_title(username):
    user_id = users.get_user_id(username)
    sql = "SELECT id, title FROM forms WHERE id IN (SELECT form_id FROM userform WHERE user_id=:user_id)"
    result = db.session.execute(sql, {"user_id":user_id}).fetchall()
    return result

def get_user_forms_id(username):
    user_id = users.get_user_id(username)
    sql = "SELECT id FROM forms WHERE id IN (SELECT form_id FROM userform WHERE user_id=:user_id)"
    results = db.session.execute(sql, {"user_id":user_id}).fetchall()
    result_list = []
    for result in results:
        result_list.append(result[0])
    return result_list

def is_admin_in_form(username, form_id):
    user_id = users.get_user_id(username)
    sql = "SELECT admin FROM userform WHERE form_id=:form_id AND user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id, "form_id":form_id})
    return result

def add_user_to_form(username, form_id:int, admin:bool):
    user_id = users.get_user_id(username)
    if user_id is None:
        raise Exception("Käyttäjää ei ole olemassa!")

    user_form_ids = get_user_forms_id(username)
    if form_id in user_form_ids:
        if is_admin_in_form(username, form_id):
            return
        add_form_to_user_id = "UPDATE userform SET admin=:admin WHERE form_id=:form_id AND user_id=:user_id"
        db.session.execute(add_form_to_user_id, {"user_id":user_id, "form_id":form_id, "admin":admin})
        db.session.commit()
    else:
        add_form_to_user_id = "INSERT INTO userform (user_id, form_id, admin) VALUES (:user_id, :form_id, :admin)"
        db.session.execute(add_form_to_user_id, {"user_id":user_id, "form_id":form_id, "admin":admin})
        db.session.commit()
