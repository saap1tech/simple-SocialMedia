from django.urls import path

from .views import *

urlpatterns = [
    path('', home),
    path('direct/<str:rec>/', index),
    path('send/', send),
    path('show/', show),
]