from django.urls import path
from portfolio.views import index

urlpatterns = [
    path('home', index, name="index"),
    path('', index, name="index"),
]