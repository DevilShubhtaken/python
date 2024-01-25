# Function to add vehicle entry
def add_vehicle_entry(vehicle_number, vehicle_type, toll_amount):
    vehicle_entry = {'Vehicle Number': vehicle_number, 'Vehicle Type': vehicle_type, 'Toll Amount': toll_amount}
    toll_management_system.append(vehicle_entry)

# Function to display vehicle entries
def display_vehicle_entries():
    if len(toll_management_system) == 0:
        print("No vehicle entries found.")
    else:
        print("Vehicle Entries:")
        for entry in toll_management_system:
            print(f"Vehicle Number: {entry['Vehicle Number']} Vehicle Type: {entry['Vehicle Type']} Toll Amount: ${entry['Toll Amount']}")

# Function to calculate total toll collection
def calculate_total_toll_collection():
    total_toll_collection = sum([entry['Toll Amount'] for entry in toll_management_system])
    print(f"Total Toll Collection: ${total_toll_collection}")

# Function to search vehicle by number
def search_vehicle_by_number(vehicle_number):
    vehicle_entry = [entry for entry in toll_management_system if entry['Vehicle Number'] == vehicle_number]
    if len(vehicle_entry) == 0:
        print("No vehicle entry found.")
    else:
        print("Vehicle Details:")
        print(f"Vehicle Number: {vehicle_entry[0]['Vehicle Number']} Vehicle Type: {vehicle_entry[0]['Vehicle Type']} Toll Amount: ${vehicle_entry[0]['Toll Amount']}")

# Function to perform operations based on user choice
def perform_operation(choice):
    if choice == 1:
        vehicle_number = input("Enter Vehicle Number: ")
        vehicle_type = input("Enter Vehicle Type (Car/Truck/Bus): ")
        toll_amount = float(input("Enter Toll Amount: "))
        add_vehicle_entry(vehicle_number, vehicle_type, toll_amount)
    elif choice == 2:
        display_vehicle_entries()
    elif choice == 3:
        calculate_total_toll_collection()
    elif choice == 4:
        vehicle_number = input("Enter Vehicle Number to Search: ")
        search_vehicle_by_number(vehicle_number)
    elif choice == 5:
        print("Exiting the program.")
    else:
        print("Invalid choice. Please enter a valid choice.")

# Main program loop
toll_management_system = []
while True:
    print("\n1. Add Vehicle Entry")
    print("2. Display Vehicle Entries")
    print("3. Calculate Total Toll Collection")
    print("4. Search Vehicle by Number")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    perform_operation(choice)