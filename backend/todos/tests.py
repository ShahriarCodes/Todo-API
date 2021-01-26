from django.test import TestCase

from .models import Todo

# Create your tests here


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="first todo", body="a body here")
