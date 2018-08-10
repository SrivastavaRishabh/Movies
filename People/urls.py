from django.urls import path
from People import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.PeopleListView.as_view(),
         name="people-index"),
    path('People/add', views.add,
         name='addperson'),
    path('<slug:slug>/', views.PersonDetails.as_view(),
         name='people-details'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
