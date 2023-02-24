from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from .filters import ProductFilter
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ProductForm
from .models import *
from django import forms


class ProductsList(ListView):
    model = Post
    ordering = '-time_created'
    template_name = 'news.html'
    context_object_name = 'post'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['filterset'] = self.filterset
        return context

class ProductDetail(DetailView):
    model = Post
    template_name = 'news_pk.html'
    context_object_name = 'post'

def create_post(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        form.save()
        return HttpResponseRedirect('/news')
    form = ProductForm()
    return render(request, 'post_edit.html', {'form': form})

class ProductCreate(CreateView):
    form_class = ProductForm
    model = Post
    template_name = 'post_edit.html'

class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Post
    template_name = 'post_edit.html'

class ProductDelete(DeleteView):
    model = Post
    template_name = 'product_delete.html'
    success_url = reverse_lazy('post_list')
