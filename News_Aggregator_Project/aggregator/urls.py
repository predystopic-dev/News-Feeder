from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=""),
    path('dashboard', views.dashboard, name="dashboard"),
    path('register', views.register, name="register"),
    path('profile-management', views.profile_management, name="profile-management"),
    path('my-login', views.my_login, name="my-login"),

]
