from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy, reverse
from .models import Bookmarks
from .forms import BookmarksForm


class BookmarkIndex(generic.ListView):
    model = Bookmarks
    template_name = 'Bookmark/index.html'
    context_object_name = 'bookmarks'


class AddBookmark(CreateView):
    model = Bookmarks
    fields = ['name', 'url', 'description', 'tags']
    template_name = 'Bookmark/bookmark_add.html'
    context_object_name = 'fields'
    success_url = reverse_lazy('bookmark_index')


class UpdateBookmark(UpdateView):
    model = Bookmarks
    form_class = BookmarksForm
    template_name = 'Bookmark/bookmark_update.html'
    context_object_name = 'fields'
    success_url = reverse_lazy('bookmark_index')


class DeleteBookmark(DeleteView):
    model = Bookmarks
    template_name = 'Bookmark/delete.html'
    context_object_name = 'bookmark'

    def get_success_url(self):
        return reverse('bookmark_index')
