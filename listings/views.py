from django.shortcuts import render
from listings.models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 3)  # Show 3 listings per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'listings': paged_listings}
    return render(request,'listings/listings.html', context)

def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    context = {'listing': listing}
    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request,'pages/search.html')
