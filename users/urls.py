from django.urls import path
from .views import creator_profile, CreatorTutorSetListView

urlpatterns = [
    path('creatorProfile/<creator_pk>', CreatorTutorSetListView.as_view(), name='creator-profile'),
]