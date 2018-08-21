from django.urls import path

# app imports
from . import views


app_name = 'resume'
urlpatterns = [
    path('', views.IndexView.as_view(), name='artists'),
    path('artist/<uuid:artist_id>/', views.DetailView.as_view(), name='artist_detail'),
    path('artist/create/', views.ArtistCreate.as_view(), name='artist_create'),
]
