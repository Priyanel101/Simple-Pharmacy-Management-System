inventory = {"paracetamol": 213, "biogesic": 523, "dentol": 23}
medicine_info = {
    "paracetamol": "Paracetamol (Panadol, Calpol, Alvedon) is an analgesic and antipyretic drug that is used to temporarily relieve mild-to-moderate pain and fever",
    "biogesic": "A trusted brand of paracetamol, Paracetamol (Biogesic) is a medication that is typically used to relieve mild to moderate pain such as headache.",
    "dentol": "Better than both of these, it's called magic beans in Sri Lanka."
}

def pharmacy_menu():
    """
    Displays the pharmacy menu and handles user input.
    Returns:
        bool: True if the user wants to continue, False if the user wants to quit.
    """
    print("Good day pharmacy staff member!!\n")
    print("╔════════════════════════╗")
    print("║       Pharmacy         ║")
    print("║          ✚             ║")
    print("║                        ║")
    print("║ 1. Continue            ║")
    print("║ 2. Quit                ║")
    print("╚════════════════════════╝")
    menu = input("\nEnter your choice: ")

    if menu == "1":
        print("\nHere is the menu:")
        return True
  
    elif menu == "2":
        print("Goodbye!")
        return False

    else:
        print("Invalid input. Please try again.")
        return pharmacy_menu()

def view_inventory():
    """
    Displays the current inventory.
    """
    print("\nInventory")
    for medicine, quantity in inventory.items():
        print(f"{medicine}: {quantity}")

def update_inventory():
    """
    Allows the user to add or deduct items from the inventory.
    """
    print("\nUpdate Inventory:")
    print("Available Medicines:", ", ".join(inventory.keys()))
    medicine = input("Enter the medicine name: ").lower()
    if medicine in inventory:
        action = input("Do you want to add or deduct? ").lower()
        if action == "add":
            quantity = int(input("Enter the quantity to add: "))
            inventory[medicine] += quantity
            print(f"{quantity} units of {medicine} added to inventory.")
        elif action == "deduct":
            quantity = int(input("Enter the quantity to deduct: "))
            if quantity <= inventory[medicine]:
                inventory[medicine] -= quantity
                print(f"{quantity} units of {medicine} deducted from inventory.")
            else:
                print("Insufficient stock!")
        else:
            print("Invalid action.")
    else:
        print("Medicine not found!")

def pharmacy_choices():
    """
    Displays the pharmacy choices menu and handles user input.
    """
    while True:
        print("\n1. View Inventory")
        print("2. View Medicine Information")
        print("3. Update Inventory")
        print("4. Quit")

        menu_choice = input("Enter your choice: ")

        if menu_choice == "1":
            view_inventory()
        elif menu_choice == "2":
            print("\nMedicine Information:")
            for medicine, info in medicine_info.items():
                print(f"{medicine}: {info}")
        elif menu_choice == "3":
            update_inventory()
        elif menu_choice == "4":
            print("Goodbye!")
            return
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    if not pharmacy_menu():
        exit()
    pharmacy_choices()
