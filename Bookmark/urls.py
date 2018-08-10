from django.urls import path
from Bookmark import views

urlpatterns = [
    path('', views.BookmarkIndex.as_view(),
         name='bookmark_index'),
    path('Bookmark/add', views.AddBookmark.as_view(),
         name='bookmark_add'),
    path('Bookmark/<int:pk>/update/', views.UpdateBookmark.as_view(),
         name='bookmark_update'),
    path('Bookmark/<int:pk>/delete/', views.DeleteBookmark.as_view(),
         name='bookmark_delete'),
]
