from db.run_sql import run_sql

from models.session import Session

def save(session):
    sql = "INSERT INTO sessions(name, description, upcoming) VALUES (%s, %s, %s) RETURNING id"
    values = [session.name, session.description, session.upcoming]
    results = run_sql(sql, values)
    session.id = results[0]['id']

def update(session):
    sql = "UPDATE sessions SET(name, description, upcoming) = (%s, %s, %s) WHERE id = %s"
    values = [session.name, session.description, session.upcoming, session.id]
    run_sql(sql,values)

def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)