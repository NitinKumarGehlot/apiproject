from django.urls import path
from . import views

urlpatterns = [
    path('countries/', views.CountriesList.as_view()),
    path('countries/<int:country_id>/states', views.StatesList.as_view()),
    path('states/<int:state_id>/cities', views.CitiesList.as_view()),
    path('countries/<int:country_id>/cities', views.CountryCitiesList.as_view()),
]
