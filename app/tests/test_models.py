from django.test import TestCase
from ..models import Item
import decimal

class ItemTestCase(TestCase):

    def setUp(self):
        Item.objects.create(title='Bread', price=45.50)
        Item.objects.create(title='Winstone', price=205.50)
    
    def test_title_islower(self):
        bread = Item.objects.get(title='Bread')
        self.assertTrue(bread.title.capitalize())

    def test_price_isdecimal(self):
        winstone = Item.objects.get(title='Winstone')
        print(type(winstone.price))
        self.assertEqual(True, isinstance(winstone.price, decimal.Decimal))
        
