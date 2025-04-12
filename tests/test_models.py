from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        # Create a new Menu instance
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        # Compare the string representation with the expected value
        self.assertEqual(str(item), "IceCream : 80")
