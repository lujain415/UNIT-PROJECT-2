from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('add/', views.article_create, name='article_create'),
    path('edit/<int:article_id>/', views.article_update, name='article_update'),
    path('<int:article_id>/delete/', views.article_delete, name='article_delete'),

]
