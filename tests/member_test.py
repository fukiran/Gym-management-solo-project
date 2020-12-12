import unittest

from models.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member = Member("Sylvester", 74)

    def test_member_has_name(self):
        self.assertEqual("Sylvester",self.member.name)

    def test_member_has_age(self):
        self.assertEqual(74,self.member.age)
        