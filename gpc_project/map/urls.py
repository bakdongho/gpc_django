from django.urls import path
from .views import MapMain, MapSearch

urlpatterns = [

    path('', MapMain.as_view(), name='mapMain'),
    path('search', MapSearch, name='mapSearch'),
]