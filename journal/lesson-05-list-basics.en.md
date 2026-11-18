# Lesson 05 — Chapter 3 list basics

[한국어](lesson-05-list-basics.ko.md) · [Lesson code](../lessons/ch03/lesson_05_ch03_lists.en.py) · [Notion](https://app.notion.com/p/41c058a09a5b81e599f1dc252c3ee924)

## 01. Goal

Use a list to store quantities, add another value, and apply the same calculation to every entry.

---

## 02. Concepts

List positions start at `0`. `append()` adds a value at the end. `for` visits the values in order.

---

## 03. Learner code

Run the three blocks in order. Each block uses the same list.

### 1. Access a value by position

```python
quantities = [2, 5, 8]  # Store the three quantities in a list.
print(quantities[1])  # Print the second value, at index 1.
```

### 2. Append a value

```python
quantities.append(3)  # Append quantity 3 to the end of the list.
print(quantities)  # Print the list after appending the new value.
```

### 3. Calculate totals in a loop

```python
price = 35  # Set the price used for every quantity.
for quantity in quantities:  # Take one quantity from the list at a time.
    amount = price * quantity  # Multiply the current quantity by the price.
    print(amount)  # Print the total for this quantity.
```

---

## 04. Output

The learner shared the output below for exercises 2 and 3. The first print statement was commented out in that run. In the saved script the index lookup runs immediately after the list is created. Running the organized script confirmed that it prints `5` as the first line.

```text
[2, 5, 8, 3]
70
175
280
105
```

---

## 05. Run order

The saved code places `print(quantities[1])` immediately after creating the list and before calling `append(3)`.

---

## 06. What happens in the loop

After appending `3`, the loop processes `2`, `5`, `8`, and `3`. The price stays at `35`, and the current quantity changes on each iteration.

---

## 07. Next practice

Filter quantities greater than or equal to `5` with `if` inside `for`, then calculate a total for each selected quantity.
