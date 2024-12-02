class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if quantity <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name not in self.items:
            raise KeyError("Item não encontrado no inventário.")
        if quantity > self.items[item_name]:
            raise ValueError("Quantidade insuficiente no inventário.")
        self.items[item_name] -= quantity
        if self.items[item_name] == 0:
            del self.items[item_name]

    def get_item_quantity(self, item_name):
        return self.items.get(item_name, 0)

    def transfer_item(self, target_inventory, item_name, quantity):
        self.remove_item(item_name, quantity)
        target_inventory.add_item(item_name, quantity)
