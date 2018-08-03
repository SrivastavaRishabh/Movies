from django.urls import path
from django.conf.urls import url
from messageboard import views


urlpatterns = [
    path('', views.Indexview.as_view(), name="index1"),
    path('entry/<int:pk>', views.Postdetails, name='postdetails'),
    # path('entry/<int:pk>', views.Tagdetails, name='tagdetails'),
    url(r'^search/$', views.tag_list, name='tagdetails'),
    path('entry/add', views.add, name='add'),

]

