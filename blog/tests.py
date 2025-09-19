from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post


class BlogTestCase(TestCase):
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123'
        )
        self.post = Post.objects.create(
            title='Test Post',
            content='This is test content',
            author=self.user
        )

    def test_home_page(self):
        """Test home page displays posts"""
        response = self.client.get(reverse('blog-home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail(self):
        """Test post detail page"""
        response = self.client.get(reverse('post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is test content')

    def test_post_create_requires_login(self):
        """Test that creating a post requires login"""
        response = self.client.get(reverse('post-create'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_post_create_authenticated(self):
        """Test post creation when logged in"""
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('post-create'))
        self.assertEqual(response.status_code, 200)

    def test_post_update_requires_author(self):
        """Test that updating a post requires being the author"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='otherpassword123'
        )
        self.client.login(username='otheruser', password='otherpassword123')
        response = self.client.get(reverse('post-update', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 403)  # Forbidden

    def test_post_delete_requires_author(self):
        """Test that deleting a post requires being the author"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='otherpassword123'
        )
        self.client.login(username='otheruser', password='otherpassword123')
        response = self.client.get(reverse('post-delete', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 403)  # Forbidden


class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_registration(self):
        """Test user registration"""
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login(self):
        """Test user login"""
        user = User.objects.create_user(
            username='loginuser',
            password='loginpassword123'
        )
        response = self.client.post(reverse('login'), {
            'username': 'loginuser',
            'password': 'loginpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
