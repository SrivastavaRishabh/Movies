from django.shortcuts import render,HttpResponseRedirect,reverse
from django.views.generic import ListView
from .models import *
from django.views.generic.detail import DetailView
from .forms import EntryForm


class PeopleListView(ListView):
    model = Person
    template_name = 'People/people_index.html'
    context_object_name = 'people'


class PersonDetails(DetailView):
    model = Person
    template_name = 'People/people_details.html'
    context_object_name = 'people'



def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('people-index'))
    else:
        form = EntryForm()
    return render(request, 'People/form.html', {'form': form})
