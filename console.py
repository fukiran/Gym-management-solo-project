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
member2 = Member('Arnold', 73)
member_repository.save(member2)
session1 = Session('Yoga', 'just yoga lesson', False)
session_repository.save(session1)
session2 = Session('Boxing', 'by Ivan Drago', True)
session_repository.save(session2)
session3 = Session('Belly Dancing', 'by Zoe Jakes', True)
session_repository.save(session3)

booking1 = Booking(member1, session1)
bookings_repository.save(booking1)
booking2 = Booking(member2, session1)
bookings_repository.save(booking2)

print(session_repository.select_booked_members(session1.id))
print(session_repository.show_upcoming())