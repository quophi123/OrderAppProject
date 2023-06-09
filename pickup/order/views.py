from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from . import forms

# Create your views here.
def index(request):
    return render(request,"home.html")

@login_required
def customer_page(request):
    return render(request,"customer_page.html")

@login_required
def courier_page(request):
    return render(request,"courier_page.html")

def sign_up(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email'].lower()
            user = form.save(commit=False)
            user.username = email
            user.save()
            
            #Send a welcome emial
              
            
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
    return render(request,'sign-up.html',{
        'form':form
    })