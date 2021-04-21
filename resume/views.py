from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import CreateView

# app imports
from .models import Artist


class IndexView(generic.ListView):
    template_name = 'resume/artists.html'
    context_object_name = 'artist_list'

    def get_queryset(self):
        return Artist.objects.order_by('-date_created')[:3]


class ArtistCreate(CreateView):
    model = Artist
    fields = ['first_name', 'last_name', 'email']


class DetailView(generic.DetailView):
    model = Artist
    template_name = 'resume/artist_detail.html'

    def get_object(self, queryset=None):
        return Artist.objects.get(id=self.kwargs.get('artist_id'))
