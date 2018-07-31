from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy,reverse
from django.views import generic
from .models import *

class IndexView(generic.ListView):
    model=Movie
    template_name='Movies/index.html'
    context_object_name="movies"


def moviedetails(request,pk):
    movie=Movie.objects.get(id=pk)
    return render(request,'Movies/movie_details.html',{'movie':movie})


class Genreview(generic.ListView):
    model=Movie
    template_name='Movies/genre.html'
    context_object_name="movies"



class Studioview(generic.ListView):
    model=Movie
    template_name='Movies/studio.html'
    context_object_name="movies"


class Directorview(generic.ListView):
    model=Movie
    template_name='Movies/director.html'
    context_object_name="movies"


class Movieview(generic.ListView):
    model=Movie
    template_name='Movies/movie.html'
    context_object_name="movies"