from django.urls import path
from . import views  # "." is the current folder

# index or new_prods  function doesnt need to be called

urlpatterns = [
    path('', views.index),
    path('new/', views.new_prods)
]
