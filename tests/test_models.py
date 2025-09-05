from django.test import TestCase
from .models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Ice Cream", price= 80, inventory= 50)
        self.assertEqual(str(item), "IceCream: 80")