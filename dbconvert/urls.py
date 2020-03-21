from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home.as_view()),
    path('1', home1),
    ]