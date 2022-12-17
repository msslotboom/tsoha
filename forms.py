from db import db

def get_form_fields(form_id):
    print("test")
    sql = "SELECT fields FROM forms WHERE id=:id"
    result = db.session.execute(sql, {"id": form_id}).fetchone()[0]
    result_list = result.split(";")
    result_list.pop()
    return result_list