from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Seed

# Create your tests here.
class SeedTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(username='testuser',
                                                    email='test@gmail.com',
                                                    password='secret')
        return super().setUp()
    def test_seed_list_view(self):
        response = self.client.get(reverse('seed_list'))

        self.assertEqual(response.status_code, 200)
    
    def test_seed_create_view(self):
        self.client.post(reverse('seed_create'), {
            'author' : self.user,
            'seedName' : 'a seed name',
            'content' : 'content of the seed'
        })
        self.assertEqual(Seed.objects.last().seedName, 'a seed name')
    
    def test_seed_update_view(self):
        response = self.client.post(reverse('seed_update', args='1'), {
            'seedName' : 'update name',
            'content' : 'update content'
        })
        self.assertEqual(response.status_code, 302)

    def test_seed_delete_view(self):
        response = self.client.get(reverse('seed_delete', args = '1'))
        self.assertEqual(response.status_code, 302)