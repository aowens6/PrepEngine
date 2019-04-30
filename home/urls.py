from django.urls import path
from .views import TutorSetListView, UserTutorSetListView
urlpatterns = [
    path('', TutorSetListView.as_view(), name='engine-home'),
    path('userTutorSets/<str:username>', UserTutorSetListView.as_view(), name='user-tutorsets'),
]