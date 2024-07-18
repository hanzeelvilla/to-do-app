from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class AccountTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        
    def test_signup_view(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("signup.html")
        
    def test_signup_success(self):
        data = {
            'username': "normaluser1",
            'password1': "normalpswd1234",
            'password2': "normalpswd1234",
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username="normaluser1").exists())