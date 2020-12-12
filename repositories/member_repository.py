from db.run_sql import run_sql

from models.member import Member


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
    return result
    
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

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)