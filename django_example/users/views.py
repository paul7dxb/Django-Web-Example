from django.shortcuts import render, redirect
from .forms import UserRegisterForm # Form for User creation Extended form from forms.py
from django.contrib import messages #Flash messages library

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #Check form is valid
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            #Redirect user to home page after successful account create
            return redirect('blog-home')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', { 'form' : form })