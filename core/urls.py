
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
   path('', views.index_page, name='index'),
   path('about/', views.about_page, name='about_page'),
   path('course_page/', views.course_page, name='course_page'),
   path('testimonial/', views.xstudents_page, name='xstudents'),

   path('contact/', views.contact, name='contact_page'), 

   

   
   
]
