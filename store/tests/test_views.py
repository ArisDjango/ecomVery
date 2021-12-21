from importlib import import_module
from unittest import skip

from django.conf import settings
from django.contrib.auth.models import User
from account.models import UserBase
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import product_all


@skip("demonstrating skipping")
class TestSkip(TestCase):
    def test_skip_exmaple(self):
        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        # self.factory = RequestFactory()
        # User.objects.create(username='admin')
        UserBase.objects.create(email='winandiaris@gmail.com')
        Category.objects.create(name='Komputer', slug='komputer')
        Product.objects.create(category_id=1, title='Buku Python', created_by_id=1,
                               slug='buku-python', price='20.00', image='django')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/', HTTP_HOST='ariswong.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='aris.com')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_list_url(self):
        """
        Test category response status
        """
        response = self.c.get(
            reverse('store:category_list', args=['komputer']))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test items response status
        """
        response = self.c.get(
            reverse('store:product_detail', args=['buku-python']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Example: code validation, search HTML for text
        """
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE) 
        request.session = engine.SessionStore()
        response = product_all(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Book Store</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    ## deactivated after using a session
    # def test_view_function(self):
    #     """
    #     Example: Using request factory
    #     """
    #     request = self.factory.get('/django-beginners')
    #     response = product_all(request)
    #     html = response.content.decode('utf8')
    #     self.assertIn('<title>Book Store</title>', html)
    #     self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
    #     self.assertEqual(response.status_code, 200)