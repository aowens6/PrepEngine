from django.urls import path
from . import views

urlpatterns = [
    path('', views.createEngine, name='create-engine'),
]