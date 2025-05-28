from django.urls import path
from . import views
app_name="pages"
urlpatterns = [
    path('', views.index, name='index'),  # Endpoint empty will direct to index page
    path('about', views.about, name='about') # endpoint, function, reverse lookup
]