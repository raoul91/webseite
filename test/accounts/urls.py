from django.conf.urls import url
from django.urls import path
from . import views
from .views import HomeView, forCyrill, forSilvan

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', HomeView.as_view(), name = 'home'),
    path('forCyrill', forCyrill, name = 'cyrillsPath'),
    path('forSilvan', forSilvan, name = 'silvansPath'),
]
