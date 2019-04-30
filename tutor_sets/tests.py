from django.test import TestCase
from .models import TutorSet
from django.contrib.auth.models import User
from django.utils import timezone


class CreateTutorSet(TestCase):

    def create_tutor_set(self):
        User.objects.create_user(username='default',email=None,password=None)
        return TutorSet.objects.create(
            title="Test Set from test.py",
            description='Description for test.py Tutor Set',
            author=User.objects.first(),
            date_created=timezone.now(),
            date_updated=timezone.now()
            )

    def test_tutor_set_creation(self):
        tutorSet = self.create_tutor_set()
        self.assertTrue(isinstance(tutorSet, TutorSet))
        self.assertEqual(tutorSet.__str__(), tutorSet.title)