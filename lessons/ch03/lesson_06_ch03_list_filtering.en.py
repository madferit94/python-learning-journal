# Lesson 06 — Chapter 3 lists and conditions

# 1. Print qualifying order amounts
price = 40  # Set the unit price to 40.
quantities = [3, 5, 0, 8, 4]  # Store the order quantities in a list.

for quantity in quantities:  # Read one quantity at a time.
    if quantity >= 5:  # Check whether the current quantity is at least 5.
        amount = price * quantity  # Multiply the unit price by the current quantity.
        print(amount)  # Print each qualifying amount.

# 2. Collect amounts in a list
price = 40  # Set the unit price to 40.
quantities = [3, 5, 0, 8, 4]  # Store the order quantities in a list.

amounts = []  # Create an empty list for the amounts.

for quantity in quantities:  # Read one quantity at a time.
    if quantity >= 5:  # Check whether the current quantity is at least 5.
        amount = price * quantity  # Multiply the unit price by the current quantity.
        amounts.append(amount)  # Append the calculated amount.

print(amounts)  # Print the list once after the loop.

# 3. Sum the collected amounts
print(sum(amounts))  # Sum the amounts and print the total.

# Output shared by the learner
# 200
# 320
# [200, 320]
# 520

# Intermediate errors and fixes
# for quantity in quantities >= 5: raised TypeError because it compared the whole list with an integer. The fix tests each quantity inside the loop.
#
# if quantity >= 5 raised SyntaxError. Adding : starts the conditional block.
#
# An intermediate run printed a long repeated list. Multiplying a list by an integer repeats its entries. Using price * quantity calculates a single order amount.
#
# An intermediate run printed []. The final code initializes the list before the loop, appends each qualifying amount, and prints after the loop.
#
# sum(amounts = []) raised TypeError. The fix passes the populated list as the first argument in sum(amounts).
