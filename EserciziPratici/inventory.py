import pandas as pd

# Load inventory data from CSV
inventory_df = pd.read_csv("inventory.csv")

# Set the 'product_name' column as the index
inventory_df.set_index("product_name", inplace=True)

# Convert the DataFrame directly to a dictionary, selecting only the 'stock_level' column
inventory_dict = inventory_df["stock_level"].to_dict()

# Print the inventory
print("Initial Inventory:")
print(inventory_dict)


# Add "Puppy Snacks" to the inventory
inventory_dict["Puppy Snacks"] = 40

# Update "Cheesy Chompers" in the inventory and assign it the value of 20
inventory_dict["Cheesy Chompers"] = 20

print("\nUpdated Inventory:")
print(inventory_dict)


# We've discontinued "Peanut Butter Biscuits". Remove it from the inventory

# Remove item
del inventory_dict["Peanut Butter Biscuits"]

print("\nUpdated Inventory after Discontinuation:")
print(inventory_dict)


print("\nInventory Report:")
for product, stock in inventory_dict.items():
    print(f"Product: {product}, Stock: {stock}")
