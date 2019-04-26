from django.urls import path
from . import views
from .views import tutorset_overview,TutorSetDetailView, tutorset_create, tutorset_edit, question_create, question_edit, option_create

urlpatterns = [
    path('createSet/', tutorset_create, name='tutorSet-create'),
    path('editSet/<int:pk>', tutorset_edit, name='tutorSet-edit'),
    path('tutorSet/<int:tutorset_pk>/', tutorset_overview, name='tutorSet-detail'),
    path('addQuestion/<int:tutorset_pk>/', question_create, name='add-question'),
    path('editQuestion/<int:tutorset_pk>/<int:question_pk>/', question_edit, name='edit-question'),
]