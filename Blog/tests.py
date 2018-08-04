from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from .views import BlogDetails, BlogListView

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        resolved_view = resolve(reverse("blog-index"))
        self.assertEqual(resolved_view.func.view_class, BlogListView)
