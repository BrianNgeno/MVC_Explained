from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import BlogCreateView

urlpatterns = [
    # path('', views.index, name='landing'), 
    path('',views.blog,name='blog'),
    path('blog/<slug:slug>_<int:pk>',views.singleblog,name='singleblog'),
    path('blog/delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('blog/upload', BlogCreateView.as_view(), name='upload_blog'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)