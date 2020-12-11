import unittest

from models.session import Session

class TestSession(unittest.TestCase):

    def setUp(self):
        self.session = Session('Yoga', 'just yoga lesson', True)

    def test_session_has_name(self):
        self.assertEqual("Yoga",self.session.name)

    def test_session_has_desription(self):
        self.assertEqual('just yoga lesson',self.session.description)
    
    def test_session_has_upcoming_value(self):
        self.assertEqual(True,self.session.upcoming)