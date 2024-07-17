from django.contrib.auth import get_user_model 
from django.test import TestCase
from django.urls import reverse

from .models import Post

class TodoTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@gmail.com",
            password="testuserpswd1234",
        )
        
        cls.post = Post.objects.create(
            title="Task 1",
            body="Test user 1 has to do smt",
            author = cls.user,
        )
        
    def test_post_model(self):
        self.assertEqual(self.post.title, "Task 1")
        self.assertEqual(self.post.body, "Test user 1 has to do smt")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "Task 1")
        
    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test user 1 has to do smt")
        self.assertTemplateUsed(response, "home.html")
        
    def test_post_createview(self):
        response = self.client.post(
            reverse("post_new"),
            {
                "title": "Task 2",
                "body": "Another task",
                "author": self.user.id,
            },
        )
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Task 2")
        self.assertEqual(Post.objects.last().body, "Another task")
        
    def test_post_editview(self):
        response = self.client.post(
            reverse("post_edit", args="1"),
            {   
                "title": self.post.title,
                "body": "Another task edited",
                "deadline": "2024-07-16",
            },
        )
        
        print(response.content)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().body, "Another task edited")
        self.assertEqual(Post.objects.last().deadline.strftime("%Y-%m-%d"), "2024-07-16")
        
    def test_post_deleteview(self):
        response = self.client.post(
            reverse("post_delete", args="1"),
        )
        
        self.assertEqual(response.status_code, 302)