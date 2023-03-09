from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title = "icecream", price = 90, inventory = 20)
        menuitem= Menu(title = "icecream", price = 90)
        self.assertEqual(item, menuitem)