from django.shortcuts import get_object_or_404, render

from .models import Artist


def artists(request):
    artist_list = Artist.objects.order_by('-date_created')[:3]
    context = {
        'artist_list': artist_list,
    }
    return render(request, 'resume/artists.html', context)


def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'resume/artist_detail.html', {'artist': artist})
