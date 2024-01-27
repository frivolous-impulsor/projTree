from django.test import TestCase
from .models import Profile
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your tests here.

class UserTests(TestCase):
    username = 'newUser'
    email = 'new@gmail.com'

    def test_register_page_status_code(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
    

