# Lesson 09 — Reading a CSV file

[한국어](./lesson-09-reading-files.ko.md) · [Code](../lessons/ch03/lesson_09_ch03_reading_files.en.py) · [3.3](https://wesmckinney.com/book/python-builtin#files-and-the-operating-system)

The learner wrote the exercise code. The coach added the comments and explanations. The outputs below come from the learner’s runs. Set the file path to match your environment.

## Goal and concepts

open() opens the CSV. as file gives the open file a name, and with closes it when its block ends. Each call to readline() reads the next line as a string. read() reads everything remaining from the current position.

## Problem 1 — Header and first record

```python
with open("f1_2026_results.csv", encoding="utf-8") as file:  # Open the CSV and name the open file file.
    first_line = file.readline()  # Read the column names from the first line.
    first_record = file.readline()  # Read the first data record from the next line.
    print(first_line)  # Display the column names.
    print(first_record)  # Display the first data record.
```

```text
round,race,circuit,driver,team,grid,position,status,points

1,Australian GP,Albert Park Grand Prix Circuit,RUS,Mercedes,1,1,Finished,25.0
```

The first attempt at reading the second line used read(), which reads from the first record to the end of the file. The learner switched to readline() to read one line. One attempt stored the value as fisrt_record and tried to print first_record. The spelling was made consistent. The blank line occurs because readline() keeps the newline and print() adds another.

## Problem 2 — Data line count

```python
with open("f1_2026_results.csv", encoding="utf-8") as file:  # Reopen the CSV to start at the beginning.
    first_line = file.readline()  # Read the header so the loop skips it.
    count = 0  # Start the data line count at zero.
    for line in file:  # Read the remaining lines one at a time while the file is open.
        count = count + 1  # Add one for each data line.
    print(count)  # Print the total once after the loop ends.
```

```text
418
```

Calling readline() twice would skip the first data line as well as the header. Calling it once skips just the header. The learner moved the for loop inside with so it could read the file while it was open. With print(count) inside the loop, the run printed 1 through 418. Aligning it with for printed 418 once.

## Problem 3 — Meaning of one row

The learner described one row as a driver result. More precisely, each row describes one driver in one race. A driver may appear in several races, so 418 counts race-result records. SQL COUNT(*) counts rows at the same level when the CSV is imported as-is.

## Next lesson

Next is Chapter 4.1 on NumPy array basics. Use the book’s small numeric examples to compare multiplication with lists and arrays, then inspect an array’s shape.
