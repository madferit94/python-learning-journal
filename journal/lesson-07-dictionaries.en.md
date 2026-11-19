# Lesson 07 — Analyze orders with dictionaries

[한국어](lesson-07-dictionaries.ko.md) · [Lesson code](../lessons/ch03/lesson_07_ch03_dictionaries.en.py) · [Notion](https://app.notion.com/p/41d058a09a5b819190bee70d32a9e9ca)

- **Dictionary braces `{}`** store key–value pairs. `order["price"]` retrieves `40` using the key `"price"`.
- **Brackets `[]`** create a list. After a variable, use a position such as `orders[0]` for a list or a key such as `order["price"]` for a dictionary.
- **Parentheses `()`** hold the values passed to a call such as `append()`, `sum()` or `print()`.
- **`append()` and `sum()`** do different jobs. Append adds one amount to the existing list. Sum takes the full list and returns one number. In `print(sum(...))`, the inner call runs first.

## Exercise 1 — Create one order and read its values

Look up order A’s name, unit price and quantity.

```python
order = {"name": "A", "price": 40,"quantity":3}  # Store one order as key–value pairs.
print(order["name"])  # Print the looked-up value and any additional argument on one line.
print(order["price"])  # Print the looked-up value and any additional argument on one line.
print(order["quantity"])  # Print the looked-up value and any additional argument on one line.
```

```text
A
40
3
```

Read a value using its key, as in `order["name"]`.

---

## Exercise 2 — Recalculate after changing the quantity

Compare the amounts before and after changing quantity from 3 to 5.

```python
order = {"name": "A", "price": 40, "quantity": 3}  # Store one order as key–value pairs.
amounts = order["price"] * order["quantity"]  # Multiply the current unit price and quantity.
print(amounts)  # Print the current amount.
order["quantity"] = 5  # Set the quantity to 5.
amounts = order["price"] * order["quantity"]  # Multiply the current unit price and quantity.
print(amounts)  # Print the current amount.
```

```text
120
200
```

The first attempt looped over lists of strings and tried multiplying the lists. The corrected code reads numbers from the dictionary. Updating first produced only `200`, so the learner put a calculation and print on each side of the update.

---

## Exercise 3 — Print three orders stored in a list

Print the name and amount of each order on one line.

```python
orders = [{"name": "A", "price":40, "quantity":5},  # Store the order dictionaries in a list.
          {"name": "B", "price":25, "quantity":8},  # Store one order in the list.
          {"name": "C", "price":30, "quantity":2}]  # Store one order in the list.
for order in orders:  # Take one order at a time.
    amounts = order["price"] * order["quantity"]  # Multiply the current unit price and quantity.
    print(order["name"],amounts)  # Print the looked-up value and any additional argument on one line.
```

```text
A 200
B 200
C 60
```

Multiple assignments retained only the final order, and repeated dictionary keys retained the last value. The learner stored three dictionaries in one list, moved the combined print into the loop, and removed the extra amount-only print.

---

## Exercise 4 — Sum only qualifying orders

Collect and sum the amounts for quantities of at least 5.

```python
orders = [{"name": "A", "price":40, "quantity":5},  # Store the order dictionaries in a list.
         {"name": "B", "price":25, "quantity":8},  # Store one order in the list.
         {"name":"C", "price":30, "quantity":2}]  # Store one order in the list.
selected_amounts = []  # Create an empty list for qualifying amounts.
for order in orders:  # Take one order at a time.
    if order["quantity"] >= 5:  # Check the current order quantity.
        amounts = order["price"] *  order["quantity"]  # Multiply the current unit price and quantity.
        selected_amounts.append(amounts)  # Append one amount to the end.
print(selected_amounts)  # Print the completed list once after the loop.
print(sum(selected_amounts))  # Sum the list first, then print the total.
```

```text
[200, 200]
400
```

Printing alone left the list empty. The learner appended inside the condition and printed the list and total after the loop. The organized script omits the redundant standalone `sum(selected_amounts)` expression.

---

## Exercise 5 — Verify the result when C reaches 5

Change only C’s quantity from 2 to 5 and check the total again.

```python
orders = [{"name":"A", "price":40, "quantity":5},  # Store the order dictionaries in a list.
          {"name":"B", "price":25, "quantity":8},  # Store one order in the list.
          {"name":"C", "price":30, "quantity":5}]  # Store one order in the list.
selected_amounts = []  # Create an empty list for qualifying amounts.
for order in orders:  # Take one order at a time.
    if order["quantity"] >= 5:  # Check the current order quantity.
        amounts = order["price"] * order["quantity"]  # Multiply the current unit price and quantity.
        selected_amounts.append(amounts)  # Append one amount to the end.
print(selected_amounts)  # Print the completed list once after the loop.
print(sum(selected_amounts))  # Sum the list first, then print the total.
```

```text
[200, 200, 150]
550
```

C now meets `>= 5`. Its amount, `30 × 5 = 150`, raises the total from `400` to `550`.
