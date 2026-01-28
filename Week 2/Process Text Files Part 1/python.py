import os
import json

# ASK user to enter product ID
# ASK user to enter quantity
productID = input("Enter a product ID: ")
quantity = float(input("Enter a quantity: "))

# SET found to false
# SET product name to empty
# SET price to 0
found = False
productName = ""
price = 0

# OPEN products file
base_dir = os.path.dirname(__file__)
file_path1 = os.path.join(base_dir, "products.csv")

f = open(file_path1, "r")
# SKIP header row
f.readline()

"""
FOR each line in products file
    SPLIT line into parts

    IF product ID matches
        SAVE product name
        SAVE price
        SET found to true
END FOR 
"""
for line in f:
    parts = line.strip().split(",")

    if productID == parts[0]:
        productName = parts[1]
        price = float(parts[2])
        found = True
        break

# CLOSE products file
f.close()

# OPEN tax file
file_path2 = os.path.join(base_dir, "tax.json")

f = open(file_path2, "r")

# READ tax rate
tax_rate = float(json.load(f)["tax_rate"])

# CLOSE tax file
f.close()

"""
IF product was found
    CALCULATE subtotal (price × quantity)
    CALCULATE tax (subtotal × tax rate)
    CALCULATE total (subtotal + tax)

    DISPLAY order summary
    DISPLAY product name, price, quantity
    DISPLAY subtotal, tax, and total
ELSE
    DISPLAY "Product not found" error message
"""

if found:
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax

    print("Order Summary")
    print(f"Product Name: {productName}")
    print(f"Price: {price}")
    print(f"quantity: {quantity}")

    print(f"Subtotal: {subtotal}")
    print(f"Tax: {tax_rate}")
    print(f"Total: {total}")
else:
    print("Product ID not found")
# END
