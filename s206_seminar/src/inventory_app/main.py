from s206_seminar.src.inventory_app.inventory import Inventory

if __name__ == "__main__":
    inv1 = Inventory()
    inv2 = Inventory()

    inv1.add_item("Life Potion", 10)
    inv1.add_item("Rune Stone", 5)

    inv1.transfer_item(inv2, "Life Potion", 3)

    print("Inventory 1:", inv1.items)
    print("Inventory 2:", inv2.items)
