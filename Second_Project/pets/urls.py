from  django.urls import path
from . import views

app_name = "pets"
urlpatterns = [
    path('all/', views.pet_list, name='pet_list'),
    path('<int:pet_id>/detail/', views.pet_detail, name='pet_detail'),
    path('new/', views.pet_create, name='pet_create'),
    path('<int:pet_id>/update/', views.pet_update, name='pet_update'),
    path('<int:pet_id>/delete/', views.pet_delete, name='pet_delete'),
    path('search/', views.pet_search, name='pet_search'),
    path('<int:pet_id>/adopt/', views.adoption_request_view, name='adoption_request'),
    path('adoption-requests/', views.adoption_requests_list, name='adoption_requests_list'),
     path('thank-you/', views.thank_you_view, name='thank_you'),
     path('requests/<int:request_id>/delete/', views.delete_adoption_request, name='delete_adoption_request'),
     path('adoption/<int:request_id>/accept/', views.accept_adoption_request, name='accept_request'),



    
]