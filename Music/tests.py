from django.test import TestCase
# from moviesapp.models import Movie
from django.urls import reverse


class MusicListView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/Music/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('music_index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_template(self):
        resp = self.client.get(reverse('music_index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'Music/music_index.html')
