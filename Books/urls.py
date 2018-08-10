from django.urls import path
from Books import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.BooksIndex.as_view(),
         name='books_index'),
    path('Books/book_add/', views.BookAdd,
         name='book_add'),
    path('Books/<int:pk>/book_update/',
         views.UpdateBook.as_view(), name='book_update'),
    path('Books/<int:pk>/book_delete/',
         views.DeleteBook.as_view(), name='book_delete'),
    path('Books/search/', views.book_list,
         name='book_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
