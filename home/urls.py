from django.urls import path
from .views import TutorSetListView

urlpatterns = [
    path('', TutorSetListView.as_view(), name='engine-home'),
]