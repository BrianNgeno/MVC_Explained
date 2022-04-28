from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request,'index.html')


def blog(request):
    blog = Blog.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(blog, 9)
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