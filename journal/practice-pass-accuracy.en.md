# Earlier practice — Pass completion rates and grades

> Reference material compiled from older files. Learner authorship is unconfirmed.

[한국어](practice-pass-accuracy.ko.md) · [Code](../lessons/practice/practice-pass-accuracy.en.py) · [Notion](https://app.notion.com/p/41c058a09a5b814cbf45ec97705537d0)

## 01. Goal

Calculate and grade pass completion for each value in a list.

---

## 02. Concepts

Use for to iterate and if, elif and else to assign a grade.

---

## 03. Practice code and review examples

```python
completed_passes = [48, 36, 30]
for passes in completed_passes:
    accuracy_passes = passes / 60 * 100
    print(accuracy_passes)
    if accuracy_passes >= 80:
        print('우수')
    elif accuracy_passes >= 60:
        print('보통')
    else:
        print('개선 필요')
```

---

## 04. Output

Fresh script output:

```text
80.0
우수
60.0
보통
50.0
개선 필요
```

---

## 05. Corrections

An empty loop caused IndentationError. Indenting the calculation and print makes both run on each iteration.

---

## 06. Interpretation

The numerators 48, 36 and 30 are each divided by 60. The grade thresholds are exercise rules.

---

## 07. Next practice

Predict how often print runs if moved outside a nonempty loop.
