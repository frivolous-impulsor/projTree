from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from .models import Post

# Create your tests here.

class PostTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser',
                                                    email='test@gmail.com',
                                                    password='secret')
        self.post = Post.objects.create(title='testTitle', 
                                        content='testContent',
                                        author = self.user)
        
        self.deletePost = Post.objects.create(title='DeletetestTitle', 
                                        content='DeletetestContent',
                                        author = self.user)
        
    def test_str_representation(self):
        post = Post(title='a sample title')
        self.assertEqual(str(post), f'{post.title} Post')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'testTitle')
        self.assertEqual(f'{self.post.content}', 'testContent')
        self.assertEqual(f'{self.post.author}', 'testuser')

    def test_post_list(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testContent')
        self.assertTemplateUsed(response, 'post/post_list.html')

    def test_post_detail(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk':1}))
        no_response = self.client.get(reverse('post_detail', kwargs={'pk':100}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'testContent')
        self.assertTemplateUsed(response, 'post/post_detail.html')

    def test_post_create(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'new title',
            'content': 'new content',
            'author': self.user
        })
        self.assertEqual(response.status_code, 302)

    def test_post_update(self):
        response = self.client.post(reverse('post_update', args='1'), {
            'title': 'updated',
            'content': 'updated content'
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete(self):
        response = self.client.get(reverse('post_delete', kwargs={'pk':1}))
        self.assertEqual(response.status_code, 302)