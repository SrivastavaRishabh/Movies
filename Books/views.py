from django.shortcuts import render,HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy,reverse
from django.views.generic.edit import DeleteView,UpdateView
from .models import Books
from .forms import EntryForm
from .filter import BookFilter
# Create your views here.


class BooksIndex(generic.ListView):
  model = Books
  template_name = 'Books/books_index.html'
  context_object_name = 'books'


class UpdateBook(UpdateView):
    model = Books
    form_class = EntryForm
    template_name = 'Books/book_update.html'
    context_object_name = 'fields'
    success_url = reverse_lazy('books_index')


def BookAdd(request):
    if request.method == 'POST':
        form = EntryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books_index'))
    else:
        form = EntryForm()
    return render(request,'Books/book_add.html',{'form':form})


class DeleteBook(DeleteView):
    model = Books
    template_name = 'Books/book_delete.html'
    context_object_name = 'book'
    # Notice get_success_url is defined here and not in the model, because the model will be deleted
    def get_success_url(self):
        return reverse('books_index')


def book_list(request):
	books = Books.objects.all()
	filter = BookFilter(request.GET, queryset = books)
	return render(request, 'Books/filter.html', {'filter' : filter})    


