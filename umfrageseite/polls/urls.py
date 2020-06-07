from django.urls import path
from .views import index, umfrage_detail, vote, results, myFunction


urlpatterns = [
    # anfrage an / , dann übergebe dies der fkt index
    path('', index, name = 'index'),
    path('abstimmung/<str:slug>/', umfrage_detail, name = 'umfrage-detail'),
    path('abstimmung/<str:slug>/vote/', vote, name = 'vote'),
    path('abstimmung/<str:slug>/results/', results, name = 'results'),
    path('', index, name = 'ttt'),
    path('search/', myFunction, name = 'search'),
]
