from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from trip.views import mainmytrip

urlpatterns = [
    url('all_trip', mainmytrip) #первая вьюха
]
