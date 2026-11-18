# Lesson 04 — Chapter 2 review
# Run this file to see all three exercises in order.

# 1. Conversion and multiplication
price_text = "35"  # Store the price as a string.
quantity_text = "6"  # Store the quantity as a string.

price_number = int(price_text)  # Convert the price string to an integer.
quantity_number = int(quantity_text)  # Convert the quantity string to an integer.

print(price_number)  # Print the converted price.
print(quantity_number)  # Print the converted quantity.

amount = price_number * quantity_number  # Multiply the integer price and quantity and store the total.
print(amount)  # Print the total.

# Reported output
# 35
# 6
# 210


# 2. Conditionals
price = 35  # Set the price to 35.
quantity = 0  # Check the case where the quantity is zero.

if quantity <= 0:  # Check whether the quantity is zero or less.
    print("수량 확인 필요")  # Print a message if the condition is true.
else:  # Run the lines below for a positive quantity.
    amount = price * quantity  # Multiply the price and quantity and store the total.
    print(amount)  # Print the total.

# Reported output
# 수량 확인 필요
# Quantity 3 was checked separately and printed 105.


# 3. Loops
price = 35  # Use the same price, 35, for every calculation.
quantities = [2, 5, 8]  # Collect the quantities in a list.

for quantity in quantities:  # Take one quantity from the list at a time.
    amount = price * quantity  # Multiply the current quantity by the price.
    print(amount)  # Print one total per iteration.

# Reported output
# 70
# 175
# 280

# Learner explanation, edited for clarity
# The price stays at 35.
# The loop takes 2, 5, and 8 from quantities in order and assigns each value to quantity.
# Calculating and printing inside the loop gives one line per total: 70, 175, and 280.
