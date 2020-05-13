from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    """
    Here we define and run the test against our Product Models
    """

    def test_str_(self):
        test_name = Product(name='Product 1')
        self.assertEqual(str(test_name), 'Product 1')