from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy,reverse
from django.views import generic
from .models import *


class MusicListView(generic.ListView):
    model = Track
    template_name = 'Music/music_index.html'
    context_object_name = "tracks"


class MusicDetailView(generic.DetailView):
    model = Track
    template_name = 'Music/music_detail.html'
    context_object_name = 'track'


class BandListView(generic.ListView):
    model = Band
    template_name = "Music/band_index.html"
    context_object_name = 'bands'


class BandDetailView(generic.DetailView):
    model = Band
    template_name = "Music/band_detail.html"
    context_object_name = 'band'


class AlbumListView(generic.ListView):
    model = Album
    template_name = "Music/album_index.html"
    context_object_name = 'albums'


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = "Music/album_detail.html"
    context_object_name = 'album'


class LabelListView(generic.ListView):
    model = Label
    template_name = "Music/label_index.html"
    context_object_name = 'labels'


class LabelDetailView(generic.DetailView):
    model = Label
    template_name = "Music/label_detail.html"
    context_object_name = 'label'


class MusicianListView(generic.ListView):
    model = Musician
    template_name = "Music/musician_index.html"
    context_object_name = 'musicians'


class MusicianDetailView(generic.DetailView):
    model = Musician
    template_name = "Music/musician_detail.html"
    context_object_name = 'musician'

class GenreListView(generic.ListView):
    model = Genre
    template_name = "Music/genre_index.html"
    context_object_name = 'genres'


class GenreDetailView(generic.DetailView):
    model = Genre
    template_name = "Music/genre_detail.html"
    context_object_name = 'genre'