from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from . models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
     model = Post
     template_name = 'blog/post_detail.html'

class BlogCreateView(SuccessMessageMixin,CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ('autor','titulo','conteudo', 'status')
    success_message = " O artigo %(titulo)s foi criado com sucesso"

    def get_success_message(self, cleaned_data):
         return self.success_message % dict(
             cleaned_data,
             calculated_field=self.object.titulo,
         )

class BlogUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ('autor','titulo','conteudo', 'status')
    success_message = " O artigo %(titulo)s foi alterado com sucesso"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.titulo,
        )

class BlogDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    success_message = " O artigo foi deletado com sucesso"

    def delete (self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)