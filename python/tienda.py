#Inventory

# Dictionary to keep the inventory
inventory = {}

# Function to get a number from the user
def get_number(message, number_type=float):
    while True:
        user_input = input(message)
        try:
            value = number_type(user_input)
            if value < 0:
                print("Please type a positive number.")
            else:
                return value
        except ValueError:
            print("That is not a valid number. Try again.")

# Add a product to the inventory
def add_product(name, price, quantity):
    if name in inventory:
        print(f"The product '{name}' is already in the inventory. Use update.")
    else:
        inventory[name] = (price, quantity)
        print(f"Product '{name}' added.")

# Search for a product
def search_product(name):
    if name in inventory:
        price, quantity = inventory[name]
        print(f"Product: {name}\nPrice: ${price:.2f}\nQuantity: {quantity}")
    else:
        print(f"The product '{name}' is not in the inventory.")

# Update the price of a product
def update_price(name, new_price):
    if name in inventory:
        _, quantity = inventory[name]
        inventory[name] = (new_price, quantity)
        print(f"The price of '{name}' is now ${new_price:.2f}.")
    else:
        print(f"The product '{name}' is not found.")

# Delete a product from the inventory
def delete_product(name):
    if name in inventory:
        del inventory[name]
        print(f"Product '{name}' was deleted.")
    else:
        print(f"The product '{name}' is not in the inventory.")

# Calculate the total value of the inventory
def calculate_total_value():
    total = sum(price * quantity for price, quantity in inventory.values())
    print(f"\nTotal inventory value: ${total:.2f}\n")

# Menu to use the program
def menu():
    while True:
        print("\n--- INVENTORY MENU ---")
        print("1. Add product")
        print("2. Search product")
        print("3. Update price")
        print("4. Delete product")
        print("5. Show total value")
        print("6. Show all products")
        print("0. Exit")

        option = input("Choose an option: ")

        if option == "1":
            name = input("Product name: ").strip()
            price = get_number("Product price: $")
            quantity = get_number("Product quantity: ", int)
            add_product(name, price, quantity)
        elif option == "2":
            name = input("Product name to search: ").strip()
            search_product(name)
        elif option == "3":
            name = input("Product name to update: ").strip()
            new_price = get_number("New price: $")
            update_price(name, new_price)
        elif option == "4":
            name = input("Product name to delete: ").strip()
            delete_product(name)
        elif option == "5":
            calculate_total_value()
        elif option == "6":
            if inventory:
                print("\n--- All Products ---")
                for product, (price, quantity) in inventory.items():
                    print(f"{product} - ${price:.2f} - {quantity} units")
            else:
                print("The inventory is empty.")
        elif option == "0":
            print("Goodbye!")
            break
        else:
            print("Wrong option. Try again.")

# Run the program
if __name__ == "__main__":
    menu()