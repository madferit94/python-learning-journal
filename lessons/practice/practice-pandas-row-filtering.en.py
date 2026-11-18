# CSV column selection and row filtering
# Pass a CSV path as the first script argument. The CSV needs player_name and goals.
# Use head() for a preview. Select player_name or goals to inspect one column.
# Compare goals against a threshold to make a Boolean mask. Use df[mask] to select rows.
# A preview of selected rows follows the input order. Sorting is a separate step.
# Call read_csv() with parentheses, quote column names and check their spelling.

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
