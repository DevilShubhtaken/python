# Function to add a medicine to the store inventory
def add_medicine(medicine_id, medicine_name, quantity, price):
    global medicine_store
    medicine = {"Medicine ID": medicine_id, "Medicine Name": medicine_name, "Quantity": quantity, "Price": price}
    medicine_store.append(medicine)

# Function to display all medicines in the store inventory
def display_medicines():
    print("\nMedicine Inventory:")
    for medicine in medicine_store:
        print(f"Medicine ID: {medicine['Medicine ID']} Medicine Name: {medicine['Medicine Name']} Quantity: {medicine['Quantity']} Price: ${medicine['Price']}")

# Function to update the quantity of a specific medicine in the inventory
def update_medicine_quantity(medicine_id, new_quantity):
    global medicine_store
    for medicine in medicine_store:
        if medicine['Medicine ID'] == medicine_id:
            medicine['Quantity'] = new_quantity
            print("Medicine quantity updated successfully.")
            break

# Function to search for a medicine based on its ID
def search_medicine_by_id(medicine_id):
    global medicine_store
    for medicine in medicine_store:
        if medicine['Medicine ID'] == medicine_id:
            print(f"Medicine Details: Medicine ID: {medicine['Medicine ID']} Medicine Name: {medicine['Medicine Name']} Quantity: {medicine['Quantity']} Price: ${medicine['Price']}")
            break

# Main program loop
medicine_store = []
while True:
    print("\n1. Add Medicine")
    print("2. Display Medicine Inventory")
    print("3. Update Medicine Quantity")
    print("4. Search Medicine by ID")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        medicine_id = input("Enter Medicine ID: ")
        medicine_name = input("Enter Medicine Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        add_medicine(medicine_id, medicine_name, quantity, price)
    elif choice == 2:
        display_medicines()
    elif choice == 3:
        medicine_id = input("Enter Medicine ID to Update Quantity: ")
        new_quantity = int(input("Enter the new Quantity: "))
        update_medicine_quantity(medicine_id, new_quantity)
    elif choice == 4:
        medicine_id = input("Enter Medicine ID to Search: ")
        search_medicine_by_id(medicine_id)
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid choice.")