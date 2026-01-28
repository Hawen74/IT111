# START
import os
import json

# ASK user to enter product ID
# ASK user to enter quantity
productID = input("Enter a product ID: ")
quantity = int(input("Enter a quantity: "))

# SET found to false
# SET product name to empty
# SET price to 0
found = False
productName = ""
price = 0

# OPEN products file
# SKIP header row
base_dir = os.path.dirname(__file__)
file_path1 = os.path.join(base_dir, "products.csv")

f = open(file_path1, "r")
f.readline()

# FOR each line in products file
#     SPLIT line into parts
for line in f:
  parts = line.strip().split(',')
#     IF product ID matches
#         SAVE product name
#         SAVE price
#         SET found to true
# END FOR
  if productID == parts[0]:
    productName = parts[1]
    price = float(parts[2])
    found = True

# CLOSE products file
f.close()

# OPEN tax file
# READ tax rate
# CLOSE tax file
file_path2 = os.path.join(base_dir, "tax.json")

f = open(file_path2, "r")
tax_rate = float(json.load(f)["tax_rate"])

f.close()

# IF product was found
#     CALCULATE subtotal (price × quantity)
#     CALCULATE tax (subtotal × tax rate)
#     CALCULATE total (subtotal + tax)
if found:
  subtotal = price * quantity
  tax = subtotal * tax_rate
  total = subtotal + tax

#     DISPLAY order summary
#     DISPLAY product name, price, quantity
#     DISPLAY subtotal, tax, and total
# ELSE
#     DISPLAY "Product not found" error message
  print("Order summary: ")
  print("Product name: ", productName)
  print("Price: ", price)
  print("Quantity: ", quantity)
  print("Subtotal: ", subtotal)
  print("Tax: ", tax)
  print("Total: ", subtotal)
else:
  print("Product not found!")
# END
