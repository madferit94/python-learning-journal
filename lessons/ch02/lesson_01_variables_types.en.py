# 한국어: https://github.com/madferit94/python-learning-journal/blob/main/lessons/ch02/lesson_01_variables_types.py
# Book-based Python lesson 01 — Variables, values, types and function calls
# Session finished.
# Textbook: Wes McKinney, Python for Data Analysis, third edition, Chapter 2.
# The learner's paper edition is unconfirmed.
# Source: https://github.com/wesm/pydata-book/blob/3rd-edition/ch02.ipynb
# Explanation: https://wesmckinney.com/book/python-basics
# See THIRD_PARTY_NOTICES.md for attribution and license.
# AI added print calls, explanations and organization to the short textbook example.
# Only the learner's final code in section 4 is active.

# 1. Goals and scope
# Distinguish a variable name, its current value, and the value's type.
# Use type() to inspect a type and print() to display a value.
# Compare print(value) with print("value").
# Planned workload: about 30 minutes; actual time was not measured.
# CSV, pandas, Series, references and function definitions were outside this session.

# 2. Concepts
# A variable is a name referring to a value; a and value are chosen names.
# = assigns the right-hand value to the left-hand name; == compares equality.
# int means integer; str means string, written with quotes.
# type(value) returns its type. print(value) displays its value.
# print(type(value)) evaluates the inner type() call, then prints that result.
# Parentheses after a function name call it.
# Reassigning a different value is not the same as converting a value's type.

# 3. Textbook example and learner evidence
# The notebook displays type(a); a .py script needs print() to show that result.
# a = 5
# print(type(a))
# a = "foo"
# print(type(a))
# print(a)
# Learner prediction: integer, then string; final value foo because it was assigned last.
# Learner-reported output:
# <class 'int'>
# <class 'str'>
# foo
# Prediction matched. The current value changes; both values are not kept in a.

# 4. Learner's final code — the only active code
# The prompt requested integer -> string; the learner wrote string -> integer.
# The order differs, but the code and corresponding output are valid.
value = "7"
print(type(value))

value = 7
print(type(value))

print(value)
print("value")
# First assignment: string "7", type str.
# Second assignment: integer 7, type int.
# print(value) looks up the current value; print("value") prints literal text.

# 5. Actual learner output and prediction
# <class 'str'>
# <class 'int'>
# 7
# value
# The learner predicted stored 7 and literal value before execution. Output matched.
# Quotes mark a string in source code and are not printed by these print() calls.

# 6. Initial attempts and feedback
# Early output showed only 7, which does not distinguish integer 7 from string "7".
# The coach explained type() and supplied the print(type(value)) hint.
# Later outputs separately showed str or int; they alone did not prove both assignments
# were included in one run. The coach asked for both assignments and outputs together.
# The final code/output confirmed string -> integer in one file.
# No exception message was shared; do not invent TypeError or NameError history.
# This was completed with examples and hints.

# 7. Checked understanding and limits
# Checked: final value foo, string/integer types, variable versus literal output.
# Unverified: exact book pages read, actual study time.
# Assistance: author example, AI explanation, type() hint and a prepared exercise file.
# The learner wrote the final application code and shared output.
# AI organized this review file and separately reran its active code.

# 8. Next recall — leave the answer blank
# Hide the example. Assign integer 12 to item and print its type.
# Reassign string "12" to item and print its type.
# Explain print(item) versus print("item") before execution.
# Learner code:

# Prediction:
# Actual output:
# Examples/hints used:
# Remaining questions:
# Decide the next topic after checking recall.
