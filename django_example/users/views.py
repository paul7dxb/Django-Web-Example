from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm # Form for User creation Extended form from forms.py
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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,  instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile') #POST GET redirect pattern, forces GET request instead of post
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)