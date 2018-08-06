from django.urls import path
from Pages import views

urlpatterns = [
    path('', views.PagesIndex.as_view(),name='page_index'),
    path('Pages/add/', views.PageAdd.as_view(), name="page_add"),
    path('Pages/<slug>/', views.PageDetail.as_view(), name="page_detail"),
]