# Lesson 02 — Strings, integers and type conversion

[한국어](lesson-02-strings-integers-conversion.ko.md) · [코드 / Code](../lessons/ch02/lesson_02_strings_integers_conversion.en.py)
[Notion](https://app.notion.com/p/41b058a09a5b8137895eec92e5ce5a87)

> 📘 Session finished

## 🎯 01. Goal and scope

Review variables, values and types; compare string joining with integer addition; use `int()` results in arithmetic.

The exercises were created by the coach around Chapter 2 of the third edition of *Python for Data Analysis*, not copied as textbook exercises. The learner's paper edition, pages read and actual study time are unverified.

---

## 📖 02. Concepts and purpose

| Syntax | Role | Purpose here |
| --- | --- | --- |
| `=` | Assign a value to a name | Keep originals and converted values separately |
| `print()` | Display a value | Observe actual results |
| `type()` | Inspect a type | Distinguish numeric-looking strings from integers |
| `+` | Add integers or join strings | Explain `15` versus `123` |
| `int()` | Convert a supported value to an integer | Prepare a string value for arithmetic |

`first_number = int(first_text)` assigns the conversion result to a new name. It does not reassign `first_text`, which continues to refer to a string.

---

## ✍️ 03. Prediction and learner code

**Recall:** the learner printed the integer value and literal text, added type output after a coach reminder, then reassigned the string `"12"` and checked `str`. The learner explained that the quoted value is a string.

**Learner's comparison code:**

```python
first = 12
second = 3
total = first + second
print(total)

first_text = "12"
second_text = "3"
joined = first_text + second_text
print(joined)
```

The learner predicted `123` for joining the strings. The written prediction for `total` and some type predictions were blank; do not claim every result was predicted first.

**Final learner code, corrected after guidance:**

```python
first_text = "12"
second_text = "3"
first_number = int(first_text)
second_number = int(second_text)
numeric_total = first_number + second_number
print(numeric_total)
print(type(first_text))
print(type(first_number))
print(type(second_text))
print(type(second_number))
```

---

## 🖥️ 04. Actual output and verification

Learner-reported outputs are separated by run.

| Run | Observed output |
| --- | --- |
| Initial item output | `12`, `item` |
| Integer type check | `<class 'int'>` |
| Separate string reassignment run | `<class 'str'>` |
| Integer addition / string joining | `15`, `123` |

Final conversion output shared by the learner:

```text
15
<class 'str'>
<class 'int'>
<class 'str'>
<class 'int'>
```

The agent separately executed the organized Korean and English code and confirmed these five lines. Agent verification is not learner execution.

---

## 🛠️ 05. Initial attempts and corrections

**5-1. Conversion was correct, but the calculation used original strings**

```python
first_text = "12"
second_text = "3"
first_number = int(first_text)
second_number = int(second_text)
numeric_total = first_text + second_text
print(numeric_total)
```

Actual output: `123`. This was valid string joining, not an exception. The coach prompted the learner to use the variable names holding integers in the calculation.

Learner correction:

```python
numeric_total = first_number + second_number
```

Actual corrected output: `15`.

**5-2. Improve the type comparison**

Initially the learner printed only the two converted types, correctly obtaining `int`, `int`. The coach supplied the two lines comparing `first_text` and `first_number`. The learner extended the check to the second original/converted pair.

No exception message or measured runtime was supplied in this session; none is invented here.

---

## 🧠 06. Understanding and assistance

The learner explained that the first calculation used strings and the second integers. The coach clarified that selecting operands of different types changes the behavior of `+`.

- Checked: joining gives `123`; integer addition gives `15`; originals are `str` and converted values are `int`.
- Learner work: comparison code, correction after the variable-selection hint, extension to the second type pair.
- Assistance: type-output reminder, operand-selection hint, original/converted type-comparison code.
- Unverified: complete advance predictions, a separate explanation of assignment versus conversion.

---

## 🔁 07. Next recall

- [ ] Assign `"25"` to `price_text` and `"4"` to `quantity_text`.
- [ ] Predict their concatenation before execution.
- [ ] Convert them to integers stored in `price` and `quantity`.
- [ ] Store `price * quantity` in `amount` and print it (`*` means multiplication).
- [ ] Print the types of `price_text` and `price`.
- [ ] Explain whether storing a converted value under a new name changes the original.

This is an unsolved recall task. Answers, predictions and results are left blank.
