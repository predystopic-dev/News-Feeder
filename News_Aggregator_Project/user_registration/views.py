from django.shortcuts import render,redirect
from user_registration.forms import RegistrationForm
from django.contrib import messages

# Create your views here.


def my_login(request): return render(request, 'user_registration/my-login.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            users = form.save(commit=False)
            users.set_password(form.cleaned_data['password'])
            users.save()
            messages.success(request, 'Your account has been created successfully')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'user_registration/my-login.html', {'form': form})

