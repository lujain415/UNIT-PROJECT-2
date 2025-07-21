from  django.urls import path
from . import views

app_name = "main"
urlpatterns = [
      path('search/', views.entry_search, name='entry_search'),
]