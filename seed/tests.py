from django.test import TestCase
from django.urls import reverse
from .models import Seed

# Create your tests here.
class SeedTests(TestCase):
    def test_seed_list_view(self):
        response = self.client.get(reverse('seed_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_seed_create_view(self):
        response = self.client.post(reverse('seed_create'), {
            'seedName' : 'a seed name',
            'content' : 'content of the seed'
        })
        self.assertEqual(response.status_code, 302)
    
    def test_seed_update_view(self):
        response = self.client.post(reverse('seed_update', args='1'), {
            'seedName' : 'update name',
            'content' : 'update content'
        })
        self.assertEqual(response.status_code, 302)

    def test_seed_delete_view(self):
        response = self.client.get(reverse('seed_delete', args = '1'))
        self.assertEqual(response.status_code, 302)