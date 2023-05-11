from django import forms
from user_registration.models import Users

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ('email', 'first_name', 'last_name', 'password')
