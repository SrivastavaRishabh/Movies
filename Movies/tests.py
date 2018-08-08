from django.test import TestCase
# from moviesapp.models import Movie
from django.urls import reverse


class MovieListView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/Movies/')
        self.assertEqual(resp.status_code, 200)
