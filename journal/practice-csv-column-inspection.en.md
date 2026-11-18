# Earlier practice — Loops and CSV column inspection

[한국어](practice-csv-column-inspection.ko.md) · [Code](../lessons/practice/practice-csv-column-inspection.en.py) · [Notion](https://app.notion.com/p/41c058a09a5b81d48a0ef9c4d35ac4e4)

## 01. Goal

Calculate pass completion in a loop, then open a CSV with pandas and inspect its columns.

---

## 02. Concepts

head() shows five rows by default. Iterate over columns to print their names individually.

---

## 03. Practice code and review examples

```python
completed_passes = [54, 24, 12]
print(completed_passes)
for passes in completed_passes:
    accuracy_passes = passes / 60 * 100
    print(accuracy_passes)
    if accuracy_passes >= 80:
        print("우수")
    elif accuracy_passes >= 60:
        print("보통")
    else:
        print("개선 필요")
```

```python
numbers = [10, 20, 30]
for number in numbers:
    doubled = number * 2
    print(doubled)
```

```python
import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])
print(df.head())
print(df.columns)
for column in df.columns:
    print(column)
```

---

## 04. Output

The learner reported 90.0, 40.0 and 20.0 for the pass exercise. The CSV preview repeated one player and showed fields such as player_name, season_name and team. Pass a CSV path when running the published script.

---

## 05. Corrections

Dividing the full list by 60 raises TypeError. Divide the single value obtained from the loop. A loop also needs an indented body.

---

## 06. Interpretation

A print inside the loop runs each time. Inspect season, team and competition fields to understand what each row represents.

---

## 07. Next practice

Read a CSV and compare the first row with the list of column names.
