from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, "core/home.html")

@login_required
def products(request):
    return render(request, "core/products.html")

