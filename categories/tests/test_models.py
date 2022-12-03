from categories.models import Categories

from django.test import TestCase

###################################################################
class CategoriesModelTest(TestCase):
    @classmethod
    
    def setUpTestData(cls):
        cls.categories = {
          "name": "Name Test",
    }
        
        cls.category = Categories.objects.create(**cls.categories)
    
    def test_name_max_length(self):
        max_length = self.category._meta.get_field("name").max_length
        self.assertEqual(max_length, 125)
        
    def test_fields(self):
        self.assertEqual(self.category.name, self.categories["name"])
        
######################################################################