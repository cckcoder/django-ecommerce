from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from django.test.client import RequestFactory
from django.urls import reverse

from store.models import *
from store.views import *


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username="admin")
        Category.objects.create(name="django", slug="django")
        Product.object.create(
            category_id=1,
            title="django beginners",
            created_by_id=1,
            slug="django-beginners",
            price="20.00",
            image="django",
        )

    def test_homepage_url(self):
        response = self.c.get("/")
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.c.get(
            reverse("store:product_detail", args=["django-beginners"])
        )
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        response = self.c.get(reverse("store:category_list", args=["django"]))
        self.assertEqual(response.status_code, 200)

    def test_url_allowed_hosts(self):
        resp = self.c.get("/", HTTP_HOST="noaddress.com")
        self.assertEqual(resp.status_code, 400)
        resp = self.c.get("/", HTTP_HOST="yourdomain.com")
        self.assertEqual(resp.status_code, 200)

    def test_homepage_html(self):
        response = self.c.get("")
        html = response.content.decode("utf8")
        self.assertIn("<title>BookStore</title>", html)
        self.assertEqual(response.status_code, 200)

    # def test_view_function(self):
    #     resp = self.factory.get("item/django-beginners")
    #     self.assertIn("<title>Home</title>", resp)
    #     self.assertEqual(resp.sta, 200)
