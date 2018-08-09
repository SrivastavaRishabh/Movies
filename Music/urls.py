from django.urls import path
from Music import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.MusicListView.as_view(), name='music_index'),
    path('Music/<slug>', views.MusicDetailView.as_view(), name='music_detail'),
    path('band', views.BandListView.as_view(), name='band_index'),
    path('band/<slug>', views.BandDetailView.as_view(), name='band_detail'),
    path('album', views.AlbumListView.as_view(), name='album_index'),
    path('album/<slug>', views.AlbumDetailView.as_view(), name='album_detail'),
    path('label', views.LabelListView.as_view(), name='label_index'),
    path('label/<slug>', views.LabelDetailView.as_view(), name='label_detail'),
    path('musician', views.MusicianListView.as_view(), name='musician_index'),
    path('musician/<int:pk>', views.MusicianDetailView.as_view(), name='musician_detail'),
    path('genre', views.GenreListView.as_view(), name='genre_index'),
    path('genre/<slug>', views.GenreDetailView.as_view(), name='genre_detail'),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)