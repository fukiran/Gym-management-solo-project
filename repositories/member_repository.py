from db.run_sql import run_sql

from models.member import Member
from models.session import Session



def save(member):
    sql = "INSERT INTO members (name, age, premium, active) VALUES(%s, %s, %s, %s) RETURNING id"
    values = [member.name, member.age, member.premium, member.active]
    results = run_sql(sql, values)
    member.id = results[0]['id']

def select(id):
    member = None
    sql = "Select * FROM members WHERE id =%s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        member = Member(result['name'], result['age'], result['premium'], result['active'], result['id'])
    return member
    
def select_all():
    members = []
    sql ="SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['age'], row['premium'], row['active'], row['id'])
        members.append(member)
    return members

def update(member):
    sql = "UPDATE members SET (name, age, premium, active) = (%s, %s, %s, %s) WHERE id = %s"
    values = [member.name, member.age, member.premium, member.active, member.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def select_classes_booked_for(id):
    sessions = []
    sql = "SELECT sessions.* FROM sessions INNER JOIN bookings ON bookings.session_id = sessions.id WHERE bookings.member_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        session = Session(result["name"], result["description"], result['upcoming'], result['capacity'], result['offpeak'], result['id'])
        sessions.append(session)
    return sessions

def select_active():
    active_members = []
    sql = "SELECT * FROM members WHERE members.active = True"
    results = run_sql(sql)
    for row in results:
        active_member = Member(row['name'], row['age'], row['premium'], row['active'], row['id'])
        active_members.append(active_member)
    return active_members

def select_inactive():
    inactive_members = []
    sql = "SELECT * FROM members WHERE members.active = False"
    results = run_sql(sql)
    for row in results:
        inactive_member = Member(row['name'], row['age'], row['premium'], row['active'], row['id'])
        inactive_members.append(inactive_member)
    return inactive_members

def select_all_premium_active_members():
    premium_members = []
    sql = "SELECT * FROM members WHERE members.premium = TRUE AND members.active = TRUE"
    results = run_sql(sql)
    for row in results:
        premium_member = Member(row['name'], row['age'], row['premium'], row['active'], row['id'])
        premium_members.append(premium_member)
    return premium_members

