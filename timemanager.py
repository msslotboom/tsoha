from db import db

def add_timestamp(time, task, user_id):
    sql_insert = "INSERT INTO time (hours, task, user_id, logged_at) VALUES (:time, :task, :id, NOW())"
    db.session.execute(sql_insert, {"time":time, "task":task, "id":user_id})
    db.session.commit()

def get_total_time_user(user_id):
    sql_tot_time = "SELECT SUM (hours) FROM time WHERE user_id =:user_id"
    result = db.session.execute(sql_tot_time, {"user_id":user_id})
    total = result.fetchone()[0]
    db.session.commit()
    return total