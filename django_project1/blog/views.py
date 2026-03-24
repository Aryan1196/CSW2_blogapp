from django.shortcuts import render
from blog.models import Post
from django.views.generic import (ListView,DetailView,CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
   model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
   model = Post
   fields = ['title' , 'content']
   def form_valid(self,form):
      form.instance.author = self.request.user
      return super().form_valid(form)




def home(request):
   context = {
   'posts': Post.objects.all()
   }
   return render(request, 'blog/home.html', context)

# def home(request):
#    context = {
#    'posts': posts
#    }
   
def about(request):
   return render(request, 'blog/about.html', {'title': 'About'})


# posts = [
# {
#    'author': 'Aryan',
#    'title': 'Blog Post 1',
#    'content': 'Blog 1 Content!',
#    'date_posted': 'January 20, 2026'
# },
# {
#    'author': 'Ramu',
#    'title': 'Blog Post 2',
#    'content': 'Blog 2 Content!',
#    'date_posted': 'January 23, 2026'
# }
# ]