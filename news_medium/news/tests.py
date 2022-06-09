from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse, resolve

from .views import *


class NewsTests(TestCase):


    # url test
    def test_url_logout(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout_user)

    def test_url_article_list(self):
        url = reverse('article_list')
        print(resolve(url).func.view_class)
        self.assertEqual(resolve(url).func.view_class, ArticleListView)

    def test_url_add_comment(self):
        url = reverse('add_comment')
        print(resolve(url).func.view_class)
        self.assertEqual(resolve(url).func.view_class, CommentCreateView)

    def test_url_add_article(self):
        url = reverse('add_article')
        print(resolve(url).func.view_class)
        self.assertEqual(resolve(url).func.view_class, ArticleCreateView)

    def test_url_add_tag(self):
        url = reverse('add_tag')
        print(resolve(url).func.view_class)
        self.assertEqual(resolve(url).func.view_class, TagsCreateView)

    def test_url_one_article(self):
        url = reverse('one_article', args=['hello'])
        print(resolve(url).func.view_class)
        self.assertEqual(resolve(url).func.view_class, ArticleDetailView)

    def test_url_tags(self):
        url = reverse('tags')
        print(resolve(url).func.view_class)
        self.assertEqual(resolve(url).func.view_class, TagsListVies)

    def test_url_login(self):
        url = reverse('login')
        print(resolve(url).func.view_class)
        self.assertEqual(resolve(url).func.view_class, LoginUser)

    def test_url_register(self):
        url = reverse('register')
        print(resolve(url).func.view_class)
        self.assertEqual(resolve(url).func.view_class, RegisterUser)

    def test_url_add_article(self):
        url = reverse('article_by_tag', args=['test_slug'])
        print(resolve(url).func.view_class)
        self.assertEqual(resolve(url).func.view_class, ShowArticleListView)

    # test view

    clietn = Client()

    def test_view_article_by_tag(self):
        response = self.clietn.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/article/main_page.html')

    def test_view_add_comment(self):
        response = self.clietn.get(reverse('add_comment'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/comments/add_comment.html')

    def test_view_add_article(self):
        response = self.clietn.get(reverse('add_article'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/article/add_article.html')

    def test_view_add_tag(self):
        response = self.clietn.get(reverse('add_tag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/tags/add_tag.html')

    def test_view_tags(self):
        response = self.clietn.get(reverse('tags'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/tags/tags.html')

    def test_view_login(self):
        response = self.clietn.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/login_register/login.html')

    def test_view_register(self):
        response = self.clietn.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/login_register/register.html')

    def test_view_logout(self):
        response = self.clietn.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    # models

    def setUp(self):
        self.category = CategoryArticle.objects.create(name_category='Test tag', slug='test-tag')
        self.author = User.objects.create(username='Yan4321', email='Yan1234@gmail.com', password='qazedctgb1234')
        self.article = Article.objects.create(title='test', text='test_text', author=self.author, slug_field='test_slug',
                                         status='publisher', category=self.category)

    def test_category_article_is_text(self):
        self.assertEqual(str(self.category), 'Test tag')



    def test_article_model_is_not_empty(self):
        self.assertNotEqual(self.article, None)

    def test_article_is_unique(self):
        with self.assertRaises(Exception):
            Article.objects.create(title='test', text='test_text', author=self.author, slug_field='test_slug',
                                   status='publisher', category=self.category)


    def test_tag_is_unique(self):
        with self.assertRaises(Exception):
            CategoryArticle.objects.create(name_category='Test tag', slug='test-tag')


