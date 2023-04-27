from django.shortcuts import render


def index(request): return render(request, 'aggregator/index.html')


def dashboard(request): return render(request, 'aggregator/dashboard.html')


def register(request): return render(request, 'aggregator/register.html')


#def my_login(request): return render(request, 'aggregator/login_page_temporary.html')


def profile_management(request): return render(request, 'aggregator/profile-management.html')