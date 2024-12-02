import pytest

from s206_seminar.src.inventory_app.inventory import Inventory


class TestInventoryUnit:

    def setup_method(self, _):
        self.inv = Inventory()

    def teardown_method(self):
        self.inv.items = {}

    def test_add_item(self):
        self.inv.add_item("Life Potion", 10)
        assert self.inv.items == {"Life Potion": 10}

    def test_add_item_already_exists(self):
        self.inv.add_item("Life Potion", 10)
        self.inv.add_item("Life Potion", 5)
        assert self.inv.items == {"Life Potion": 15}

    def test_add_item_invalid_quantity(self):
        with pytest.raises(ValueError) as excinfo:
            self.inv.add_item("Life Potion", 0)
        assert str(excinfo.value) == "The quantity must be greater than zero."

    def test_remove_item(self):
        self.inv.add_item("Life Potion", 10)
        self.inv.remove_item("Life Potion", 5)
        assert self.inv.items == {"Life Potion": 5}

    def test_remove_item_not_found(self):
        with pytest.raises(KeyError) as excinfo:
            self.inv.remove_item("Life Potion", 5)
        assert excinfo.value.args[0] == "Item not found in the inventory."

    def test_remove_item_invalid_quantity(self):
        self.inv.add_item("Life Potion", 10)
        with pytest.raises(ValueError) as excinfo:
            self.inv.remove_item("Life Potion", 15)
        assert str(excinfo.value) == "The quantity to remove is greater than the current quantity."

    def test_remove_item_zero_quantity(self):
        self.inv.add_item("Life Potion", 10)
        self.inv.remove_item("Life Potion", 10)
        assert self.inv.items == {}

    def test_get_item_quantity(self):
        self.inv.add_item("Life Potion", 10)
        assert self.inv.get_item_quantity("Life Potion") == 10

    def test_get_item_quantity_not_found(self):
        assert self.inv.get_item_quantity("Life Potion") == 0

    def test_transfer_item(self):
        inv2 = Inventory()
        self.inv.add_item("Life Potion", 10)
        self.inv.transfer_item(inv2, "Life Potion", 5)
        assert self.inv.items == {"Life Potion": 5}
        assert inv2.items == {"Life Potion": 5}

    def test_transfer_item_not_found(self):
        inv2 = Inventory()
        with pytest.raises(KeyError) as excinfo:
            self.inv.transfer_item(inv2, "Life Potion", 5)
        assert excinfo.value.args[0] == "Item not found in the inventory."

    def test_transfer_item_invalid_quantity(self):
        inv2 = Inventory()
        self.inv.add_item("Life Potion", 10)
        with pytest.raises(ValueError) as excinfo:
            self.inv.transfer_item(inv2, "Life Potion", 15)
        assert str(excinfo.value) == "The quantity to remove is greater than the current quantity."

    def test_consume_item(self):
        self.inv.add_item("Life Potion", 10)
        self.inv.consume_item("Life Potion")
        assert self.inv.items == {"Life Potion": 9}

    def test_consume_item_zero_quantity(self):
        self.inv.add_item("Life Potion", 1)
        self.inv.consume_item("Life Potion")
        assert self.inv.items == {}

    def test_consume_item_not_found(self):
        with pytest.raises(KeyError) as excinfo:
            self.inv.consume_item("Life Potion")
        assert excinfo.value.args[0] == "Item not found in the inventory."
