from django.shortcuts import render, redirect
from .forms import UserRegisterForm # Form for User creation Extended form from forms.py
from django.contrib import messages #Flash messages library
from django.contrib.auth.decorators import login_required # Decorator to restrict access to pages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #Check form is valid
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can now login!')
            #Redirect user to home page after successful account create
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', { 'form' : form })

@login_required
def profile(request):
    return render(request, 'users/profile.html')