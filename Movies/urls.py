from django.urls import path
from Movies import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    path('genre', views.Genreview.as_view(),name='genre'),
    path('studio', views.Studioview.as_view(),name='studio'),
    path('movie', views.Movieview.as_view(),name='movie'),
    path('director', views.Directorview.as_view(),name='director'),
    path('entry/<int:pk>',views.moviedetails,name='details'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
