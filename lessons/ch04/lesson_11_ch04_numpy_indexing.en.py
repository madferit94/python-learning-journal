# Lesson 11 — Selecting values from NumPy arrays
# The learner’s code and reported output are grouped by problem. The coach added the inline comments and restored the print line for problem 1 from the conversation.
# A row is one horizontal line. A column is the set of cells in the same position from top to bottom. In `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, the second row is `4, 5, 6` and the second column is `2, 5, 8`. Position numbers start at zero.

import numpy as np  # Import NumPy as np.

# Problem 0 — Array shape and brackets
shape_01 = np.array([[1, 2, 4, 5], [6, 7, 8, 9]])  # Create an array with two rows of four values.
shape_02 = np.array([[1, 2, 3, 4,], [5, 6, 7, 8]])  # Use different values with the same number of rows and columns.
print(shape_01.shape)  # Print the number of rows and columns.
print(shape_02.shape)  # Check the shape of the second array.

# (2, 4)
# (2, 4)
# The initial input `[2, 4]` had two values along one axis, so its shape was `(2,)`. Closing the outer brackets after the first row passed the two row groups as separate arguments. Keeping both rows inside one pair of outer brackets passes one nested list and produces `(2, 4)`. The trailing comma after `4` adds no cell.

# Problem 1 — Select one value by position
numbers = np.array([6, 7, 8, 9])  # Create an array from the four exercise values.
print(numbers[2])  # Print the third value, at position 2.

# 8
# The learner first selected `3` at position `2` from the Python list `[1, 2, 3, 5]`. The index was already correct. After seeing the coach’s example, the learner used the exercise values in a NumPy array and obtained `8`.

# Problem 2 — Select consecutive values
numbers = np.array([6, 7, 8, 9])  # Prepare the array for this exercise.
print(numbers[1:4])  # Print values from position 1 up to position 4.

# [7 8 9]
# The stop index marks the boundary where slicing stops. `1:4` selects positions `1`, `2`, and `3`. When the bounds are within the array, this rule makes the number selected equal to stop minus start, or `4 − 1 = 3` here. The learner described it as starting at the first index and going up to just before the stop.

# Problem 3 — Select a row and one cell
table = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Put three rows into one array.
print(table[1])  # Print the whole second row.
print(table[2, 1])  # Select the third row and print its second value from the left.

# [4 5 6]
# 8
# The `2` before the comma selects the third row from the top, `[7, 8, 9]`. The `1` after the comma selects the second cell from the left, which is `8`.

# Lesson 12 covers Boolean indexing in Chapter 4, Section 4.1. Build a condition with `>=` and select only the values where it is `True`.
