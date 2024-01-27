from django.test import TestCase
from .models import Profile
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your tests here.

class UserTests(TestCase):
    def setUp(self):
        self.testUser = get_user_model().objects.create(username = 'testuser',
                                                    email = 'test@gmail.com',
                                                    password = 'secrete')
        self.testProfile = Profile.objects.create(user = self.testUser)
