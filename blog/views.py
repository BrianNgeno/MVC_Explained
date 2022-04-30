import requests
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, View

from .forms import BlogForm
from .models import Blog


# Create your views here.
def index(request):
    return render(request,'index.html')


def blog(request):
    blog = Blog.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(blog, 2)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request, 'main/blog.html', locals())



def singleblog(request, pk,slug):

    blog = Blog.objects.all()
    single = get_object_or_404(Blog, pk=pk)
    
    return render(request, 'main/singleblog.html', {'single': single,'blog':blog})

class BlogCreateView( CreateView):
    template_name = 'main/upload.html'
    form_class = BlogForm
    success_url = '/blog/'
 
    def form_valid(self, form):
        p = form.save()
           
        return super().form_valid(form)

def delete_blog(request, blog_id):
    blog_item = Blog.objects.get(id=blog_id)
    Blog.delete_blog(blog_item)
    messages.warning(request, 'Blog item deleted successfully')
    return redirect('blog')
