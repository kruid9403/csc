class ItemToPurchase():
    def __init__(self, item_name = "none", item_price = 0.0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        return self.item_price * self.item_quantity

one = ItemToPurchase("Chocolate Chips", 3.0, 1)
two = ItemToPurchase("Bottled Water", 1.0, 10)

print("TOTAL COST")
print(one.item_name + " " + str(one.item_quantity) + " @ $" + str(one.item_price) + " = $" + str(one.print_item_cost()))
print(two.item_name + " " + str(two.item_quantity) + " @ $" + str(two.item_price) + " = $" + str(two.print_item_cost()))
print("\nTotal: $" + str(one.print_item_cost() + two.print_item_cost()))