from django.urls import path
from .views import (tutorset_overview,
                    tutorset_delete,
                    tutorset_create,
                    tutorset_edit,
                    tutorset_start,
                    question_create,
                    question_edit,
                    question_delete,
                    finish_quiz
                    )

urlpatterns = [
    path('createSet/', tutorset_create, name='tutorSet-create'),
    path('editSet/<int:pk>', tutorset_edit, name='tutorSet-edit'),
    path('deleteSet/<int:tutorset_pk>', tutorset_delete, name='tutorSet-delete'),
    path('tutorSet/<int:tutorset_pk>/', tutorset_overview, name='tutorSet-detail'),
    path('tutorSetStart/<int:tutorset_pk>/', tutorset_start, name='tutorSet-start'),
    path('addQuestion/<int:tutorset_pk>/', question_create, name='add-question'),
    path('editQuestion/<int:tutorset_pk>/<int:question_pk>/',
         question_edit, name='edit-question'),
    path('deleteQuestion/<int:question_pk>/', question_delete, name='question-delete'),
    path('finishQuiz/<int:tutorset_pk>/', finish_quiz, name='finish-quiz'),
]