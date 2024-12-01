from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart

def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option:\n")
        
        if choice == 'a':
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(name, price, quantity)
            cart.add_item(item)
        elif choice == 'r':
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)
        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            item = ItemToPurchase(name, item_quantity=quantity)
            cart.modify_item(item)
        elif choice == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}\n")
    
    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)

if __name__ == "__main__":
    main()
