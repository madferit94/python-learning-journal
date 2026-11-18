# Lesson 05 — Chapter 3 list basics
# Practice indexing, appending, and looping over a list.

# 1. Access a value by position
quantities = [2, 5, 8]  # Store the three quantities in a list.
print(quantities[1])  # Print the second value, at index 1.

# 2. Append a value
quantities.append(3)  # Append quantity 3 to the end of the list.
print(quantities)  # Print the list after appending the new value.

# 3. Calculate totals in a loop
price = 35  # Set the price used for every quantity.
for quantity in quantities:  # Take one quantity from the list at a time.
    amount = price * quantity  # Multiply the current quantity by the price.
    print(amount)  # Print the total for this quantity.

# Verified output from the organized script
# 5
# [2, 5, 8, 3]
# 70
# 175
# 280
# 105
