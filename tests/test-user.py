import unittest
from app.models import User
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username="paul", email="paul@gmail.com", password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
        
    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))
        
    def save_account(self):
        db.session.add(self.new_user)
        db.session.commit()
        self.asserTrue(len(user.id) > 0)

