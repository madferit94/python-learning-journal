# Lesson 10 — NumPy array basics
# The coach added inline comments to the learner’s code. Learner-reported outputs and the coach’s
# comparison example are labeled separately. To run problem 0, uncomment the block and set your CSV
# path.
# Multiplying a list by an integer repeats the whole list. NumPy’s `np.array()` turns a list into an
# array. Multiplying that array by an integer applies the multiplication to each value. Read `.shape`
# without parentheses because it is an attribute.

# Problem 0 — Review counting CSV lines
# with open("f1_2026_results.csv", encoding="utf-8") as file:  # Open the CSV and close it after the
# with block.
#     first_line = file.readline()  # Read the header so the count excludes it.
#     count = 0  # Start at zero.
#     for line in file:  # Read one data line at a time.
#         count = count + 1  # Add one for each line read.
#     print(count)  # Print the total once after the loop.

# 418
# Running from the home directory with only the filename caused `FileNotFoundError`. The learner
# supplied the full CSV path locally and got `418`. Because `print(count)` is aligned with `for`, it
# runs once after the loop. To run problem 0 from the published code, set the path to your own copy of
# the CSV.

# Problem 1 — Multiplying lists and arrays
import numpy as np  # Import NumPy as np.
demo = np.array([4, 7])  # Build the array from the lesson example.
print(demo * 3)  # Multiply each example value by three.

quantities = np.array([2, 5, 8])  # Put the three exercise values in an array.
print(quantities * 2)  # Multiply each array value by two and display the result.

# [12 21]
# [ 4 10 16]
# `np.quantities` looked for a NumPy attribute named `quantities` and raised `AttributeError`.
# `quantities` is the learner’s variable name. The learner created the array with `np.array()` and
# then printed the doubled values. The coach verified the list output below for comparison.

# print([2, 5, 8] * 2)  # Coach’s comparison: the whole list repeats twice.
# [2, 5, 8, 2, 5, 8]

# Problem 2 — Inspecting array shape
import numpy as np  # Import NumPy for this exercise.
shape_01 = np.array([6, 7.5, 8, 0, 1])  # Make a one-dimensional array with five values.
shape_02 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])  # Make an array with two rows of four values.
print(shape_01.shape)  # Check the number of values along the only axis.
print(shape_02.shape)  # Check the number of rows and columns.

# (5,)
# (2, 4)
# `shape.01` raised `SyntaxError` because a dot cannot appear inside that variable name. It was
# changed to `shape_01`. The typo `np.arrat` raised `AttributeError` and was corrected to `np.array`.
# `data.shape_01` raised `NameError` because `data` was undefined. The learner fixed it by putting
# `.shape` after the actual array name.
# `(5,)` means one dimension with five values. The trailing comma marks a tuple with one item. `(2,
# 4)` means two rows and four columns. For uneven input such as `[[1, 2, 3, 4], [5, 6, 7]]`,
# `np.array()` raises `ValueError` before any shape can be printed. The coach checked this with NumPy
# 1.26.4.

# Lesson 11 covers array indexing and slicing in Chapter 4, Section 4.1. Select one value by position,
# select a range of values, then select a row and an individual cell from a two-dimensional array.
