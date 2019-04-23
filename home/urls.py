from django.urls import path
from . import views
from .views import TutorSetListView, TutorSetDetailView

urlpatterns = [
    path('', TutorSetListView.as_view(), name='engine-home'),
    path('tutorSet/<int:pk>/', TutorSetDetailView.as_view(), name='tutorSet-detail'),
]