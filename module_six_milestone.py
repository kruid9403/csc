class ItemToPurchase:

    def __init__(self, name="", description="", price=0, quantity=0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.description = description

class Customer():
    def __init__(self, customer_name, date):
        self.customer_name = customer_name
        self.date = date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart.")

    def modify_item(self, updated_item):
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == updated_item.item_name:
                if updated_item.description:
                    self.cart_items[i].description = updated_item.description
                if updated_item.item_price > 0:
                    self.cart_items[i].item_price = updated_item.item_price
                if updated_item.item_quantity > 0:
                    self.cart_items[i].item_quantity = updated_item.item_quantity
                return
        print("Item not found in cart.")

    def get_num_items_in_cart(self):
        return sum([item.item_quantity for item in self.cart_items])
    
    def get_cost_of_cart(self):
        return sum([item.item_price * item.item_quantity for item in self.cart_items])
    
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart = {self.date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${round((item.item_price * item.item_quantity), 2)}")
        print(f"Total: ${round(self.get_cost_of_cart(), 2)}")

    def print_descriptions(self):
        print("Item Descriptions")
        for i in self.cart_items:
            print(f"{i.item_name}: {i.description}")

    def print_menu(cart):
        while True:
            print("MENU")
            print("a - Add item to cart")
            print("r - Remove item from cart")
            print("c - Change item quantity")
            print("i - Output items' descriptions")
            print("o - Output shopping cart")
            print("q - Quit")
            
            choice = input("Choose an Option: ").lower()

            if choice == 'q':
                print("Quitting")
                return
            elif choice == 'a':
                name = input("Enter the item name: ")
                description = input("Enter the item description: ")
                price = float(input("Enter the item price: "))
                quantity = int(input("Enter the item quantity: "))
                cart.add_item(ItemToPurchase(name, description, price, quantity))
                print(f"{name} added to cart.")
            elif choice == 'r':
                name = input("Enter the item name: ")
                cart.remove_item(name)
            elif choice == 'c':
                name = input("Enter the item name: ")
                quantity = int(input("Enter the new quantity: "))
                cart.modify_item(ItemToPurchase(name, "", 0, quantity))
            elif choice == 'i':
                cart.print_descriptions()
            elif choice == 'o':
                cart.print_total()
            else:
                print("Invalid input. Please try again.")

def main():
    cart = Customer("Jeremy Kruid", "November 13, 2024")
    cart.print_menu()

if __name__ == "__main__":
    main()