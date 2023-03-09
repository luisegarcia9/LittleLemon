from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        item1 = Menu.objects.create(title = "icecream", price = 90, inventory = 20)
        item2 = Menu.objects.create(title = "postre", price = 10, inventory = 30)
        
    def test_getall(self):
        items = Menu.objects.all()
        data = MenuSerializer(items,many = True)
        c = Client()
        response = c.get('/restaurant/menu/menu/')
        self.assertEqual(data,response.content)
          
        