from django.shortcuts import render,HttpResponseRedirect,reverse
from django.views.generic import ListView
from .models import *
from django.views.generic.detail import DetailView
from .forms import EntryForm


class BlogListView(ListView):
    model = Post
    template_name = 'Blog/blog_index.html'
    context_object_name = 'blogs'

class BlogDetails(DetailView):
    model = Post
    template_name = 'Blog/blog_details.html'
    context_object_name = 'blog'


def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog-index'))
    else:
        form = EntryForm()
    return render(request, 'Blog/form.html', {'form': form})