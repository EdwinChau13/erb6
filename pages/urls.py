from django.urls import path
from . import views
app_name="pages"
urlpatterns = [
    path('', views.index, name='index'),  # is localhost:8000/
    path('about', views.about, name='about') # Endpoint, function name, reverse lookup
]