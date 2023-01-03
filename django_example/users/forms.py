from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#Create new class that inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        #model to be affected
        model = User
        # Fields to display in form in order
        fields = ['username', 'email', 'password1', 'password2']