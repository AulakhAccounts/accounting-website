from django.urls import path
from . import views
 
urlpatterns = [
 
    path('', views.home, name='home'),
 
    path('about/', views.about, name='about'),
 
    path('services/', views.services, name='services'),
 
    path('contact/', views.contact, name='contact'),
 
    path('success/', views.success, name='success'),
 
    path('apply/itr/', views.itr_request),
 
    path('apply/gst/', views.gst_request),
 
    path('apply/tds/', views.tds_request),
 
    path('apply/bookkeeping/', views.bookkeeping_request),
]