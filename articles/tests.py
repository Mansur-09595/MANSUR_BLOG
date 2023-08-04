from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article, Comment

class ModelTests(TestCase):

    def setUp(self):
        # Создадим тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_article_creation(self):
        # Проверим, что модель Article создается корректно
        article = Article.objects.create(title='Test Article', body='This is a test article', author=self.user)
        self.assertEqual(article.title, 'Test Article')
        self.assertEqual(article.body, 'This is a test article')
        self.assertEqual(article.author, self.user)

    def test_comment_creation(self):
        # Проверим, что модель Comment создается корректно
        article = Article.objects.create(title='Test Article', body='This is a test article', author=self.user)
        comment = Comment.objects.create(article=article, comment='Test Comment', body='This is a test comment', author=self.user)
        self.assertEqual(comment.article, article)
        self.assertEqual(comment.comment, 'Test Comment')
        self.assertEqual(comment.body, 'This is a test comment')
        self.assertEqual(comment.author, self.user)
