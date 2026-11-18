# Lesson 03 — Convert strings and calculate an amount
# Goal: Convert price and quantity before multiplying them.
# Purpose: Values that look like numbers can be stored as strings.
# The final practice in section 4 runs when you open the script with Python.

# 1. Review integer conversion
# price_text = "25"  # Store the price as a string.
# quantity_text = "4"  # Store the quantity as a string.
# print(type(price_text))  # Print the original price type.
# print(type(quantity_text))  # Print the original quantity type.
# price = int(price_text)  # Convert the price to an integer and save it in price.
# quantity = int(quantity_text)  # Convert the quantity to an integer and save it in quantity.
# print(price)  # Print the converted price.
# print(quantity)  # Print the converted quantity.
# print(type(price))  # Print the converted price type.
# print(type(quantity))  # Print the converted quantity type.
# Reported: str, str, 25, 4, int, int.

# 2. Calculate the total
# amount = price * quantity  # Multiply the integer price by the quantity and store the total.
# print(amount)  # Print the total.
# Prediction and reported output: 100.

# 3. Compare the original and converted values
# print(type(price_text))  # Print the original price type.
# print(type(price))  # Print the converted price type.
# Reported: str, int.
# Explanation: int(price_text) returns integer 25, which the assignment stores in price on the left of =. The original price_text still holds the string "25" because it was never reassigned.
# The learner clarified after feedback that the original type remains unchanged.

# 4. Repeat with different values
# The first run printed 18 and 3. After a prompt, the learner added multiplication.
# The prediction field was blank. Both final runs printed a total of 54.
price_text = "18"  # Store the price as a string.
quantity_text = "3"  # Store the quantity as a string.
print(type(price_text))  # Print the original price type.
print(type(quantity_text))  # Print the original quantity type.
price = int(price_text)  # Convert the price to an integer and save it in price.
quantity = int(quantity_text)  # Convert the quantity to an integer and save it in quantity.
print(price)  # Print the converted price.
print(quantity)  # Print the converted quantity.
print(type(price))  # Print the converted price type.
print(type(quantity))  # Print the converted quantity type.
amount = price * quantity  # Multiply the integer price by the quantity and store the total.
print(amount)  # Print the total.
