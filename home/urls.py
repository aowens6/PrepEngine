from django.urls import path
from .views import TutorSetListView, UserTutorSetListView, UserAttemptsListView

urlpatterns = [
    path('', TutorSetListView.as_view(), name='engine-home'),
    path('userTutorSets/<str:username>', UserTutorSetListView.as_view(), name='user-tutorsets'),
    path('userAttempts/<str:username>', UserAttemptsListView.as_view(), name='user-attempts'),
]