from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_csv, name="display_csv"),
    path('', views.interface, name="interface"),
    path('login', views.my_login, name="login"),
    path('bias', views.bias, name="bias"),
]
