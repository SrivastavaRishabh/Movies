from django.shortcuts import render,HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views import generic
from .models import *
from .filter import TagFilter
from .forms import EntryForm
# Create your views here.


class Indexview(generic.ListView):
    model = post
    template_name = 'messageboard/index.html'
    context_object_name = 'posts'


def Postdetails(request, pk):
    Post = post.objects.get(id=pk)
    return render(request, 'messageboard/post_details.html', {'Post': Post})



def tag_list(request):
	Post = post.objects.all()
	filter = TagFilter(request.GET, queryset = Post)
	return render(request, 'messageboard/filter.html', {'filter': filter})  


def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = EntryForm()
    return render(request, 'messageboard/form.html', {'form': form})