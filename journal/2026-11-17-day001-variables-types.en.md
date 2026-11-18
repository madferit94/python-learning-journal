# Day 001 — Variables, values, types and function calls

[한국어](2026-11-17-day001-variables-types.ko.md)

> 📘 **Session summary** · Status: session finished
> Scope: third edition, Chapter 2

## 🎯 01. Goal and scope

Distinguish variable names, stored values, types and function calls. The learner's paper edition, pages read and actual study duration are unverified; companion examples follow the third edition.

---

## 📖 02. Textbook example

The short example assigns `5`, then `"foo"`, to `a`. We wrapped `type(a)` in `print()` so results appear when running a Python file. The learner predicted `int`, then `str`, and the final value `foo`; the shared output matched.

---

## ✍️ 03. Learner's final code

The exercise requested integer → string. The learner wrote the reverse order; the code and its output are valid.

```python
value = "7"
print(type(value))

value = 7
print(type(value))

print(value)
print("value")
```

Before execution, the learner predicted the final two outputs: the stored value `7`, then the literal text `value`.

---

## 🖥️ 04. Learner-reported output

```text
<class 'str'>
<class 'int'>
7
value
```

Predictions matched. The agent separately ran the organized code and confirmed the same output. Learner execution and agent verification are separate evidence.

---

## 🛠️ 05. Initial attempts and corrections

An early output showed only `7`, which cannot distinguish an integer from a string. The coach explained `type()` and provided the hint `print(type(value))`. Separate outputs showing only `str` or only `int` were followed by a complete file containing both assignments and outputs. No exception message was shared in this session; none was invented for this record.

---

## 🧠 06. Understanding and assistance

- Predicted the last value of a variable and checked it.
- Checked string and integer types through code.
- Explained variable output versus literal text output.
- Used textbook examples, AI explanations and a `print(type(value))` hint.

---

## 🔁 07. Next recall

- [ ] Assign integer 12 to `item` and print its type.
- [ ] Reassign string `"12"` to the same name and print its type.
- [ ] Explain `print(item)` versus `print("item")` before running them.
