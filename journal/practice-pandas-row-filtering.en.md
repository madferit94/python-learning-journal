# Earlier practice — pandas column selection and goal filtering

> Reference material compiled from older files. Learner authorship is unconfirmed.

[한국어](practice-pandas-row-filtering.ko.md) · [Code](../lessons/practice/practice-pandas-row-filtering.en.py) · [Notion](https://app.notion.com/p/41c058a09a5b8182b671d1d94b9f4bfa)

## 01. Goal

Read a football CSV, inspect player names and goals, and filter for at least 10 or 20 goals.

---

## 02. Concepts

A column comparison produces a Boolean mask. Applying the mask selects rows, and head() previews the first five.

---

## 03. Practice code and review examples

```python
import sys
import pandas as pd
df = pd.read_csv(sys.argv[1])
print(df.head())
print(df['player_name'])
print(df['player_name'].head())
print(df['goals'].head())
goals_10_plus = df[df['goals'] >= 10]
print(goals_10_plus.head())
goals_20_plus = df[df['goals'] >= 20]
print(goals_20_plus.head())
print(df[df['goals'] >= 20].head())
```

---

## 04. Output

The learner reported goals of 22, 39, 29, 21 and 26 in the 20-goal preview. The published script was checked with a sample CSV and takes a CSV path as an argument.

---

## 05. Corrections

Use a read_csv() call, spell player_name correctly and use actual column names to prevent KeyError.

---

## 06. Interpretation

The first five selected rows follow input order. Check the row grain before combining seasons or competitions.

---

## 07. Next practice

Try a different threshold and inspect the matching rows.
