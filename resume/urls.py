from django.urls import path

# app imports
from . import views


app_name = 'resume'
urlpatterns = [
    path('', views.artists, name='artists'),
]
