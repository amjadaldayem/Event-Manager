# from django.test import TestCase
from django.test import TestCase
from user.models import User
from .tests_config import TEST_USER_CREDENTIALS as test_user

# Create your tests here.


class UserModelTest(TestCase):
    @classmethod
    def create_user(cls, username=test_user['username'],
                    email=test_user['email'], first_name='event',
                    password=test_user['password'], last_name='manager'):
        user = User.objects.create(
            username=username, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def test_user_creation(self):
        user_instance = self.create_user()
        self.assertTrue(isinstance(user_instance, User))

    def test_user_fullname(self):
        user_instance = self.create_user()
        self.assertEqual(user_instance.get_full_name(), user_instance.first_name + user_instance.last_name)
        self.assertNotEqual(user_instance.get_full_name(),
                            'invalid user first and last name')

    def test_user_shortname(self):
        user_instance = self.create_user()
        self.assertEqual(user_instance.get_short_name(), user_instance.first_name)
        self.assertNotEqual(user_instance.get_short_name(), 'invalid user first name')