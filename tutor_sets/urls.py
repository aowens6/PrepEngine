from django.urls import path
from . import views
from .views import TutorSetDetailView, TutorSetCreateView

urlpatterns = [
    path('createSet/', TutorSetCreateView.as_view(), name='tutorSet-create'),
    path('tutorSet/<int:pk>/', TutorSetDetailView.as_view(), name='tutorSet-detail'),
]