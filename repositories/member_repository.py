from db.run_sql import run_sql

from models.member import Member
from models.session import Session



def save(member):
    sql = "INSERT INTO members (name, age) VALUES(%s, %s) RETURNING id"
    values = [member.name, member.age]
    results = run_sql(sql, values)
    member.id = results[0]['id']

def select(id):
    member = None
    sql = "Select * FROM members WHERE id =%s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        member = Member(result['name'], result['age'], result['id'])
    return member
    
def select_all():
    members = []
    sql ="SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['age'], row['id'])
        members.append(member)
    return members

def update(member):
    sql = "UPDATE members SET (name, age) = (%s, %s) WHERE id = %s"
    values = [member.name, member.age, member.id]
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
        session = Session(result["name"], result["description"], result['upcoming'], result['capacity'], result['id'])
        sessions.append(session)
    return sessions