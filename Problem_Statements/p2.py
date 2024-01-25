# Function to add a product
def add_product(product_id, product_name, quantity, price):
    product = {
        'Product ID': product_id,
        'Product Name': product_name,
        'Quantity': quantity,
        'Price': price
    }
    online_store.append(product)

# Function to display all products
def display_products():
    if len(online_store) == 0:
        print("No products in the catalog.")
    else:
        print("Product Catalog:")
        for product in online_store:
            print(f"Product ID: {product['Product ID']} Product Name: {product['Product Name']} Quantity: {product['Quantity']} Price: ${product['Price']}")

# Function to update the quantity of a product
def update_product_quantity(product_id, new_quantity):
    for product in online_store:
        if product['Product ID'] == product_id:
            product['Quantity'] = new_quantity
            break

# Function to search for a product by ID
def search_product_by_id(product_id):
    for product in online_store:
        if product['Product ID'] == product_id:
            print(f"Product found: Product ID: {product['Product ID']} Product Name: {product['Product Name']} Quantity: {product['Quantity']} Price: ${product['Price']}")
            break
    else:
        print("Product not found.")

# Function to calculate the total cost of all products
def calculate_total_cost():
    total_cost = sum(product['Quantity'] * product['Price'] for product in online_store)
    print(f"Total Cost of Products: ${total_cost}")

# Function to remove a product by ID
def remove_product_by_id(product_id):
    global online_store
    online_store = [product for product in online_store if product['Product ID'] != product_id]

# Main program loop
online_store = []
while True:
    print("\n1. Add Product")
    print("2. Display Product Catalog")
    print("3. Update Product Quantity")
    print("4. Search Product by ID")
    print("5. Calculate Total Cost")
    print("6. Remove Product by ID")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        product_id = input("Enter Product ID: ")
        product_name = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        add_product(product_id, product_name, quantity, price)
    elif choice == 2:
        display_products()
    elif choice == 3:
        product_id = input("Enter Product ID to Update Quantity: ")
        new_quantity = int(input("Enter New Quantity: "))
        update_product_quantity(product_id, new_quantity)
    elif choice == 4:
        product_id = input("Enter Product ID to Search: ")
        search_product_by_id(product_id)
    elif choice == 5:
        calculate_total_cost()
    elif choice == 6:
        product_id = input("Enter Product ID to Remove: ")
        remove_product_by_id(product_id)
    elif choice == 7:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid choice.")