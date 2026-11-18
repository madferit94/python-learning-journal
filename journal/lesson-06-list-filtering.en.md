# Lesson 06 — Chapter 3 lists and conditions

[한국어](lesson-06-list-filtering.ko.md) · [Lesson code](../lessons/ch03/lesson_06_ch03_list_filtering.en.py) · [Notion](https://app.notion.com/p/41c058a09a5b81588b11e6038c474fae)

## 01. Goal

Filter orders by quantity, collect their amounts, and calculate the sum.

---

## 02. Concepts

`for` reads one quantity at a time. `if` checks the minimum, `append()` collects the amounts, and `sum()` adds them.

---

## 03. Learner code

Run the three blocks in order. Exercise 3 uses the list built in exercise 2.

### 1. Print qualifying order amounts

```python
price = 40  # Set the unit price to 40.
quantities = [3, 5, 0, 8, 4]  # Store the order quantities in a list.

for quantity in quantities:  # Read one quantity at a time.
    if quantity >= 5:  # Check whether the current quantity is at least 5.
        amount = price * quantity  # Multiply the unit price by the current quantity.
        print(amount)  # Print each qualifying amount.
```

### 2. Collect amounts in a list

```python
price = 40  # Set the unit price to 40.
quantities = [3, 5, 0, 8, 4]  # Store the order quantities in a list.

amounts = []  # Create an empty list for the amounts.

for quantity in quantities:  # Read one quantity at a time.
    if quantity >= 5:  # Check whether the current quantity is at least 5.
        amount = price * quantity  # Multiply the unit price by the current quantity.
        amounts.append(amount)  # Append the calculated amount.

print(amounts)  # Print the list once after the loop.
```

### 3. Sum the collected amounts

```python
print(sum(amounts))  # Sum the amounts and print the total.
```

---

## 04. Reported output

Only quantities `5` and `8` qualify. The learner shared the output below, and the organized script reproduced it.

```text
200
320
[200, 320]
520
```

---

## 05. Intermediate errors and fixes

- `for quantity in quantities >= 5:` raised `TypeError` because it compared the whole list with an integer. The fix tests each `quantity` inside the loop.
- `if quantity >= 5` raised `SyntaxError`. Adding `:` starts the conditional block.
- An intermediate run printed a long repeated list. Multiplying a list by an integer repeats its entries. Using `price * quantity` calculates a single order amount.
- An intermediate run printed `[]`. The final code initializes the list before the loop, appends each qualifying amount, and prints after the loop.
- `sum(amounts = [])` raised `TypeError`. The fix passes the populated list as the first argument in `sum(amounts)`.

---

## 06. Inside and outside the loop

Append inside the condition. Print the completed list and calculate its sum after the loop.

---

## 07. Next practice

Change the minimum to `6` and predict the list and total before running the script.
