from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import SignupForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            messages.success(request, 'A user is added. Please login with provided credentials.')

            return redirect('/')
        
    else:
        form = SignupForm()
    
    return render(request, 'myauth/signup_form.html', {
        'form': form,
        'title': 'Signup'
    })

