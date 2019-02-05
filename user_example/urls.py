from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro', views.register, name='registro'),
    path('blog', views.blog, name='blog'),
    path('error', views.blog, name='error'),
    path('blog2', views.blog2, name='blog2'),
    #path('error2', views.blog2, name='error2'),
]
