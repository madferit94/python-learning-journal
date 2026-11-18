# 한국어: https://github.com/madferit94/python-learning-journal/blob/main/lessons/ch02/lesson_02_strings_integers_conversion.py
# Lesson 02 — Strings, integers and type conversion
# Status: session finished with guidance.
# Book connection: Python for Data Analysis, third edition, Chapter 2 Python basics.
# Paper edition, pages read and actual study duration are unverified.
# Coach-created exercises based on the concepts, not verbatim textbook exercises.
# AI organized the explanations; learner statements and assistance are identified below.
# Only the final conversion code in section 03 is active.
# Earlier completed exercises are kept as comments so their outputs do not mix.

# ============================================================
# 01. Goals
# ============================================================
# Distinguish value output and type output.
# Compare integer addition with string concatenation.
# Store int() conversion results in new variables and use those variables in arithmetic.
# Identify where the original strings and converted integers remain.

# ============================================================
# 02. Concepts and purpose
# ============================================================
# = assigns the right-hand value to the left-hand name.
# print() displays a value. type() returns its type.
# print(type(...)) checks the type first, then displays it.
# int() converts a supported value to an integer.
# + adds integers, but joins strings when both operands are strings.
# "12" is a string even though it looks numeric; 12 is an integer.
# Assigning int(first_text) to first_number does not reassign first_text.

# ============================================================
# 03. Learner code, separated by exercise
# ============================================================
# [A] Recall: the coach prompted the learner to add the type output.
# The following combines two separately reported runs for review.
# item = 12  # Store integer 12 in item.
# print(item)  # Display the value referred to by item.
# print("item")  # Display literal text item, without looking up the variable.
# print(type(item))  # Display the type of the current value.
# item = "12"  # Reassign the string "12" to the same name.
# print(type(item))  # Display the type of the current value.
# Learner explanation: the quoted value is a string.

# [B] Learner-written and executed comparison.
# first = 12  # Store integer 12 in first.
# second = 3  # Store integer 3 in second.
# total = first + second  # Add the integers and store 15 in total.
# print(total)  # Display the sum, 15.
# first_text = "12"  # Store the string "12", not an integer.
# second_text = "3"  # Store the string "3", not an integer.
# joined = first_text + second_text  # Join the strings and store "123".
# print(joined)  # Display the joined text, 123.
# Learner predicted 123 for string joining before execution.
# The written prediction for total was blank; do not claim all outputs were predicted.

# [C] Learner's final conversion code — only this section executes.
first_text = "12"  # Store the string "12", not an integer.
second_text = "3"  # Store the string "3", not an integer.
first_number = int(first_text)  # Convert "12" to integer 12 and store it under a new name.
second_number = int(second_text)  # Convert "3" to integer 3 and store it under a new name.

numeric_total = first_number + second_number  # Add the converted integers and store 15.

print(numeric_total)  # Display the result held in numeric_total.

print(type(first_text))  # Check that the original value is str.
print(type(first_number))  # Check that the converted value is int.
print(type(second_text))  # Check that the second original value is str.
print(type(second_number))  # Check that the second converted value is int.

# ============================================================
# 04. Actual learner-reported output, by run
# ============================================================
# [A] Initially: 12 / item. After type() was added: 12 / item / <class 'int'>.
# A separate string assignment run produced <class 'str'>.
# [B]
# 15
# 123
# [C]
# 15
# <class 'str'>
# <class 'int'>
# <class 'str'>
# <class 'int'>
# Agent verification of this organized file is separate from learner execution.

# ============================================================
# 05. Initial attempt, cause, correction and check
# ============================================================
# The first conversion attempt created both integer variables correctly, but used:
# numeric_total = first_text + second_text  # Using the original strings joins them into "123".
# print(numeric_total)  # Display the result held in numeric_total.
# Actual output: 123. This was valid string joining, not an exception.
# Conversion results were in first_number and second_number; the original names held strings.
# Coach hint: use the variable names holding integers in the calculation.
# Learner correction:
# numeric_total = first_number + second_number  # Add the converted integers and store 15.
# Actual corrected output: 15.
# Intermediate type check:
# print(type(first_number))  # Check that the converted value is int.
# print(type(second_number))  # Check that the second converted value is int.
# int / int was correct but did not compare originals with conversion results.
# The coach supplied the first_text/first_number comparison lines.
# The learner extended the final check to second_text/second_number too.
# No exception message was shared in this session; none is invented here.

# ============================================================
# 06. Understanding and assistance
# ============================================================
# Learner explanation: first they were strings; the second time they were integers.
# Coach clarification: the types of the operands selected for + changed its behavior.
# Checked: joining -> 123, addition -> 15, original str versus converted int outputs.
# Assistance: type() reminder, calculation-variable hint, original/converted comparison code.
# Learner wrote the comparison exercises, corrected the calculation after the hint,
# and extended the type comparison to the second pair.
# Limits: not every prediction was written first.

# ============================================================
# 07. Next recall — unsolved; leave the answer and result blank
# ============================================================
# Hide the example. Assign "25" to price_text and "4" to quantity_text.
# Predict their string concatenation. Convert them into price and quantity integers.
# Calculate price * quantity and store it in amount; * means multiplication.
# Print amount, then the types of price_text and price.
# Explain whether saving a converted value under a new name changes the original.
# Prediction:
# Learner code:


# Actual output:
# Explanation:
# Assistance used:

price_text = 25  # Initial assignment from the follow-up scratch work. This line produces no output.
