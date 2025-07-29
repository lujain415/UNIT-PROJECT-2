from django.urls import path
from . import views

app_name = "pets"

urlpatterns = [
    path("new/", views.pet_create, name="pet_create"),
    path("detail/<int:pet_id>/", views.pet_detail, name="pet_detail"),
    path("update/<int:pet_id>/", views.pet_update, name="pet_update"),
    path("delete/<int:pet_id>/", views.pet_delete, name="pet_delete"),
    path("all/", views.pet_list, name="pet_list"),
    path("search/", views.pet_search, name="pet_search"),
    path("adopt/<int:pet_id>/", views.adoption_request_view, name="adoption_request"),
    path("thank-you/", views.thank_you_view, name="thank_you"),
    path("adoption-requests/", views.adoption_requests_list, name="adoption_requests_list"),
    path("requests/delete/<int:request_id>/", views.delete_adoption_request, name="delete_adoption_request"),
    path("adoption/accept/<int:request_id>/", views.accept_adoption_request, name="accept_request"),
]
