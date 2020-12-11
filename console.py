from models.member import Member
from models.session import Session


import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

member_repository.delete_all()
session_repository.delete_all()

member1 = Member('Sylvester', 62)
member_repository.save(member1)

session1 = Session('Yoga', 'just yoga lesson', True)
session_repository.save(session1)