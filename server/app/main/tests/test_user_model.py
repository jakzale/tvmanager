from unittest2 import TestCase
from factories import UserFactory


class UserModelTestCase(TestCase):
    def test_password_setter(self):
        u = UserFactory(password='Bob')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = UserFactory(password='Bob')
        with self.assertRaises(AttributeError):
            u.password()

    def test_password_verification(self):
        u = UserFactory(password='Bob')
        self.assertTrue(u.verify_password('Bob'))
        self.assertFalse(u.verify_password('Steve'))

    def test_password_salts_are_random(self):
        u = UserFactory(password='Bob')
        u2 = UserFactory(password='Bob')
        self.assertTrue(u.password_hash != u2.password_hash)
