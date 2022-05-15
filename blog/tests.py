from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Category, Post


class TestCreatePost(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        test_user = User.objects.create_user(username='test_user', password='test12345')
        test_post = Post.objects.create(category=1, title='Test Post', excerpt='Excerpt Test Post',
                                        content='Content Test Post', slug='post-title', author_id=1, status='published')

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        category = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user')
        self.assertEqual(excerpt, 'Excerpt Test Post')
        self.assertNotEqual(title, 'Bla bla bla')
        self.assertEqual(content, 'Content Test Post')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'Test Post')
