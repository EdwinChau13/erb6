from django.urls import path
from . import views
app_name="listings"
urlpatterns = [
    path('', views.index, name='index'),  # Endpoint empty will direct to index page
    path('<int:listing_id>', views.listing, name='listing'), # endpoint, function, reverse lookup
    path('search', views.search, name='search'), # endpoint, function, reverse lookup
]