import mock

from django.test import RequestFactory, TestCase
from django.urls import reverse

# app imports
from .models import Artist
from .views import IndexView


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
