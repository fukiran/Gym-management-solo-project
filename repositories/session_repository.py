from db.run_sql import run_sql

from models.session import Session
from models.member import Member

def save(session):
    sql = "INSERT INTO sessions(name, description, upcoming) VALUES (%s, %s, %s) RETURNING id"
    values = [session.name, session.description, session.upcoming]
    results = run_sql(sql, values)
    session.id = results[0]['id']

def select(id):
    session = None
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    session = Session(result["name"], result["description"], result["upcoming"], result["id"])
    return session

def update(session):
    sql = "UPDATE sessions SET(name, description, upcoming) = (%s, %s, %s) WHERE id = %s"
    values = [session.name, session.description, session.upcoming, session.id]
    run_sql(sql,values)

def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)

def select_booked_members(id):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.session_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        member = Member(result["name"], result["age"])
        members.append(member)
    return members

def show_upcoming():
    upcoming = []
    sql = "SELECT * FROM sessions WHERE sessions.upcoming = True"
    results = run_sql(sql)
    for row in results:
        session = Session(row['name'], row['description'], row['upcoming'], row['id'])
        upcoming.append(session)
    return upcoming
