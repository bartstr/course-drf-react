from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from blog.models import Category, Post
from django.contrib.auth.models import User


class PostTests(APITestCase):

    def test_view_posts(self):

        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        client = APIClient()
        self.test_category = Category.objects.create(name='django')
        self.test_user = User.objects.create_superuser(
            username='test_user', password='password123')
        client.login(username=self.test_user.username, password='password123')
        data = {"title": "new", "author": 1, "excerpt": "new", "content": "new"}
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):
        client = APIClient()
        self.test_category = Category.objects.create(name='django')
        self.test_user = User.objects.create_user(
            username='test_user', password='password123')
        self.test_user2 = User.objects.create_user(
            username='test_user2', password='password1234')
        test_post = Post.objects.create(category_id=1, title='Post title', excerpt='old', content='New', author_id=1,
                                        slug='post-title', status='published')
        url = reverse(('blog_api:detailcreate'), kwargs={'pk': 1})
        client.login(username=self.test_user.username, password='password123')
        response = client.put(
            url, {"title": "new", "author": 1, "excerpt": "new", "content": "changed", "status": "published"},
            format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
