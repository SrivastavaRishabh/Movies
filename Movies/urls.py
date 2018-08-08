from django.urls import path
from Movies import views

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movies_index'),
    path('Movies/<slug>', views.MovieDetailView.as_view(), name='movie_detail'),
    path('director', views.DirectorListView.as_view(), name='director_index'),
    path('director/<int:pk>/', views.DirectorDetailView.as_view(), name='director_detail'),
    path('studio', views.StudioListView.as_view(), name='studio_index'),
    path('studio/<slug>/', views.StudioDetailView.as_view(), name='studio_detail'),
    path('genre', views.GenreListView.as_view(), name='genre_index'),
    path('genre/<slug>/', views.GenreDetailView.as_view(), name='genre_detail'),
       
]
