from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'listings/listings.html')

def listings(request, listing_id):
    return render(request, 'listings/listings.html')

def search(request):
    return render(request,'pages/search.html')
