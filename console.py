from models.member import Member
from models.session import Session
from models.booking import Booking


import repositories.member_repository as member_repository
import repositories.session_repository as session_repository
import repositories.bookings_repository as bookings_repository

member_repository.delete_all()
session_repository.delete_all()

member1 = Member('Sylvester', 74)
member_repository.save(member1)

session1 = Session('Yoga', 'just yoga lesson', True)
session_repository.save(session1)

booking1 = Booking(member1, session1)
bookings_repository.save(booking1)