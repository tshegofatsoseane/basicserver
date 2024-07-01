from django.urls import path
from .views import greet_visitor

urlpatterns = [
    path('api/hello', greet_visitor),
]
