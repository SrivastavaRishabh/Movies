from django.urls import path
from django.conf.urls import url
from Blog import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.BlogListView.as_view(), name="blog-index"),
    path('blog/add', views.add, name='addblog'),
    path('<slug:slug>/', views.BlogDetails.as_view(), name='blog-details'),
]
