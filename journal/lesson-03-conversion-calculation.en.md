# Lesson 03 — Convert strings and calculate an amount

[한국어](lesson-03-conversion-calculation.ko.md) · [Code](../lessons/ch02/lesson_03_conversion_calculation.en.py) · [Notion](https://app.notion.com/p/41c058a09a5b81b19b1fd52e4ec17553)

## 🎯 01. Goal

Convert a price and quantity stored as strings to integers, then multiply them to obtain the total.

---

## 📖 02. Concepts

`int()` returns the converted integer. `type()` shows the types of the original value and conversion result. `*` multiplies the integer price by the quantity.

---

## ✍️ 03. Learner code

The learner first converted `"25"` and `"4"` and predicted a total of `100`. The final variation used `"18"` and `"3"`.

```python
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
```

---

## 🖥️ 04. Reported output

The learner confirmed `100` for the first total, `str` for the original price, and `int` for the converted price. Two runs of the variation produced the output below.

```text
<class 'str'>
<class 'str'>
18
3
<class 'int'>
<class 'int'>
54
```

---

## 🛠️ 05. Initial attempt and correction

The first variation converted the values and printed `18` and `3`. After a prompt to calculate the total, the learner added multiplication and `print(amount)`. The final total was `54`. The advance prediction field was blank.

---

## 🧠 06. Exercise 3 explanation

The learner initially thought the original variable changed. After feedback clarified the question, the learner said the original type remained unchanged.

`int(price_text)` returns integer `25`, which the assignment stores in `price` on the left of `=`. The original `price_text` still holds the string `"25"` because it was never reassigned.

The learner wrote the conversion code independently. The explanation and completion of the variation received guidance.

---

## 🔁 07. Next review

- [ ] Predict a total for new values, then write the conversion, multiplication, and output in one pass.
- [ ] Check the types of the original string and converted integer.
