from django.urls import path, include
from .views import *


urlpatterns = [
    path("", HomeView, name="home"),
    path("calculate/", CalculateView, name="calculate"),
]
