class ShoppingCart:
    def __init__(self):
        self.items = {}  # Dictionary to store items and their quantities

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] -= quantity
            if self.items[item_name]['quantity'] <= 0:
                del self.items[item_name]
        else:
            print(f"{item_name} is not in the cart.")

    def calculate_total(self):
        total_price = sum(item['price'] * item['quantity'] for item in self.items.values())
        return total_price

    def display_cart(self):
        print("Items in your cart:")
        for item_name, item_info in self.items.items():
            print(f"{item_name} ({item_info['quantity']}x) - ${item_info['price']} each")

if __name__ == "__main__":
    cart = ShoppingCart()

    while True:
        print("\nOptions:")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Calculate total")
        print("5. Quit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            item_name = input("Enter the name of the item: ")
            price = float(input("Enter the price of the item: "))
            quantity = int(input("Enter the quantity: "))
            cart.add_item(item_name, price, quantity)
            print(f"{quantity} {item_name}(s) added to your cart.")

        elif choice == '2':
            item_name = input("Enter the name of the item to remove: ")
            quantity = int(input("Enter the quantity to remove: "))
            cart.remove_item(item_name, quantity)
            print(f"{quantity} {item_name}(s) removed from your cart.")

        elif choice == '3':
            cart.display_cart()

        elif choice == '4':
            total_price = cart.calculate_total()
            print(f"Total price in your cart: ${total_price:.2f}")

        elif choice == '5':
            print("Thank you for shopping with us! Have a great day!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")