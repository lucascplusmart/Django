from django.shortcuts import render

#from django.views import generic => #class BlogListView(generic.ListView):
from django.views.generic import ListView, DetailView , UpdateView

from django.views.generic.edit import CreateView, DeleteView

from .models import Post

from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin

from django.contrib import messages

from .forms import  PostForm

from django.contrib.auth.mixins import  LoginRequiredMixin
# Create your views here.


class  BlogListView(ListView):
    model = Post
    template_name= 'app_blog/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = "app_blog/detail.html"
    #context_object_name = 'custom'
    

class  BlogCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name= 'app_blog/post_new.html'
    #fields = '__all__' 
    #fields = ('__all__') 
    #fields = 'title','slug'
    #fields = ['title','slug']
    #fields = ('title','slug') 
    #fields = ('author','title','content') 

    success_message = "%(field)s - criado com sucesso!"
    # função para maniupular a menssagem 
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field = self.object.title,
        )
    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

class  BlogUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name= 'app_blog/post_edit.html'
    #fields = ('title','content')
    success_message = "%(field)s - atualizado com sucesso!"

    # função para maniupular a menssagem 
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field = self.object.title,
        )
    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

class  BlogDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Post
    template_name= 'app_blog/post_delete.html'
    success_url = reverse_lazy('home')

    success_message = "deletado com sucesso!"

    # função para maniupular a menssagem 
    def delete(self,request, *args,**kwargs):
        messages.success(self.request,self.success_message)
        return super(BlogDeleteView,self).delete(request, *args,**kwargs)
        
     
    
    
    