from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.index, name='landing'), 
    path('',views.blog,name='blog'),
    path('blog/<slug:slug>_<int:pk>',views.singleblog,name='singleblog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)