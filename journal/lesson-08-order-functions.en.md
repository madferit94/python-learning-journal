# Lesson 08 — Calculate order amounts with functions

[한국어](lesson-08-order-functions.ko.md) · [Lesson code](../lessons/ch03/lesson_08_ch03_functions.en.py) · [Notion](https://app.notion.com/p/41e058a09a5b8170abcaf26f2e822818)

- **`def` defines the calculation.** When `order_amount(orders)` receives order A, the function calculates `40 × 3`.
- **`return` sends the answer back to the caller.** The assignment `amounts = order_amount(order)` makes the answer available to `append()`. `print()` displays a value on screen.
- **`if problem == 4:` was an exercise selector added by the coach.** `problem = 4` assigns the number; `== 4` compares it. In the submitted exercise only `print(problem)` was indented under the selector. The finished version omits those control lines and presents each exercise as an independently runnable block.

## Exercise 1 — Read the unit price and append it once

Read the unit price from order A and add it once.

```python
orders = {"name": "A", "price":40, "quantity": 3}  # Store order A.
print(orders["price"])  # Print the unit price looked up by key.
selected_order = []  # Create an empty list for the price.
selected_order.append(orders["price"])  # Append one unit price.
print(selected_order)  # Print the list with the price.
```

```text
40
[40]
```

Looping over the dictionary visited three keys and appended `40` three times. Removing the loop made append run once. Printing the list on the next line shows its new contents.

---

## Exercise 2 — Calculate one order with a function

Multiply order A’s unit price and quantity inside a function.

```python
orders = {"name": "A", "price":40, "quantity": 3}  # Store order A.
def order_amount(order_amount):  # Define a function that receives one order.
    return order_amount["price"] * order_amount["quantity"]  # Return the unit price times the quantity.
print(order_amount(orders))  # Pass the order in and print the returned amount.
```

```text
120
```

`def` begins a function definition, so it cannot appear on the right of an assignment. Call the function after it has been defined. A print after return inside the function would never run. The submitted code uses the same spelling for the function name and its parameter. Before the parentheses it names the function; inside them it names the incoming order.

---

## Exercise 3 — Reuse the function for multiple orders

Pass each order to the function, then print the amount list and total.

```python
def order_amount(order_amount):  # Define a function that receives one order.
    return order_amount["price"] * order_amount["quantity"]  # Return the unit price times the quantity.
orders = [{"name":"A" ,"price":40, "quantity":3},  # Store three orders in a list.
         {"name":"B", "price":25, "quantity":8},  # Store one order.
         {"name":"C", "price":30, "quantity":2}]  # Store one order.
selected_amounts = []  # Create an empty list for the order amounts.
for order in orders:  # Take one order at a time.
    amounts = order_amount(order)  # Store the amount returned by the function.
    selected_amounts.append(amounts)  # Append the current amount.
print(selected_amounts)  # Print the amount list after the loop.
print(sum(selected_amounts))  # Print the sum of all collected amounts.
```

```text
[120, 200, 60]
380
```

Calling the function while its definition was commented out raised NameError. Define it in this exercise before the loop calls it. Repeating keys in a single dictionary keeps the last value, so each order gets its own dictionary inside the list.

---

## Exercise 4 — Change order C and compare results

Change C’s quantity from 2 to 5 and check the list and total.

```python
orders = [{"name":"A", "price":40, "quantity":3},  # Store three orders in a list.
          {"name":"B", "price":25, "quantity":8},  # Store one order.
          {"name":"C", "price":30, "quantity":5}]  # Store one order.
selected_amounts = []  # Create an empty list for the order amounts.
def order_amount(order):  # Define a function that receives one order.
    return order["price"] * order["quantity"]  # Return the unit price times the quantity.
for order in orders:  # Take one order at a time.
    amounts = order_amount(order)  # Store the amount returned by the function.
    selected_amounts.append(amounts)  # Append the current amount.
print(selected_amounts)  # Print the amount list after the loop.
print(sum(selected_amounts))  # Print the sum of all collected amounts.
```

```text
[120, 200, 150]
470
```

`["quantity"]` is a one-item list, so multiplying it by 30 repeated the text. Looking up `order["quantity"]` retrieved the number 5. Moving the list print after the loop produces one final list; the C-only check was removed from the finished code. C rose from 60 to 150, increasing the total from 380 to 470 by 90.
