from  django.urls import path
from . import views

app_name = "main"
urlpatterns = [
      
      
      path('', views.home, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/messages/', views.contact_messages_view, name='contact_messages'),
    path('contact/success/', views.contact_success_view, name='contact_success'),
]