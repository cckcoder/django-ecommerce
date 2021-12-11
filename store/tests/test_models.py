from itertools import product
from django.test import TestCase

from django.contrib.auth.models import User
from store.models import *


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name="vim", slug="vim")

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_name(self):
        data = self.data1
        self.assertEqual(str(data), "vim")


class TestProduct(TestCase):
    def setUp(self):
        Category.objects.create(name="neovim", slug="neovim")
        User.objects.create(username="admin")
        self.data = Product.objects.create(
            category_id=1,
            title="neovim beginners",
            created_by_id=1,
            slug="neovim beginners",
            price="15.99",
        )

    def test_products_model_entry(self):
        data = self.data
        self.assertTrue(isinstance(data, Product))
        self.assertTrue(str(data), "neovim beginners")
