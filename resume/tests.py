import mock

from django.test import RequestFactory, TestCase
from django.urls import reverse

# app imports
from .models import Artist, Language, Skill
from .views import IndexView, DetailView


class TestViews(TestCase):

    @mock.patch('resume.views.Artist.objects')
    def test_list_view_return_artists(self, mock_objects):
        artists_qs = [
            Artist(
                id='db5a73bb-fc16-4b93-9df3-07ee4a1f6d7f',
                first_name='Pedro',
                last_name='Curado',
                email='pedro@mail.com'
            )
        ]
        mock_objects.order_by.return_value = artists_qs

        url = reverse('resume:artists')
        factory = RequestFactory()
        request = factory.get(url)
        response = IndexView.as_view()(request)

        # self.assertEqual(response.context_data['artist_list'], artist_qs)
        self.assertEqual(response.status_code, 200)

    @mock.patch('resume.views.Artist.objects')
    def test_detail_view_return_artist(self, mock_object):
        artist = Artist(
            id='95e6f821-aaf6-44d5-a0fc-658cd950eed5',
            first_name='Pedro',
            last_name='Curado',
            email='pedro@mail.com'
        )
        mock_object.get.return_value = artist

        kwargs = {'artist_id': artist.id}
        url = reverse('resume:artist_detail', kwargs=kwargs)
        factory = RequestFactory()
        request = factory.get(url)
        response = DetailView.as_view()(request, **kwargs)

        # self.assertEqual(response.context_data['artist'], artist)
        self.assertEqual(response.status_code, 200)

    def test_artist_model_representation(self):
        expected_result = '<Artist: Pedro Curado - pedro@mail.com>'
        artist = Artist(
            first_name='Pedro',
            last_name='Curado',
            email='pedro@mail.com',
        )
        self.assertEqual(artist.__repr__(), expected_result)

    def test_language_model_representation(self):
        expected_result = '<Language: pt>'
        language = Language(name='pt')

        self.assertEqual(language.__repr__(), expected_result)

    def test_skil_model_representation(self):
        expected_result = '<Skill: Horse riding>'
        skill = Skill(name='Horse riding')

        self.assertEqual(skill.__repr__(), expected_result)
