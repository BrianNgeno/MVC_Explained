from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landing'), 
    path('blog/',views.blog,name='blog'),
    path('blog/<slug:slug>_<int:pk>',views.singleblog,name='singleblog'),
]