from django.urls import path
from . import views
from .views import tutorset_overview, tutorset_start, TutorSetDetailView, tutorset_delete, tutorset_create, tutorset_edit, question_create, question_edit, question_delete

urlpatterns = [
    path('createSet/', tutorset_create, name='tutorSet-create'),
    path('editSet/<int:pk>', tutorset_edit, name='tutorSet-edit'),
    path('deleteSet/<int:tutorset_pk>', tutorset_delete, name='tutorSet-delete'),
    path('tutorSet/<int:tutorset_pk>/', tutorset_overview, name='tutorSet-detail'),
    path('tutorSetStart/<int:tutorset_pk>/', tutorset_start, name='tutorSet-start'),
    path('addQuestion/<int:tutorset_pk>/', question_create, name='add-question'),
    path('editQuestion/<int:tutorset_pk>/<int:question_pk>/', question_edit, name='edit-question'),
    path('deleteQuestion/<int:question_pk>/', question_delete, name='question-delete'),
]