from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"home.html")

def customer_page(request):
    return render(request,"customer_page.html")

def courier_page(request):
    return render(request,"courier_page.html")