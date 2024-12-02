import pytest

from s206_seminar.src.inventory_app.inventory import Inventory


class TestInventoryIntegration:

    def setup_method(self, _):
        self.inv1 = Inventory()
        self.inv2 = Inventory()

    def teardown_method(self):
        self.inv1.items = {}
        self.inv2.items = {}

    def test_transfer_item_and_consume(self):
        self.inv1.add_item("Life Potion", 10)
        self.inv1.transfer_item(self.inv2, "Life Potion", 3)
        self.inv2.consume_item("Life Potion")
        assert self.inv1.items == {"Life Potion": 7}
        assert self.inv2.items == {"Life Potion": 2}

    def test_transfer_all_item_quantity(self):
        self.inv1.add_item("Life Potion", 10)
        self.inv1.transfer_item(self.inv2, "Life Potion", self.inv1.get_item_quantity("Life Potion"))
        assert self.inv1.items == {}
        assert self.inv2.items == {"Life Potion": 10}

    def test_transfer_half_item_quantity_and_remove_the_rest(self):
        self.inv1.add_item("Life Potion", 10)
        self.inv1.transfer_item(self.inv2, "Life Potion", 5)
        self.inv1.remove_item("Life Potion", 5)
        assert self.inv1.items == {}
        assert self.inv2.items == {"Life Potion": 5}
