from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_csv, name="display_csv"),
    path('', views.interface, name="interface"),
    path('bias', views.bias, name="bias"),
]
