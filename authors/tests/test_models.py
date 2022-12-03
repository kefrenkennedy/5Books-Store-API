from django.test import TestCase

from authors.models import Author


# Create your tests here.
class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author_data = {
            "name": "John Green"
        }

        cls.author = Author.objects.create(**cls.author_data)
    
    def test_name_max_length(self):

        max_length = self.author._meta.get_field('name').max_length

        self.assertEqual(max_length, 127)
        
    def test_name_unique(self):
        unique = self.author._meta.get_field('name').unique

        self.assertTrue(unique)

