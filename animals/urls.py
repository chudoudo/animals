from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<animal_type>/', views.get_list_of_the_animal, name = 'animal-name'),
]
