from django.shortcuts import render,HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy,reverse
from .models import *
from .forms import EntryForm


# Create your views here.
class PagesIndex(generic.ListView):
    model = Page
    template_name = 'Pages/page_index.html'
    context_object_name = "pages"
    ordering = ['order']


class PageDetail(generic.DetailView):
    model = Page
    template_name = 'Pages/page_detail.html'
    context_object_name = "Page"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Pages = Page.objects.all().order_by('ordering')
        context['Pages'] = Pages
        return context
 

class PageAdd(generic.CreateView):
    model = Page
    fields = ['title', 'html_content', 'order']
    template_name = 'Pages/page_add.html'
    success_url = reverse_lazy('page_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Pages = Page.objects.all().order_by('ordering')
        context['Pages'] = Pages
        return context