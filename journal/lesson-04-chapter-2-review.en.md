# Lesson 04 — Chapter 2 review

[한국어](lesson-04-chapter-2-review.ko.md) · [Code](../lessons/ch02/lesson_04_ch02_review.en.py) · [Notion](https://app.notion.com/p/41c058a09a5b81dfa0edd4a3263234d3)

## 01. Goal

Convert strings for calculation, validate one input, and repeat a calculation for several quantities.

---

## 02. Concepts

`int()` converts a string to an integer. `if` and `else` select a branch. `for` takes one item from the list each time.

---

## 03. Learner code

### 1. Conversion and multiplication

```python
price_text = "35"  # Store the price as a string.
quantity_text = "6"  # Store the quantity as a string.

price_number = int(price_text)  # Convert the price string to an integer.
quantity_number = int(quantity_text)  # Convert the quantity string to an integer.

print(price_number)  # Print the converted price.
print(quantity_number)  # Print the converted quantity.

amount = price_number * quantity_number  # Multiply the integer price and quantity and store the total.
print(amount)  # Print the total.
```

### 2. Conditionals

```python
price = 35  # Set the price to 35.
quantity = 0  # Check the case where the quantity is zero.

if quantity <= 0:  # Check whether the quantity is zero or less.
    print("수량 확인 필요")  # Print a message if the condition is true.
else:  # Run the lines below for a positive quantity.
    amount = price * quantity  # Multiply the price and quantity and store the total.
    print(amount)  # Print the total.
```

### 3. Loops

```python
price = 35  # Use the same price, 35, for every calculation.
quantities = [2, 5, 8]  # Collect the quantities in a list.

for quantity in quantities:  # Take one quantity from the list at a time.
    amount = price * quantity  # Multiply the current quantity by the price.
    print(amount)  # Print one total per iteration.
```

Change quantity from 0 to 3 to check the else branch (105). The warning is kept in Korean, exactly as written by the learner.

---

## 04. Reported output

- Conversion and multiplication: `35`, `6`, `210`.
- Conditionals: quantity `3` printed `105`; quantity `0` printed `수량 확인 필요`.
- Loop: `70`, `175`, `280` on separate lines.

---

## 05. Corrections

The first exercise initially printed the converted values. The learner added the total after a prompt. In the second exercise, the learner switched the condition from price to quantity and put the warning under `if` and multiplication under `else`. The first loop attempt multiplied a list by an integer. The learner then multiplied one quantity at a time. The saved file had `print(amount)` indented inside the loop, while the pasted snippet showed it outside.

---

## 06. Learner explanation

The price stays at 35. The loop takes 2, 5, and 8 from quantities in order and assigns each value to quantity. Calculating and printing inside the loop gives one line per total: 70, 175, and 280.

The learner finished the exercises with hints. A later independent rewrite has yet to be checked.

---

## 07. Next review

- [ ] Predict the outputs for a new list, then write and run the loop without the example.
