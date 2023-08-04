from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomUser


class CustomUserModelTests(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword',
            age=25,
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.age, 25)
        self.assertTrue(user.check_password('testpassword'))

    def test_create_superuser(self):
        superuser = CustomUser.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpassword',
            age=30,
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertEqual(superuser.age, 30)


class HomePageViewTests(TestCase):
    def test_home_page_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class SignUpViewTests(TestCase):
    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form_valid(self):
        response = self.client.post(reverse('signup'), data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword',
            'password2': 'newpassword',
            'age': 25,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_signup_form_invalid(self):
        response = self.client.post(reverse('signup'), data={
            'username': 'newuser',
            'email': 'invalidemail',  # Invalid email format
            'password1': 'newpassword',
            'password2': 'newpassword',
            'age': 25,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Enter a valid email address.')


class CustomUserAPIViewTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword',
            age=25,
        )

    def test_create_user_api(self):
        url = reverse('user-create')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'age': 30,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 2)

    def test_retrieve_user_api(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_update_user_api(self):
        url = reverse('user-detail', args=[self.user.id])
        data = {'username': 'updateduser'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')

    def test_delete_user_api(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CustomUser.objects.count(), 0)
