from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, district_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date'
    ).filter(is_published=True)[:3]  # Get the latest 3 listings
    context = {'listings': listings,
    'price_choices': price_choices,
    'bedroom_choices': bedroom_choices,
    'district_choices': district_choices}
    return render(request, 'pages/index.html', context)
def about(request):
    realtors_base = Realtor.objects.all()
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {"realtors": realtors,
               "mvp_realtors": mvp_realtors,
               "realtors_base": realtors_base}
    return render(request, 'pages/about.html', context)