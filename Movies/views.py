from django.views import generic
from .models import Movie, Genre, Director, Studio


class MovieListView(generic.ListView):
    model = Movie
    template_name = "Movies/movies_index.html"
    context_object_name = 'movies'


class StudioListView(generic.ListView):
    model = Studio
    template_name = "Movies/studio_index.html"
    context_object_name = 'studios'


class StudioDetailView(generic.DetailView):
    model = Studio
    template_name = "Movies/studio_detail.html"
    context_object_name = 'studio'


class DirectorListView(generic.ListView):
    model = Director
    template_name = "Movies/director_index.html"
    context_object_name = 'directors'


class DirectorDetailView(generic.DetailView):
    model = Director
    template_name = "Movies/director_detail.html"
    context_object_name = 'director'


class GenreListView(generic.ListView):
    model = Genre
    template_name = "Movies/genre_index.html"
    context_object_name = 'genres'


class GenreDetailView(generic.DetailView):
    model = Genre
    template_name = "Movies/genre_detail.html"
    context_object_name = 'genre'


class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = "Movies/movie_detail.html"
    context_object_name = 'movie'
