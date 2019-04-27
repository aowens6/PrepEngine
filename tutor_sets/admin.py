from django.contrib import admin
from .models import TutorSet, Question, Option, Attempt

admin.site.register(TutorSet)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Attempt)
