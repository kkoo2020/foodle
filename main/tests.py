from django.test import TestCase

from .models import Store


class StoreTest(TestCase):
    def test_str_representation(self):
        store = Store(name="Subway", address="some address")
        self.assertEqual("Subway", str(store))
        self.assertEqual("<Store: Subway>", repr(store))
